from flask import Flask


app = Flask(__name__)

print("start")

@app.route("/")
def first_learning_tool_step():
    return "<h1>Dubbeldekkerbus</h1>"


