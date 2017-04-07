from flask import Flask
import flask
import json
import emv_parser

app = Flask(__name__)

@app.route("/parse/<tlv>")
def parse_tlv(tlv):
    tlv_obj = emv_parser.parse(tlv)
    resp = flask.Response(json.dumps( tlv_obj ), status=200)

    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == "__main__":
    app.run()