from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def index():

    POD_NAME = os.environ.get('POD_NAME')
    NODE_NAME = os.environ.get('NODE_NAME')
    POD_NAMESPACE = os.environ.get('POD_NAMESPACE')

    # print like > Container EDU | POD Working : downward-env | nodename : lima-rancher-desktop | namespace : default
    return f"Container EDU | POD Working : {POD_NAME} | nodename : {NODE_NAME} | namespace : {POD_NAMESPACE}"
