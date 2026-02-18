from flask import Flask
app = Flask(__name__)

@app.route("/")
def print_hi():
    return '<html><head><title>主页</title></head>网页正在运行<br><br><footer>Powered By <a href="https://github.com/ExMC-Github/ExRFy-API-Server-Reset">ExRFy API Reset</a></footer></html>'


if __name__ == '__main__':
    app.run()

