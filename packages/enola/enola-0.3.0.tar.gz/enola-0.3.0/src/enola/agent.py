#
# true for execute, false can't execute
# @return
#
import jwt
from enola.base.common.huemul_functions import HuemulFunctions
from enola.step import Step
from enola.base.common.auth.auth_model import AuthModel
from enola.base.enola_types import KindType, DataListModel, DataType, ErrOrWarnKind, Info, StepType
from enola.base.connect import Connect
from enola.base.enola_types import AgentModel
from enola.base.internal.enola_agent import create as create_enola_agent


def add_one(number):
    return number + 1

class Agent:
    def __init__(self, token, name, app_id=None, user_id=None, session_id=None, channel_id=None, ip=None, code_api=None, isTest=False, enola_id_prev:str = ""):
        """
        Start agent Execution

        token: jwt token, this is used to identify the agent, request from Admin App
        name: name of this execution
        app_id: id of app, this is used to identify the app who is calling
        user_id: id of external user, this is used to identify the user who is calling
        session_id: id of session of user or application, this is used to identify the session who is calling
        channel_id: web, chat, whatsapp, etc, this is used to identify the channel who is calling
        ip: ip of user or application, this is used to identify the ip who is calling
        code_api: code of api, this is used to identify the api who is calling
        isTest: true if this call is for testing purposes
        enola_id_prev: id of previous call, this is used to link agents sequence
        """
        self.name = name
        self.enola_id_prev = enola_id_prev
        self.enola_id = "" #se obtiene al finalizar la ejecución
        self.agent_deploy_id = ""
        self.hf = HuemulFunctions()
        #Connection data

        #decodificar jwt
        try:
            decoded = jwt.decode(token, algorithms=['none'], options={'verify_signature': False})
            self.agentDeployId = decoded["sub"]
            self.orgId = decoded["orgId"]
            self.serviceAccountId = decoded["id"]
            self.serviceAccountName = decoded["displayName"]
            self.serviceAccountUrl = decoded["url"]
            
            #verify if serviceAccountUrl is empty, return error
            if not self.serviceAccountUrl:
                raise Exception("serviceAccountUrl is empty.")
            if not self.agentDeployId:
                raise Exception("agentDeployId is empty.")
            if not self.orgId:
                raise Exception("orgId is empty.")

        except jwt.ExpiredSignatureError:
            print("token expired.")
        except jwt.DecodeError:
            print("Error decoding token.")
        except jwt.InvalidTokenError:
            print("Invalid Token.")

        self.connection = Connect(AuthModel(jwtToken=token, urlService=self.serviceAccountUrl, orgId=self.orgId))
        

        #user information
        self.app_id = app_id
        self.user_id = user_id
        self.session_id = session_id
        self.channel_id = channel_id
        self.ip = ip
        self.code_api = code_api

        #current date
        self.date_start = self.hf.getDateForApi()
        
        #if is empty or not exist assign false
        self.isTest = isTest
        
        #save steps and informations
        self.step_list = []
        self.steps = 0
        self.first_step = self.new_step(self.name)

    ########################################################################################
    ###############    A G E N T   M E T H O D S     #######################################
    ########################################################################################


    def add_data_received(self, name:str, data, type:DataType):
        """
        add data received from user
        """
        self.first_step.agent_data_list.append(DataListModel(value=data, name=name, data_type=type, kind=KindType.RECEIVER)) 

    def add_data_send(self, name:str, data, type:DataType):
        """
        add data to send to user
        """
        self.first_step.agent_data_list.append(DataListModel(value=data, name=name, data_type=type, kind=KindType.SENDER)) 
        
    def add_custom_info(self, key, value):
        """
        add custom information to agent
        """
        self.first_step.info_list.append(Info(key, value))

    def add_file_link(self, name: str, url: str, type: str, sizeKb: int):
        """
        add file link to agent
        """
        self.first_step.add_file_link(name=name, url=url, type=type, sizeKb=sizeKb)

    def add_tag(self, key: str, value):
        """
        add tag to agent, this tag is used to search in Enola App
        """
        self.first_step.add_tag(key=key, value=value)

    def add_extra_info(self, key: str, value):
        """
        add extra information to agent, this can be used to test or debug
        """
        self.first_step.add_extra_info(key=key, value=value)

    def add_error(self, id: str, message: str, kind: ErrOrWarnKind):
        """
        register error to agent
        """
        self.first_step.add_error(id=id, message=message, kind=kind)

    def add_warning(self, id: str, message: str, kind: ErrOrWarnKind):
        """
        register warning to agent
        """
        self.first_step.add_warning(id=id, message=message, kind=kind)


    def finish_agent(self, successfull: bool):
        """
        register in Enola server
        """
        self.date_end = self.hf.getDateForApi()
        self.duration_in_ms = self.hf.getDifMs(self.date_start, self.date_end)
        self.close_step_others(step=self.first_step, successfull=successfull, others_cost=0, step_id="AGENT")

        #register in server
        print(f'{self.name}: sending to server... ')
        agentModel = AgentModel(
            app_id=self.app_id, 
            enola_id_prev = self.enola_id_prev,
            user_id=self.user_id, 
            session_id=self.session_id, 
            channel_id=self.channel_id, 
            ip=self.ip, 
            code_api=self.code_api, 
            isTest=self.isTest, 
            step_list=self.step_list, 
            steps=self.steps
        )

        #print("paso 10")
        enola_result = create_enola_agent(agentModel=agentModel, connection=self.connection, raiseErrorIfFail=True)
        #show results
        if (enola_result.successfull):
            #obtiene url para evaluación
            #obtiene id de enola
            self.enola_id = enola_result.enolaId
            self.agent_deploy_id = enola_result.agentDeployId


            print(f'{self.name}: finish OK! ')
        else:
            print(f'{self.name}: finish with error: {enola_result.message}')

        return enola_result


    ########################################################################################
    ###############    S T E P   I N F O     ###############################################
    ########################################################################################


    def new_step(self, name: str):
        """
        start new step

        name: name of this step
        """
        #current_step = 
        self.steps += 1
        return Step(name=name)

    def close_step_token(self, step: Step, successfull: bool, token_input_num: int=0, token_output_num: int=0, token_total_num: int=0, token_input_cost: float=0, token_output_cost: float=0, token_total_cost: float=0, enola_id: str="", agent_deploy_id: str="", step_id:str=""):
        """
        close step with token information
        enola_id: If this step was a call to another Enola agent, whether from your own company or another, this is the ID of that agent
        agent_deploy_id: include this if you want to link this step to another agent of another company
        step_id: id of this step, you can use it to link with external calls
        """
        step.enola_id = enola_id
        step.agent_deploy_id = agent_deploy_id
        step.step_id = step_id
        step.stepType = StepType.TOKEN
        step.token.token_input = token_input_num
        step.token.token_output = token_output_num
        step.token.token_total = token_total_num
        step.cost.token_input = token_input_cost
        step.cost.token_output = token_output_cost
        step.cost.token_total = token_total_cost

        step.date_end = self.hf.getDateForApi()
        step.duration_in_ms = self.hf.getDifMs(step.date_start, step.date_end)
        step.successfull = successfull

        self.step_list.append(step)

    def close_step_video(self, step: Step, successfull: bool, video_num: int=0, video_sec: int=0, video_size: int=0, video_cost: float=0, enola_id_prev: str="", agent_deploy_id: str="", step_id:str=""):
        """
        close step with video information

        enola_id_prev: If this step was a call to another Enola agent, whether from your own company or another, this is the ID of that agent
        agent_deploy_id: include this if you want to link this step to another agent of another company
        step_id: id of this step, you can use it to link with external calls
        """
        step.enola_id_prev = enola_id_prev
        step.agent_deploy_id = agent_deploy_id
        step.step_id = step_id
        step.stepType = StepType.VIDEO
        step.video.num_videos = video_num
        step.video.sec_videos = video_sec
        step.video.size_videos = video_size
        step.cost.videos = video_cost
        step.date_end = self.hf.getDateForApi()
        step.duration_in_ms = self.hf.getDifMs(step.date_start, step.date_end)
        step.successfull = successfull

        self.step_list.append(step)
        
    def close_step_audio(self, step: Step, successfull: bool, audio_num:int = 0, audio_sec:int = 0, audio_size:int = 0, audio_cost: float=0, enola_id_prev: str="", agent_deploy_id: str="", step_id:str=""):
        """
        close step with audio information

        enola_id_prev: If this step was a call to another Enola agent, whether from your own company or another, this is the ID of that agent
        agent_deploy_id: include this if you want to link this step to another agent of another company
        step_id: id of this step, you can use it to link with external calls
        """
        step.enola_id_prev = enola_id_prev
        step.agent_deploy_id = agent_deploy_id
        step.step_id = step_id
        step.stepType = StepType.AUDIO
        step.audio.num_audio = audio_num
        step.audio.sec_audio = audio_sec
        step.audio.size_audio = audio_size
        step.cost.audio = audio_cost
        step.date_end = self.hf.getDateForApi()
        step.duration_in_ms = self.hf.getDifMs(step.date_start, step.date_end)
        step.successfull = successfull

        self.step_list.append(step)

    def close_step_image(self, step: Step, successfull: bool, image_num:int = 0, image_size:int = 0, image_cost: float = 0, enola_id_prev3: str="", agent_deploy_id: str="", step_id:str=""):
        """
        close step with image information

        enola_id_prev: If this step was a call to another Enola agent, whether from your own company or another, this is the ID of that agent
        agent_deploy_id: include this if you want to link this step to another agent of another company
        step_id: id of this step, you can use it to link with external calls
        """
        step.enola_id_prev = enola_id_prev
        step.agent_deploy_id = agent_deploy_id
        step.step_id = step_id
        step.stepType = StepType.IMAGE
        step.image.num_images = image_num
        step.image.size_images = image_size
        step.cost.images = image_cost
        step.date_end = self.hf.getDateForApi()
        step.duration_in_ms = self.hf.getDifMs(step.date_start, step.date_end)
        step.successfull = successfull

        self.step_list.append(step)

    def close_step_doc(self, step: Step, successfull: bool, doc_num:int=0, doc_pages:int=0, doc_size:int = 0, doc_char:int=0, doc_cost: float=0, enola_id_prev: str="", agent_deploy_id: str="", step_id:str=""):
        """
        close step with doc information

        enola_id_prev: If this step was a call to another Enola agent, whether from your own company or another, this is the ID of that agent
        agent_deploy_id: include this if you want to link this step to another agent of another company
        step_id: id of this step, you can use it to link with external calls
        """
        step.enola_id_prev = enola_id_prev
        step.agent_deploy_id = agent_deploy_id
        step.step_id = step_id
        step.stepType = StepType.DOCUMENT
        step.doc.num_docs = doc_num
        step.doc.num_pages = doc_pages
        step.doc.size_docs = doc_size
        step.doc.num_char = doc_char
        step.cost.docs = doc_cost
        step.date_end = self.hf.getDateForApi()
        step.duration_in_ms = self.hf.getDifMs(step.date_start, step.date_end)
        step.successfull = successfull

        self.step_list.append(step)

    def close_step_others(self, step: Step, successfull: bool, others_cost: float=0, enola_id_prev: str="", agent_deploy_id: str="", step_id:str=""):
        """
        close step with others information

        enola_id_prev: If this step was a call to another Enola agent, whether from your own company or another, this is the ID of that agent
        agent_deploy_id: include this if you want to link this step to another agent of another company
        step_id: id of this step, you can use it to link with external calls
        """
        step.enola_id_prev = enola_id_prev
        step.agent_deploy_id = agent_deploy_id
        step.step_id = step_id
        step.stepType = StepType.OTHER
        step.cost.others = others_cost
        step.date_end = self.hf.getDateForApi()
        step.duration_in_ms = self.hf.getDifMs(step.date_start, step.date_end)
        step.successfull = successfull

        self.step_list.append(step)

    

    def __str__(self):
        return f'Agente: {self.name}, Pasos: {self.steps}'

