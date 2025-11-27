from flask import Flask, request, redirect, session, render_template_string
from logging.config import dictConfig
from random import randint
import os
import urllib.parse
import time
import hmac
import hashlib
import base64
from urllib.parse import quote


app = Flask(__name__)

print("start")

@app.route("/")
def first_learning_tool_step():
    return "<h1>camion</h1>"


