import datetime
from enola.base.common.huemul_functions import HuemulFunctions

from enola.base.enola_types import ApiDataModel, ErrOrWarnKind, ErrorOrWarnModel, ErrorType, FileInfoModel, Info, StepType


class StepCost:
    def __init__(self):
        self.token_input = 0
        self.token_output = 0
        self.token_total = 0
        self.videos = 0
        self.audio = 0
        self.images = 0
        self.docs = 0
        self.infra = 0
        self.others = 0
        self.total = 0

class StepVideo:
    def __init__(self):
        self.num_videos = 0
        self.size_videos = 0
        self.sec_videos = 0

class StepAudio:
    def __init__(self):
        self.size_audio = 0
        self.num_audio = 0
        self.sec_audio = 0

class StepImage:
    def __init__(self):
        self.num_images = 0
        self.size_images = 0

class StepDoc:
    def __init__(self):
        self.num_docs = 0
        self.num_pages = 0
        self.size_docs = 0
        self.num_char = 0

class StepToken:
    def __init__(self):
        self.num_char = 0
        self.token_input = 0
        self.token_output = 0
        self.token_total = 0

class Step:
    def __init__(self, name: str):
        self.hf = HuemulFunctions()
        self.name = name
        self.enola_id = ""
        self.agent_deploy_id = ""
        self.step_id = ""
        self.step_api_code = ""
        self.step_id_prev = ""
        self.date_start = self.hf.getDateForApi()
        self.date_end = self.date_start
        #self.result_list = []
        self.agent_data_list = [] #only for first step
        self.errOrWarn_list = []
        self.extra_info_list = []
        self.file_info_list = []
        self.step_api_data_list = []
        self.stepType:StepType = StepType.OTHER

        self.successfull = False
        self.num_errors = 0
        self.num_warnings = 0

        self.video = StepVideo()
        self.audio = StepAudio()
        self.image = StepImage()
        self.doc = StepDoc()
        self.token = StepToken()
        self.cost = StepCost()
        self.income_total = 0
        self.duration_in_ms = 0        

    def add_api_data(self, bodyToSend: str, payloadReceived: str, name: str, method: str, url: str, description: str = "", headerToSend: str = ""):
        self.step_api_data_list.append(ApiDataModel(name=name, method=method, url=url, body=bodyToSend, header=headerToSend, payload=payloadReceived, description=description)) 
        #{"body": bodyToSend, "header": headerToSend, "payload": payloadReceived})

    def add_file_link(self, name: str, url: str, type: str, sizeKb: int, description: str = ""):
        self.file_info_list.append(FileInfoModel(name=name, url=url, type=type, sizeKb=sizeKb, description=description))
        #{"name": name, "url": url, "type": type, "size": size})

    def add_tag(self, key: str, value):
        self.extra_info_list.append(Info(type="tag", key=key, value=value))
        
    def add_extra_info(self, key: str, value):
        self.extra_info_list.append(Info(type="info", key=key, value=value))

    def add_error(self, id: str, message: str, kind: ErrOrWarnKind):
        self.num_errors += 1
        self.errOrWarn_list.append(ErrorOrWarnModel(id=id, message=message, error_type=ErrorType.ERROR, kind=kind))

    def add_warning(self, id: str, message: str, kind: ErrOrWarnKind):
        self.num_warnings += 1
        self.errOrWarn_list.append(ErrorOrWarnModel(id=id, message=message, error_type=ErrorType.ERROR, kind=kind))

    def to_json(self):
        return {
            "stepId": self.step_id,
            "stepIdPrev": self.step_id_prev,
            "stepDateStart": self.date_start,
            "stepDateEnd": self.date_end,
            "agentDeployId": self.agent_deploy_id,
            "agentExecName": self.name,
            "agentExecDurationMs": self.duration_in_ms,
            "agentExecCliCodeApi": self.step_api_code,
            "agentExecSuccessfull": self.successfull,
            "agentExecNumErrors": self.num_errors,
            "agentExecNumWarnings": self.num_warnings,
            "agentExecNumVideos": self.video.num_videos,
            "agentExecSecVideos": self.video.sec_videos,
            "agentExecSizeAudio": self.video.size_videos,
            "agentExecNumAudio": self.audio.num_audio,
            "agentExecSecAudio": self.audio.sec_audio,
            "agentExecSizeVideos": self.video.size_videos,
            "agentExecNumImages": self.image.num_images,
            "agentExecSizeImages": self.image.size_images,
            "agentExecNumDocs": self.doc.num_docs,
            "agentExecNumPages": self.doc.num_pages,
            "agentExecSizeDocs": self.doc.size_docs,
            "agentExecNumChar": self.doc.num_char + self.token.num_char,
            "agentExecTokenInput": self.token.token_input,
            "agentExecTokenOutput": self.token.token_output,
            "agentExecTokenTotal": self.token.token_total,
            "agentExecCostTokenInput": self.cost.token_input,
            "agentExecCostTokenOutput": self.cost.token_output,
            "agentExecCostTokenTotal": self.cost.token_total,
            "agentExecCostVideos": self.cost.videos,
            "agentExecCostAudio": self.cost.audio,
            "agentExecCostImages": self.cost.images,
            "agentExecCostDocs": self.cost.docs,
            "agentExecCostInfra": self.cost.infra,
            "agentExecCostOthers": self.cost.others,
            "agentExecCostTotal": self.cost.total,
            "agentExecIncomeTotal": self.income_total,

            "agentData": list(map(lambda x: x.to_json(), self.agent_data_list)),
            "errorOrWarning": list(map(lambda x: x.to_json(), self.errOrWarn_list)),
            "extraInfo": list(map(lambda x: x.to_json(), self.extra_info_list)),
            "fileInfo": list(map(lambda x: x.to_json(), self.file_info_list)),
            "stepApiData": list(map(lambda x: x.to_json(), self.step_api_data_list)),
        }

    def __str__(self):
        return f'Step: {self.description}, Duración: {self.duration} segundos'
