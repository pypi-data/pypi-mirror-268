import base64
from enola.base.common.auth.auth_service_model import AuthServiceModel
from enola.base.common.huemul_connection import HuemulConnection
from enola.base.common.huemul_response_error import HuemulResponseError
from enola.base.common.huemul_response_to_bloc import HuemulResponseToBloc

class AuthServiceProvider(HuemulResponseToBloc):
    
    #
    # create new element
    # @param consumerId consumerId: String
    # @param consumerSecret consumerSecret: String
    # @param orgId orgId: String
    # @param applicationName applicationName: String
    #
    def authSignInService(self, consumerId, consumerSecret, orgId, applicationName):
        try:
            dataIn = consumerId + ":" + consumerSecret
            bytes = dataIn.encode('ascii') #.getBytes(StandardCharsets.UTF_8)
            base64Str = base64.b64encode(bytes).decode('ascii')

            huemulResponse = HuemulConnection(connectObject=self.connectObject).authRequest(
                route = "authService/v1/sign-in-service/",
                data = base64Str,
                orgId = orgId
            )

            #get status from connection
            self.fromResponseProvider(huemulResponseProvider = huemulResponse)
            if (self.isSuccessful):
                self.data = [] if len(huemulResponse.dataRaw) == 0 else list(map(lambda x: AuthServiceModel(**x) ,huemulResponse.dataRaw))
        except Exception as e:
            self.errors.append(
                HuemulResponseError(errorId = "APP-101", errorTxt = str(e))
            )

        return self


        