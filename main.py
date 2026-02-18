from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def index():
    return '<html><head><title>主页</title></head>网页正在运行<br><br><footer>Powered By <a href="https://github.com/ExMC-Github/ExRFy-API-Server-Reset">ExRFy API Reset</a></footer></html>'

@app.route("/favicon.ico")
def icon():
    try:
        file = open("favicon.ico", 'rb').read()
        return file
    except:
        return "Not Found",404
if __name__ == '__main__':
    app.run()

