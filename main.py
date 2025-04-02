from flask import Flask, request

app = Flask(__name__)


#when we use the @app.route followed by a function we tell flask what endpoint should trigger the function
#in the case the / endpoint triggers the test function when used
@app.route("/", methods=['get'])
def test():
    return "<p>Hello, World!</p>"