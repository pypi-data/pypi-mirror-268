from ast import Try
import json
import time
from warnings import catch_warnings
from enola.base.common.huemul_connection import HuemulConnection
from enola.base.common.huemul_response_provider import HuemulResponseProvider
from enola.base.connect import Connect

#
# @author Sebastián Rodríguez Robotham
# base class to create, get, getAll methods exposed to user
# @tparam T class Model
#


class HuemulResponseToBloc(HuemulResponseProvider):
    def __init__(self, connectObject: Connect, **args):
        self.data = "" #huemulResponseProvider.dataRaw
        self.connectObject = connectObject
        self.isSuccessful = False
        # status code: 200 OK, 500 error, etc
        self.httpStatusCode = ""
        # text to client
        self.message = "Not started"
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

        print("paso 100")
        if (len(args) == 1 and "huemulResponseProvider" in args):
            print("paso 200")
            self.fromResponseProvider(args["huemulResponseProvider"])

        


    def fromResponseProvider(self, huemulResponseProvider: HuemulResponseProvider):
        print("paso 300")
        self.data = huemulResponseProvider.dataRaw #huemulResponseProvider.dataRaw
        self.isSuccessful = huemulResponseProvider.isSuccessful
        # status code: 200 OK, 500 error, etc
        self.httpStatusCode = huemulResponseProvider.httpStatusCode
        # text to client
        self.message = huemulResponseProvider.message
        self.startDate = huemulResponseProvider.startDate
        self.endDate = huemulResponseProvider.endDate
        self.elapsedTimeMS = huemulResponseProvider.elapsedTimeMS
        self.transactionId = huemulResponseProvider.transactionId
        # api response version
        self.apiVersion = huemulResponseProvider.apiVersion

        #error detail
        self.errors = huemulResponseProvider.errors
        #data detail
        self.dataRaw = huemulResponseProvider.dataRaw
        #extra info detail
        self.extraInfoRaw = huemulResponseProvider.extraInfoRaw
        print("paso 400")

    #
    #analyze error and determine attempts strategy
    # @param result create/get/getAll response (HuemulResponseBloc type)
    # @param attempt attempt number
    # @return Boolean
    #
    def analyzeErrors(self, attempt):
        print("paso 500")
        continueInLoop = True

        if (self.isSuccessful):
            #all right, exit
            continueInLoop = False
        elif (attempt < self.connectObject.huemulCommon.getTotalAttempt()):
            #send errors
            self.connectObject.huemulLogging.logMessageInfo(f"Error in step {self.message}")
            #self.connectObject.huemulLogging.logMessageInfo(str(self.errors))

            try:
                #errorText = ';'.join(map(lambda x: str(x["errorId"]) + ": " + x["errorTxt"],self.errors))
                errorText = self.message if (len(self.errors) == 0) else ';'.join(map(lambda x: str(x["errorId"]) + ": " + x["errorTxt"],self.errors))
            except Exception as e:
                try:
                    #errorText = ';'.join(map(lambda x: str(x.errorId) + ": " + x.errorTxt,self.errors))
                    errorText = self.message if (len(self.errors) == 0) else ';'.join(map(lambda x: str(x.errorId) + ": " + x.errorTxt,self.errors))
                except Exception as e:
                    errorText = "error try to catch error: " + str(e)

            self.connectObject.huemulLogging.logMessageError("errors details: " + errorText)
            self.connectObject.huemulLogging.logMessageError("errors transaction-id: " + self.transactionId)
            #wait from second attempt
            if (attempt > 1):
                # wait 10 seconds and try to call again
                self.connectObject.huemulLogging.logMessageError("waiting 5 seconds.....")
                time.sleep(5)
            

            #get all possible errors
            try:
                connectionError = len(list(filter(lambda x: x["errorId"] == "APP-101", self.errors)))
            except Exception as e:
                connectionError = len([error for error in self.errors if error.errorId == "APP-101"])
            connectionError = -1 if connectionError == 0 else connectionError

            try:
                unAuthorizedError = len(list(filter(lambda x: x["errorId"] == "2040", self.errors)))
            except Exception as e:
                unAuthorizedError = len([error for error in self.errors if error.errorId == "2040"])
            unAuthorizedError = -1 if unAuthorizedError == 0 else unAuthorizedError

            try:
                forbiddenError = len(list(filter(lambda x: x["errorId"] == "2030", self.errors)))
            except Exception as e:
                forbiddenError = len([error for error in self.errors if error.errorId == "2030"])
            forbiddenError = -1 if forbiddenError == 0 else forbiddenError

            if (forbiddenError):
                self.connectObject.huemulLogging.logMessageError("forbidden")

            if (unAuthorizedError > -1):
                self.connectObject.huemulLogging.logMessageError("attempt " + str(attempt + 1) + " of " + str(self.connectObject.huemulCommon.getTotalAttempt()))
                #check if error = unauthorized, try to login again
                continueInLoop = True
            elif (connectionError > -1):
                self.connectObject.huemulLogging.logMessageError("attempt " + str(attempt + 1) + " of " + str(self.connectObject.huemulCommon.getTotalAttempt()))
                #raised error from HuemulConnection method
                continueInLoop = True
            else:
                #unknown error (maybe data), exit and return error
                continueInLoop = False

        else:
            continueInLoop = False


        return continueInLoop
    