from flask import Flask
from urllib.parse import unquote
app = Flask(__name__)
@app.route("/<path:code>")
def execute(code):
  try:
    return str(eval(unquote(code)))
  except BaseException as e:
    return repr(e)
