#
# @author Sebastián Rodríguez Robotham
# base class to post/get http methods
# isSuccessful, 
# httpStatusCode, 
# message, 
# startDate, 
# elapsedTimeMS, 
# transactionId, 
# apiVersion, 
# errors, 
# data, 
# extraInfo, 
# endDate = ""
class HuemulResponseProvider:
    def __init__(self, **args):
        if (len(args) == 0):
            self.isSuccessful = False
            # status code: 200 OK, 500 error, etc
            self.httpStatusCode = ""
            # text to client
            self.message = "not connected"
            self.startDate = ""
            self.endDate = ""
            self.elapsedTimeMS = -1
            self.transactionId = ""
            # api response version
            self.apiVersion = ""

            #error detail
            self.errors = []
            #data detail
            self.dataRaw = ""
            #extra info detail
            self.extraInfoRaw = ""
        else:
            self.fromDict(
                isSuccessful = args["isSuccessful"] if "isSuccessful" in args else "" ,
                httpStatusCode = args["httpStatusCode"] if "httpStatusCode" in args else "" ,
                message = args["message"] if "message" in args else "" ,
                startDate = args["startDate"] if "startDate" in args else "" ,
                elapsedTimeMS = args["elapsedTimeMS"] if "elapsedTimeMS" in args else -1 ,
                transactionId = args["transactionId"] if "transactionId" in args else "" ,
                apiVersion = args["apiVersion"] if "apiVersion" in args else "" ,
                errors = args["errors"] if "errors" in args else [] ,
                data = args["data"] if "data" in args else "" ,
                extraInfo = args["extraInfo"] if "extraInfo" in args else "" ,
                endDate = args["endDate"] if "endDate" in args else "" 
            )
       
    """
    def load_huemul_response_from_json(self, json_data):
        # Define una función que filtra los campos que existen en la estructura de datos
        filtered_json_data = {k: v for k, v in json_data.items() if hasattr(HuemulResponseProvider, k)}
        self.fromDict(**json_data)
    """   


    def fromDict(self, isSuccessful, httpStatusCode, message, startDate, elapsedTimeMS, transactionId, apiVersion, errors, data, extraInfo, endDate = "", *args, **kwargs):
        self.isSuccessful = True if isSuccessful == True else False
        # status code: 200 OK, 500 error, etc
        self.httpStatusCode = httpStatusCode
        # text to client
        self.message = message
        self.startDate = startDate
        self.endDate = endDate
        self.elapsedTimeMS = elapsedTimeMS if elapsedTimeMS >= 0 else -1
        self.transactionId = transactionId
        # api response version
        self.apiVersion = apiVersion

        #error detail
        self.errors = errors
        #data detail
        self.dataRaw = data
        #extra info detail
        self.extraInfoRaw = extraInfo