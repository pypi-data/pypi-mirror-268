from enola.base.common.huemul_connection import HuemulConnection
from enola.base.common.huemul_response_to_bloc import HuemulResponseToBloc
from enola.base.connect import Connect
from enola.base.enola_types import AgentModel
from enola.base.internal.enola_agent_provider import EnolaAgentProvider

class EnolaAgentBloc():
    #
    # start enolaAgentCreate
    # @param AgentModel AgentModel
    # @return HuemulResponseBloc[EnolaAgentResponseModel]
    #
    def enolaAgentCreate(self, agentModel: AgentModel, connectObject: Connect):
        continueInLoop = True
        attempt = 0
        #result = HuemulResponseToBloc(connectObject=connectObject)

        while (continueInLoop):
            result = EnolaAgentProvider(connectObject=connectObject).enolaAgentCreate(
                    agentModel=agentModel
            )
            attempt +=1
            continueInLoop = result.analyzeErrors(attempt)
        
        return result