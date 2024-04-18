from enola.base.common.auth.auth_service_provider import AuthServiceProvider

class AuthServiceBloc():
    #
    # start authSignInService
    # @param authModel authModel
    # @return HuemulResponseBloc[AuthServiceModel]
    #
    def authSignInService(self, authModel, connectObject):
        continueInLoop = True
        attempt = 0
        #result = HuemulResponseBloc()

        connectObject.huemulLogging.logMessageInfo("Ground Control station: " + authModel.urlService)
        connectObject.huemulCommon.setServiceUrl(value = authModel.urlService)

        while (continueInLoop):
            result = AuthServiceProvider(connectObject=connectObject).authSignInService(
                consumerId = authModel.consumerId,
                consumerSecret = authModel.consumerSecret,
                orgId = authModel.orgId,
                applicationName = authModel.applicationName
            )

            attempt +=1
            continueInLoop = result.analyzeErrors(attempt)
        

        return result