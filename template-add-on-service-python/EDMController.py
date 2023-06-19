import base64
import json
import logging

from LoginController import LoginController
from PublicAPIServiceController import PublicAPIServiceController
from RequestData import RequestData

logger = logging.getLogger(__name__)

class EDMController:
    def __init__(self):
        self.public_api_service = PublicAPIServiceController()
        self.loginController = LoginController()

    def  getRawCodes(selfself, input):
        logger.info("Invoke method: ggetRawCodes")

        return "TBD"

    def getProducts(self, input):
        logger.info("Invoke method: getProducts")

        token = self.loginController.login(input)
        gson = json.dumps(token)
        # token_as_object = json.loads(gson, object_hook=lambda d: Token(**d))

        input_for_service = RequestData()
        input_for_service.oAuthToken = token["token"];


        gson = "{NA}"

        message_bytes = gson.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        gson2 = "{\"oAuthToken\":\"" + input_for_service.oAuthToken + "\",\"base64Inputdata\":\"" + base64_message + "\"}";

        r = self.public_api_service.invoke("getProducts", gson2)
        str = json.dumps(r)


        return str
