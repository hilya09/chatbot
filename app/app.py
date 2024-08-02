# =[Modules dan Packages]========================

from flask import Flask, request, jsonify
from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import nltk
import joblib
import pickle
from joblib import load

# import package untuk safebot
from process import preparation, generate_response

# download nltk
preparation()

# =[Variabel Global]=============================

app = Flask(__name__, static_url_path='/static')
model = None

# =[Routing]=====================================

# [Routing untuk Halaman Utama atau Home]


@app.route("/")
def beranda():
    return render_template('index.html')

# [Routing untuk Halaman Utama atau Home]


@app.route("/chatbot")
def chatbot():
    return render_template('chatbot.html')

# Routing for API response chatbot


@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

# =[Main]========================================

if __name__ == '__main__':

    # Run Flask di localhost
    app.run(host="localhost", port=5000, debug=True)
