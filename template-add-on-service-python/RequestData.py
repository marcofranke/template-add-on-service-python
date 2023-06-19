class RequestData:
    def __init__(self):
        self.oAuthToken = ""
        self.base64Inputdata = ""

    def get_oAuthToken(self):
        return self.oAuthToken

    def set_oAuthToken(self, oAuthToken):
        self.oAuthToken = oAuthToken

    def get_base64Inputdata(self):
        return self.base64Inputdata

    def set_base64Inputdata(self, base64Inputdata):
        self.base64Inputdata = base64Inputdata

    def __str__(self):
        return "RequestData [oAuthToken=" + self.oAuthToken + ", base64Inputdata=" + self.base64Inputdata + "]"
