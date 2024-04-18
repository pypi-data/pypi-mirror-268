import json
from enola.base.common.huemul_functions import HuemulFunctions
from enola.base.common.huemul_connection import HuemulConnection
from enola.base.common.huemul_response_error import HuemulResponseError
from enola.base.common.huemul_response_to_bloc import HuemulResponseToBloc
from enola.base.enola_types import AgentModel, AgentResponseModel

class EnolaAgentProvider(HuemulResponseToBloc):
    
    #
    # EnolaAgentCreate
    # @param AgentModel AgentModel
    # @return AgentExecuteResponseModel[AgentExecuteResponseModel]
    #
    def enolaAgentCreate(self, agentModel: AgentModel):
        #self = AgentExecuteResponseModel()
        try:
            #print("paso 600")
            hf = HuemulFunctions()
            #print("paso 700")
            hf.deleteArgs(agentModel)
            #print("paso 800")
            #dataIn2 = jsonpickle.encode(agentModel)
            dataIn = json.dumps(agentModel.to_json(), default=lambda o: o.__dict__)
            #dataIn =  agentModel.to_json()

            #print(agentModel.__dict__)
            #dataIn = json.dumps(agentModel, default=lambda obj: obj.__dict__)
            self.message = "starting postRequest"
            huemulResponse = HuemulConnection(connectObject=self.connectObject).postRequest(
                route = "agent/execute/v1/",
                data = dataIn,
            )

            #print("paso 900")
            #get status from connection
            self.message = "starting fromResponseProvider"
            self.fromResponseProvider(huemulResponseProvider = huemulResponse)
            if (self.isSuccessful):
                self.data = [] if len(huemulResponse.dataRaw) == 0 else list(map(lambda x: AgentResponseModel(**x) ,huemulResponse.dataRaw))
        except Exception as e:
            self.errors.append(
                HuemulResponseError(errorId = "APP-101", errorTxt = str(e))
            )

        return self