#!flask/bin/python
from flask import Flask, render_template
from flaskrun import flaskrun


application = Flask(__name__)


@application.route('/', methods=['GET'])
def get():
    return render_template("index.html")

# @application.route("/")
# def index():
#     # fig = plt.figure(dpi=2000)
#     # ax = fig.add_subplot(111)
#     # ax.plot([-1, -4.5, 16, -2, 23,0,30,3,20])
#     # fig.savefig("./hbrar.github.io_2.0/static/images/binanceApi.png")
#     return render_template("index.html")

# @application.route('/', methods=['POST'])
# def post():
#     return '{"Output":"Hello World"}'

@application.route("/binanceApi")
def helloWorld():
    return render_template("binanceApi.html")
    
if __name__ == '__main__':
    flaskrun(application)
