from enum import Enum
import json

class StepType(Enum):
    TOKEN = "TOKEN"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    IMAGE = "IMAGE"
    DOCUMENT = "DOCUMENT"
    OTHER = "OTHER"

class DataType(Enum):
    TEXT = "TEXT"
    NUMBER = "NUMBER"
    DATE = "DATE"
    BOOLEAN = "BOOLEAN"

class KindType(Enum):
    RECEIVER = "RECEIVER"
    SENDER = "SENDER"

class ErrorType(Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"

class ErrOrWarnKind(Enum):
    """
    EXTERNAL: external agent call generate an unexpected error or warning
    """
    EXTERNAL = "EXTERNAL"
    """
    INTERNAL_CONTROLLED: internal agent call generate an unexpected error or warning
    """
    INTERNAL_CONTROLLED = "INTERNAL_CONTROLLED"
    """
    INTERNAL_TOUSER: controlled error or warning to send to user
    """
    INTERNAL_TOUSER = "INTERNAL_TOUSER"


class ErrorOrWarnModel:
    def __init__(self, id: str, message: str, error_type: ErrorType, kind: ErrOrWarnKind):
        self.id = id
        self.error = message
        self.error_type: ErrorType = error_type
        self.kind: ErrOrWarnKind = kind

    def to_json(self):
        return {
            "id": self.id,
            "error": self.error,
            "error_type": self.error_type.value,
            "kind": self.kind.value
        }
    

class DataListModel:
    def __init__(self, kind: str, name: str, data_type: DataType, value):
        self.kind = kind
        self.name = name
        self.data_type = data_type
        self.value = value

    def to_json(self):
        return {
            "kind": self.kind,
            "name": self.name,
            "data_type": self.data_type.value,
            "value": self.value
        }

class Info:

    def is_numeric(self, value):
        return isinstance(value, (int, float, complex))
    def is_string(self, value):
        return isinstance(value, (str))
    def is_dict(self, value):
        return isinstance(value, (dict))

    def __init__(self, type: str, key: str, value):
        self.type = type
        self.key = key
        #si valor es numerico, asignar
        if (self.is_numeric(value)):
            self.value = value
        elif (self.is_string(value)):
            if (self.is_dict(value)):
                self.value = json.dumps(value)
            else:
                self.value = value
        else:
            self.value = value
        

    def to_json(self):
        return {
            "type": self.type,
            "key": self.key,
            "value": self.value
        }

class ApiDataModel:
    def __init__(self, name: str, method: str, url: str, body: str, header: str, payload: str, description: str):
        self.name = name
        self.method = method
        self.url = url
        self.description = description
        self.body = body
        self.header = header
        self.payload = payload


    def to_json(self):
        return {
            "name": self.name,
            "method": self.method,
            "url": self.url,
            "description": self.description,
            "body": self.body,
            "header": self.header,
            "payload": self.payload
        }

class FileInfoModel:
    def __init__(self, name: str, url: str, type: str, sizeKb: int, description: str):
        self.name = name
        self.url = url
        self.type = type
        self.size = sizeKb
        self.description = description

    def to_json(self):
        return {
            "name": self.name,
            "url": self.url,
            "type": self.type,
            "size": self.size,
            "description": self.description
        }

class DataListModel:
    def __init__(self, kind: KindType, name: str, data_type: DataType, value):
        self.kind = kind
        self.name = name
        self.data_type = data_type
        self.value = value

    def to_json(self):
        return {
            "kind": self.kind.value,
            "name": self.name,
            "data_type": self.data_type.value,
            "value": self.value
        }
    

class AgentModel:
    """
    AgentModel
    """
    def __init__(self, app_id: str, user_id: str, session_id: str, channel_id: str, ip: str, code_api: str, isTest: bool, step_list: list, steps: int, enola_id_prev: str):
        self.app_id = app_id
        self.user_id = user_id
        self.session_id = session_id
        self.channel_id = channel_id
        self.ip = ip
        self.code_api = code_api
        self.isTest = isTest
        #step_list es una lista, generar un arreglo ejecutando el metodo to_json de cada elemento de la lista con map
        self.step_list = step_list
        self.steps = steps
        self.enola_id_prev = enola_id_prev

    def to_json(self):
        return {
            "app_id": self.app_id,
            "user_id": self.user_id,
            "session_id": self.session_id,
            "channel_id": self.channel_id,
            "ip": self.ip,
            "code_api": self.code_api,
            "isTest": self.isTest,
            "step_list": list(map(lambda x: x.to_json(), self.step_list)),
            "steps": self.steps,
            "enola_id_prev": self.enola_id_prev
        }

class AgentResponseModel:
    def __init__(self, enolaId: str, agentDeployId:str, successfull: bool, message: str, enolaApiFeedback: str="", enolaUrlFeedback: str="", **args):
        self.enolaId = enolaId
        self.agentDeployId = agentDeployId
        self.enolaApiFeedback = enolaApiFeedback
        self.enolaUrlFeedback = enolaUrlFeedback
        self.successfull = successfull
        self.message = message
        self.args = args

    def to_json(self):
        return {
            "enolaId": self.enolaId,
            "agentDeployId": self.agentDeployId,
            "successfull": self.successfull,
            "message": self.message,
            "args": self.args
        }


