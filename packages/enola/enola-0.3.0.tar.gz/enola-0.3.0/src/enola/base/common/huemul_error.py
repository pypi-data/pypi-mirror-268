 # errorTrace, 
 # errorClassName, 
 # errorFileName, 
 # errorLineNumber, 
 # errorMethodName, 
 # errorMessage, 
 # errorIsError, 
 # errorCode
class HuemulError:
    def __init__(self, orgId, huemulLogging, **args):
        self.errorId = ""
        self.orgId = orgId
        self.errorDetail = ""
        self.errorWhoIs = ""
        self.errorWhoCode = ""
        self.huemulLogging = huemulLogging

        if (len(args) == 0):
            #val Invoker: Array[StackTraceElement] = new Exception().getStackTrace
            self.errorIsError = False
            self.errorCode = ""
            self.errorTrace = ""
            self.errorClassName = ""
            self.errorFileName = "" # Invoker(3).getFileName //todo: obtener dinamicamente a partir de los nombres de las clases (descartando)
            self.errorLineNumber = "" #Invoker(3).getLineNumber
            self.errorMethodName = ""
            self.errorMessage = ""
        elif (len(args) == 4):
            #val Invoker: Array[StackTraceElement] = new Exception().getStackTrace
            self.errorIsError = True
            self.errorCode = args["code"]
            self.errorTrace = ""
            self.errorClassName = args["getClassName"]
            self.errorFileName = "" # Invoker(3).getFileName //todo: obtener dinamicamente a partir de los nombres de las clases (descartando)
            self.errorLineNumber = "" #Invoker(3).getLineNumber
            self.errorMethodName = args["getMethodName"]
            self.errorMessage = args["message"]

            self.printError(self.errorMessage)
        elif len(args) > 4:
            self.errorTrace = args["errorTrace"]
            self.errorClassName = args["errorClassName"]
            self.errorFileName = args["errorFileName"]
            self.errorLineNumber = args["errorLineNumber"]
            self.errorMethodName = args["errorMethodName"]
            self.errorMessage = args["errorMessage"]
            self.errorIsError = args["errorIsError"]
            self.errorCode = args["errorCode"]


    # return boolean
    def isOK(self):
        return not (self.errorIsError)

    
    def printError(self, error):
        self.huemulLogging.logMessageError("***************************************************************")
        self.huemulLogging.logMessageError("HuemulLauncher: Error Detail")
        self.huemulLogging.logMessageError("***************************************************************")
        self.huemulLogging.logMessageError("error_ClassName: " + self.errorClassName)
        self.huemulLogging.logMessageError("error_FileName: " + self.errorFileName)
        self.huemulLogging.logMessageError("error_ErrorCode: " + self.errorCode)
        self.huemulLogging.logMessageError("error_LineNumber: " + self.errorLineNumber)
        self.huemulLogging.logMessageError("error_MethodName: " + self.errorMethodName)
        self.huemulLogging.logMessageError("error_Message: " + self.errorMessage)
        self.huemulLogging.logMessageError("error_Trace: " + self.errorTrace)

        self.huemulLogging.logMessageError("Detail")
        self.huemulLogging.logMessageError(error)

