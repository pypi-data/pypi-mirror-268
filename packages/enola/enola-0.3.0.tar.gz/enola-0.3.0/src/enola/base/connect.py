from enola.base.common.auth.auth_model import AuthModel
from enola.base.common.huemul_common import HuemulCommon
from enola.base.common.huemul_error import HuemulError
from enola.base.common.huemul_logging import HuemulLogging

# authData: AuthModel
class Connect:
    def __init__(self, authData: AuthModel):
        self.authData = authData
        self.huemulLogging = HuemulLogging()
        self.huemulLogging.logMessageInfo(message = "WELCOME to Enola...")

        self._canExecute = False
        self._isOpen = True
        self._errorMessage = ""
        self.othersParams = []
        self.controlClassName = "" #: String = Invoker(1).getClassName.replace("$", "")
        self.controlMethodName = "" #: String = Invoker(1).getMethodName.replace("$", "")
        #val controlFileName: String = Invoker(1).getFileName.replace("$", "")

        #create error and common object
        self.controlError = HuemulError(orgId=authData.orgId, huemulLogging=self.huemulLogging)
        self.huemulCommon = HuemulCommon()
        
        #valida que jwtToken no sea nulo
        if (authData.jwtToken is None):
            self.huemulLogging.logMessageError(message = "jwtToken is null")
            self._errorMessage = "jwtToken is null"
            self._isOpen = False
            return

        #store credentials and token
        self.huemulCommon.setOrgId(authData.orgId)
        self.huemulCommon.setConsumerId(authData.consumerId)
        self.huemulCommon.setConsumerSecret(authData.consumerSecret)
        self.huemulCommon.setApplicationName(authData.applicationName)
        self.huemulCommon.setJwtToken(authData.jwtToken)
        self.huemulCommon.setTokenId(self.authData.jwtToken)
        self.huemulCommon.setServiceUrl(self.authData.urlService)
        

        self.huemulLogging.logMessageInfo(message = "authorized...")
        self.canExecute = True
        self.huemulLogging.logMessageInfo(message = "STARTED!!!")

        ### END START
        
    def isOpen(self):
        return self._isOpen

    #/************************************************************************************/
    #/******************  R E S U L T S    ***********************************************/
    #/************************************************************************************

    
    

    #/************************************************************************************/
    #/******************  U T I L   F U N C T I O N S    *********************************/
    #/************************************************************************************/

    #
    # true for execute, false can't execute
    # @return
    #
    def canExecute(self):
        return self._canExecute

    #
    # return error message
    # @return
    #
    def getErrorMessage(self):
        return self._errorMessage
    
    