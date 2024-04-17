# -*- coding: utf-8 -*-
# (C) Run, Inc. 2022
# All rights reserved (Author BinZHU)
# Licensed under Simplified BSD License (see LICENSE)

import os
import sys
import time
import datetime
import argparse
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

from openfinance.service.error import StatusCodeEnum

model = SentenceTransformer('flax-sentence-embeddings/all_datasets_v4_MiniLM-L6')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = "application/json;charset=utf-8"

@app.route('/', methods=['GET', 'POST'])
def connect():

    ret = jsonify(message="Congrats! Connected!",
                  status=StatusCodeEnum.OK.code)
    return ret

def get_embedding(query):
    embeddings = model.encode(query)
    return embeddings.tolist()

@app.route('/predict', methods=['POST'])
def predict():
    start_time = time.time()
    data = request.get_json(force=True)
    inputs = data["texts"]
    result = get_embedding(inputs)
    print(result)
    end_time = time.time()
    ret = jsonify(embedding=result,
                  message=StatusCodeEnum.OK.msg,
                  status=StatusCodeEnum.OK.code)
    return ret

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="port id", type=int, default=5008)
    parser.add_argument("-l", "--localhost",
                        help="local host", type=int, default=1)
    args = parser.parse_args()

    if args.localhost:
        app.run(port=args.port, debug=True)
    else:
        # set port into 5000 and debug is True
        app.run(port=args.port, debug=False, host="0.0.0.0")  # 开启对外服务

