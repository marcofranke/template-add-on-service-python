import flask
from flask import Flask

import GetUserInput
from EDMController import EDMController
from LoginInput import LoginInput
from LoginController import LoginController

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, I am the de.biba.trick.template.add.on.service for TRICK. You can just add an RESTController to get in touch with all TRICK functions"


@app.route('/getUserDetails')
def getUserDetails():
    loginController = LoginController();
    input = LoginInput()
    input.set_username("fma@biba.uni-bremen.de");
    input.set_password("mY8422cTya");
    user = loginController.get_user_details(input);
    return user

@app.route('/getProducts')
def getProducts():
    edmController = EDMController();
    input = LoginInput()
    input.set_username("fma@biba.uni-bremen.de");
    input.set_password("mY8422cTya");
    products = edmController.getProducts(input);
    return products

@app.route('/checkWhetherUserIsExporter')
def checkWhetherUserIsExporter():
    loginController = LoginController();
    input = LoginInput()
    input.set_username("fma@biba.uni-bremen.de");
    input.set_password("mY8422cTya");
    # Your source code
    return "False"

@app.route('/getRawCodes')
def getRawCodes():
    oginController = LoginController();
    input = LoginInput()
    input.set_username("fma@biba.uni-bremen.de");
    input.set_password("mY8422cTya");
    edmController = EDMController();
    # Your source code
    return edmController.getRawCodes(input);


if __name__ == '__main__':
    app.run(port=8072)  # Set the desired port number here