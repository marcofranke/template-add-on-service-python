import base64
import json
import logging

from PublicAPIServiceController import PublicAPIServiceController
from RequestData import RequestData
from Token import Token
from User import User
from GetUserInput import GetUserInput

logger = logging.getLogger(__name__)


class LoginController:
    def __init__(self):
        self.public_api_service = PublicAPIServiceController()

    def config(self):
        logger.info("Invoke method: config")

        response = "It uses the public api microservice to get in touch with the TRICK Security Broker"

        return response

    def login(self, input):
        logger.info("Invoke method: login")

        gson = "{\"username\": \"" + input.username + "\",\"password\":\"" + input.password + "\"}";

        message_bytes = gson.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        input_for_service = RequestData()
        input_for_service.base64Inputdata = base64_bytes

        gson2 = "{\"oAuthToken\":\"" + "na" + "\",\"base64Inputdata\":\"" + base64_message + "\"}";
        print(gson2)

        r = self.public_api_service.invoke("login", gson2)

        return r

    def get_user_details(self, input):
        logger.info("Invoke method: get_user_details")

        token = self.login(input)
        gson = json.dumps(token)
        # token_as_object = json.loads(gson, object_hook=lambda d: Token(**d))

        input_for_service = RequestData()
        input_for_service.oAuthToken = token["token"];


        gson = "{\"username\":\"" + input.username + "\"}"

        message_bytes = gson.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        gson2 = "{\"oAuthToken\":\"" + input_for_service.oAuthToken + "\",\"base64Inputdata\":\"" + base64_message + "\"}";

        r = self.public_api_service.invoke("getUserDetails", gson2)
        str = json.dumps(r)
        #user = json.loads(str, object_hook=lambda d: User(**d))

        return str
