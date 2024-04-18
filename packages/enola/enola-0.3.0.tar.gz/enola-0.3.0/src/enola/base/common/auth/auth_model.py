
# consumerId: String,
# consumerSecret: String,
# orgId: String,
# applicationName: String,
# urlService: String
class AuthModel:
    def __init__(self, consumerId:str = "", consumerSecret:str = "", orgId:str = "", applicationName:str = "", urlService:str = "", sessionId:str = "", jwtToken: str = ""):
        self.consumerId = consumerId
        self.consumerSecret = consumerSecret
        self.orgId = orgId
        self.applicationName = applicationName
        self.urlService = urlService
        self.sessionId = sessionId
        self.jwtToken = jwtToken
        