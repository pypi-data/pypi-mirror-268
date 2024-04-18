#
# @author Sebastián Rodríguez Robotham
# error class used by backend to return error info
# @param errorId error Id
# @param errorTxt error Message
#
class HuemulResponseError:
    def __init__(self, errorId, errorTxt):
        self.errorId = errorId
        self.errorTxt = errorTxt