
class HuemulCommon:

    def __init__(self):
        self._serviceUrl = ""

    #
    # return total attemps
    # @return int
    def getTotalAttempt(self):
        return 5

    #**********************************************************************
    #***********  S E R V I C E   U R L    ********************************
    #**********************************************************************

    _serviceUrl = ""

    #
    # get Service Url
    # @return ServiceUrl: string
    def getServiceUrl(self):
        if (self._serviceUrl != "" and self._serviceUrl[-1] != "/"):
            self._serviceUrl = self._serviceUrl + "/"

        return self._serviceUrl


    # set serviceUrl
    # value: string
    def setServiceUrl(self, value):
        self._serviceUrl = value


    #**********************************************************************
    #***********  T O K E N   I D    **************************************
    #**********************************************************************

    #return string
    _tokenId = ""

    #
    # get user Token Id
    # @return TokenId
    #
    def getTokenId(self):
        return self._tokenId

    #
    # set tokenID
    # value: string
    #
    def setTokenId(self, value):
        self._tokenId = value


    #**********************************************************************
    #***********  O R G   I D    **************************************
    #**********************************************************************

    _orgId = ""

    #
    # get user org Id
    # @return orgId
    #
    def getOrgId(self):
        return self._orgId

    #set orgID
    #value: string
    def setOrgId(self, value):
        self._orgId = value


    #**********************************************************************
    #***********  C O N S U M E R   I D    ********************************
    #**********************************************************************

    _consumerId = ""

    #
    # get user Consumer Id
    # @return ConsumerId
    #
    def getConsumerId(self):
        return self._consumerId

    #set consumerID
    def setConsumerId(self, value):
        self._consumerId = value

    #**********************************************************************
    #***********  J W T    T O K E N    ********************************
    #**********************************************************************

    _jwtToken = ""

    #
    # get user Consumer Id
    # @return jwtToken
    #
    def getJwtToken(self):
        return self._jwtToken

    #set jwtToken
    def setJwtToken(self, value):
        self._jwtToken = value

    #**********************************************************************
    #***********  C O N S U M E R   S E C R E T    ************************
    #**********************************************************************

    _consumerSecret = ""

    #
    # get user Consumer Secret
    # @return ConsumerSecret
    #
    def getConsumerSecret(self):
        return self._consumerSecret

    #set consumerSecret
    def setConsumerSecret(self, value):
        self._consumerSecret = value

    #**********************************************************************
    #***********  A P P L I C A T I O N   I D    ********************************
    #**********************************************************************

    _applicationName = ""

    #
    # get user Application Id
    # @return _applicationName
    #
    def getApplicationName(self):
        return self._applicationName

    #set applicationName
    def setApplicationName(self, value):
        self._applicationName = value