import json
import string
import random
import base64
from ..models import CommandDetails, AnedyaEncoder
from enum import Enum
from ..errors import AnedyaInvalidConfig, AnedyaInvalidType, AnedyaTxFailure
from ..config import ConnectionMode


class CommandStatus(Enum):
    PENDING = "pending"
    RECEIVED = "received"
    PROCESSING = "processing"
    SUCCESS = "success"
    FAILURE = "failure"
    INVALIDATED = "invalidated"


def update_command_status(self, command: CommandDetails, status: CommandStatus, ackdata: str | bytes | None = None, acktype: str = "string", timeout: float | None = None) -> None:
    """
    Update status of a command

    Args:
        command (CommandDetails): Command object of which status needs to be updated
        status (CommandStatus): New status of the command
        ackdata (str | bytes | None, optional): Data to be submitted along with acknowledgement. Maximum 1 kB of data is allowed. Defaults to None.
        acktype (str, optional): Specify the type of data submitted. Defaults to "string".
        timeout (float | None, optional): Time out in seconds for the request. In production setup it is advisable to use a timeout or else your program can get stuck indefinitely. Defaults to None.

    Raises:
        AnedyaInvalidConfig: Invalid configuration
        AnedyaInvalidType: Invalid datatype is specified
        AnedyaTxFailure: Transaction failure
    """
    if self._config is None:
        raise AnedyaInvalidConfig('Configuration not provided')
    if self._config.connection_mode == ConnectionMode.HTTP:
        return _update_command_status_http(self, command=command, status=status, timeout=timeout)
    elif self._config.connection_mode == ConnectionMode.MQTT:
        return _update_command_status_mqtt(self, command=command, status=status, timeout=timeout)
    else:
        raise AnedyaInvalidConfig('Invalid connection mode')


def _update_command_status_http(self, command: CommandDetails, status: CommandStatus, ackdata: str | tuple | None = None, acktype: str = "string", timeout: float | None = None) -> None:
    if self._config._testmode:
        url = "https://device.stageapi.anedya.io/v1/submitData"
    else:
        url = self._baseurl + "/v1/submitData"
    d = _UpdateCommandStatusReq("req_" + ''.join(random.choices(string.ascii_letters + string.digits, k=16)), command=command, status=status, ackdata=ackdata, acktype=acktype)
    r = self._httpsession.post(url, data=d.encodeJSON(), timeout=timeout)
    # print(r.json())
    try:
        jsonResponse = r.json()
        payload = json.loads(jsonResponse)
        if payload['success'] is not True:
            raise AnedyaTxFailure(payload['error'], payload['errCode'])
    except ValueError:
        raise AnedyaTxFailure(message="Invalid JSON response")
    return


def _update_command_status_mqtt(self, command: CommandDetails, status: CommandStatus, ackdata: str | tuple | None = None, acktype: str = "string", timeout: float | None = None) -> None:
    # Create and register a transaction
    tr = self._transactions.create_transaction()
    # Encode the payload
    d = _UpdateCommandStatusReq(tr.get_id(), command=command, status=status, ackdata=ackdata, acktype=acktype)
    payload = d.encodeJSON()
    # Publish the message
    # print(payload)
    topic_prefix = "$anedya/device/" + str(self._config._deviceID)
    # print(topic_prefix + "/submitData/json")
    msginfo = self._mqttclient.publish(topic=topic_prefix + "/commands/updateStatus/json",
                                       payload=payload, qos=1)
    try:
        msginfo.wait_for_publish(timeout=timeout)
    except ValueError:
        raise AnedyaTxFailure(message="Publish queue full")
    except RuntimeError as err:
        raise AnedyaTxFailure(message=str(err))
    # Wait for transaction to complete
    tr.wait_to_complete()
    # Transaction completed
    # Get the data from the transaction
    data = tr.get_data()
    # Clear transaction
    self._transactions.clear_transaction(tr)
    # Check if transaction is successful or not
    if data['success'] is not True:
        raise AnedyaTxFailure(data['error'], data['errCode'])
    return


class _UpdateCommandStatusReq:
    def __init__(self, reqId: str, command: CommandDetails, status: CommandStatus, ackdata: str | bytes | None = None, acktype: str = "string"):
        self.command_id = command.id
        self.reqID = reqId
        self.status = status
        if acktype == "string":
            if isinstance(ackdata, str):
                raise AnedyaInvalidType('ackdata is not a valid str')
            self.ackdata = ackdata
            self.acktype = "string"
        elif acktype == "binary":
            if isinstance(ackdata, bytes):
                raise AnedyaInvalidType('ackdata is not a valid list')
            self.ackdata_binary = ackdata
            self.ackdata = base64.b64encode(self.ackdata_binary).decode('ascii')
            self.acktype = "binary"
        else:
            raise AnedyaInvalidType('Invalid acktype')

    def toJSON(self):
        dict = {
            "reqId": self.reqID,
            "commandId": str(self.command_id),
            "status": self.status,
            "ackdata": self.ackdata,
            "ackdatatype": self.acktype
        }
        return dict

    def encodeJSON(self):
        data = json.dumps(self, cls=AnedyaEncoder)
        return data
