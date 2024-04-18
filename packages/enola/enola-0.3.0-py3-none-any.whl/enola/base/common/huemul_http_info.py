#
# @author Sebastián Rodríguez Robotham
# @param body http return body
# @param httpCode http return code
#
class HuemulHttpInfo:
    def __init__(self, body, httpCode):
        self.body = body
        self.httpCode = httpCode