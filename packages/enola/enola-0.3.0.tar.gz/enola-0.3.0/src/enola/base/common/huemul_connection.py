import requests
from enola.base.common.huemul_http_info import HuemulHttpInfo
from enola.base.common.huemul_response_provider import HuemulResponseProvider
from enola.base.common.huemul_response_error import HuemulResponseError
import json

from enola.base.connect import Connect

class HuemulConnection:
    def __init__(self, connectObject: Connect):
        self.connectObject = connectObject
        #self.httpClient: CloseableHttpClient = HttpClients.createDefault


    #
    # get HTTP call to post method
    # @param route url
    # @param data info to be sent to post method
    # @return
    #
    def authRequest(self, route, data, orgId):
        if (self.connectObject.huemulCommon.getServiceUrl() == ""):
            raise NameError('API Url null or empty')

        httpInfo = HuemulHttpInfo("", -1)

        try:
            # create object
            uriFinal = self.connectObject.huemulCommon.getServiceUrl() + route

            #add header
            headers = self.getHeaderForAuth({
                "authorization" : "Basic " + data,
                "orgId": orgId,
            })

            payload = "".format("")
            httpInfo = requests.request("POST", uriFinal, data=payload, headers=headers)
            # print(response.text)
        except Exception as e:
            print(e)
            

        value = self._getResponse(httpInfo)
        return value
        

    #
    # get HTTP call to post method
    # @param route url
    # @param queryParams query params
    # @param data info to be sent to post method
    # @return
    #
    def postRequest(self, route, data, queryParams = [], headerParams = None):
        if (self.connectObject.huemulCommon.getServiceUrl() == ""):
            raise NameError('API Url null or empty')

        routeParams = ""
        for i in range(len(queryParams)):
            routeParams = routeParams + ("?" if i == 0 else "&") + str(queryParams[0].name) + "=" + str(queryParams[0].value)
        
        httpInfo = HuemulHttpInfo("", -1)

        try:
            # create object
            uriFinal = self.connectObject.huemulCommon.getServiceUrl() + route + routeParams

            #add header
            headers = self.getHeader(headerParams=headerParams)

            payload = data #"".format("")
            httpInfo = requests.request("POST", uriFinal, data=payload, headers=headers)
            # print(response.text)
        except Exception as e:
            print(e)
            
        value = self._getResponse(httpInfo)
        return value

    #
    # get HTTP call to post method
    # @param route url
    # @param queryParams query params
    # @param data info to be sent to put method
    # @return
    #
    def putRequest(self, route, data, queryParams = []):
        if (self.connectObject.huemulCommon.getServiceUrl() == ""):
            raise NameError('API Url null or empty')

        routeParams = ""
        for i in range(len(queryParams)):
            routeParams = routeParams + ("?" if i == 0 else "&") + str(queryParams[0].name) + "=" + str(queryParams[0].value)
        
        httpInfo = HuemulHttpInfo("", -1)

        try:
            # create object
            uriFinal = self.connectObject.huemulCommon.getServiceUrl() + route + routeParams

            #add header
            headers = self.getHeader(headerParams=None)

            payload = data #"".format("")
            httpInfo = requests.request("PUT", uriFinal, data=payload, headers=headers)
            # print(response.text)
        except Exception as e:
            print(e)
            
        value = self._getResponse(httpInfo)
        return value

    #
    # common header for each http method
    # headerParams: Dictionary
    # @return Dictionary
    #
    def getHeaderForAuth(self, headerParams):
        dataToReturn = {
            "Accept" : "application/json",
            "content-type" : "application/json",
            "huemul-client-language" : "PYTHON",
            "huemul-client-version" : "1.0",
            "huemul-client-app" : "SERVER",
            "huemul-client-info" : "",
        }

        if (headerParams != None):
            dataToReturn.update(headerParams)

        return dataToReturn


    #
    # common header for each http method
    # headerParams: Dictionary
    # @return Dictionary
    #
    def getHeader(self, headerParams):
        dataToReturn = {
            "Accept" : "application/json",
            "content-type" : "application/json",
            "huemul-client-language" : "PYTHON",
            "huemul-client-version" : "1.0",
            "huemul-client-app" : "SERVER",
            "huemul-client-info" : "",
            "authorization": "Bearer " + self.connectObject.huemulCommon.getTokenId(),
            "orgId" : self.connectObject.huemulCommon.getOrgId()
        }

        if (headerParams != None): 
            dataToReturn.update(headerParams)

        return dataToReturn


    # transform data from api to response
    # response: HuemulHttpInfo
    # return HuemulResponseProvider
    def _getResponse(self, response):
        huemulResponse = HuemulResponseProvider()

        try:
            if (response.text != ""):
                dataFromJson = json.loads(response.text)
                huemulResponse.fromDict(**dataFromJson)
            else:
                huemulResponse.isSuccessful = False
                huemulResponse.errors.append(HuemulResponseError(errorId = "getResponseError", errorTxt = f'status {response.status_code}: response.text is empty'))
                huemulResponse.httpStatusCode = response.status_code
                huemulResponse.message = response.reason
            
            #huemulResponse.fromDict(**dataFromJson) #HuemulResponseProvider.fromJson(response.text)
        except Exception as e:
            #huemulResponse.isSuccessful = false;
            huemulResponse.errors.append(HuemulResponseError(errorId = "getResponseError", errorTxt = str(e)))
        
        return huemulResponse