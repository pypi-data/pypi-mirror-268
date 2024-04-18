from enola.base.connect import Connect
from enola.base.enola_types import AgentResponseModel
from enola.base.enola_types import AgentModel
from enola.base.internal.enola_agent_bloc import EnolaAgentBloc


def create(agentModel: AgentModel, connection: Connect, raiseErrorIfFail = True):
    #print("paso 20")
    if (not connection.canExecute):
        connection.huemulLogging.logMessageError(message = "cant execute: ")
        return AgentResponseModel(
            enolaId = "",
            agentDeployId = "",
            enolaApiFeedback="",
            enolaUrlFeedback="",
            successfull = False,
            message = "cant execute:"
        )

    #print("paso 30")
    connection.huemulLogging.logMessageInfo(message = "creating Enola Agent")

    enolaAgentResult = EnolaAgentBloc().enolaAgentCreate(agentModel=agentModel,connectObject=connection)
    #print("paso 40")
    #if error
    if (not enolaAgentResult.isSuccessful):
        #print("paso 50")
        print(enolaAgentResult)
        connection._canExecute = False
        try:
            connection._errorMessage = enolaAgentResult.message if (len(enolaAgentResult.errors) == 0) else enolaAgentResult.errors[0]["errorTxt"]
        except:
            connection._errorMessage = enolaAgentResult.message if (len(enolaAgentResult.errors) == 0) else enolaAgentResult.errors[0].errorTxt

        #print("paso 60")

        connection.huemulLogging.logMessageError(message = "error in enolaAgent: " + connection._errorMessage)

        if (raiseErrorIfFail):
            connection.huemulLogging.logMessageError(message = "error" + connection._errorMessage)
            raise NameError(connection._errorMessage)
        else:
            connection.huemulLogging.logMessageError(message = "error" + connection._errorMessage)
            return AgentResponseModel(
                enolaId = "",
                agentDeployId = "",
                enolaApiFeedback="",
                enolaUrlFeedback="",
                successfull = False,
                message = "error" + connection._errorMessage
            )

    #if all ok, continue
    # connectObject._processExecStepId = enolaAgentResult.data[0].processExecStepId

    return AgentResponseModel(
        #enolaId = enolaAgentResult.data["enolaId"],
        #agentDeployId = enolaAgentResult.data["agentDeployId"],
        #enolaApiFeedback = enolaAgentResult.data.agentApiFeedback if hasattr(enolaAgentResult.data, "agentApiFeedback") else "",
        #enolaUrlFeedback = enolaAgentResult.data.enolaUrlFeedback if hasattr(enolaAgentResult.data, "agentUrlFeedback") else "",
        successfull = enolaAgentResult.isSuccessful,
        message = enolaAgentResult.message,
        **enolaAgentResult.data
    )