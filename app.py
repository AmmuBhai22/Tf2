from flask import Flask, make_response

import requests

app = Flask(__name__)

API_ENDPOINT = "https://bldcmprod-cdn.toffeelive.com/"

headers = {

    "Cookie": "Edge-Cache-Cookie=URLPrefix=aHR0cHM6Ly9ibGRjbXByb2QtY2RuLnRvZmZlZWxpdmUuY29tLw:Expires=1687300795:KeyName=prod_linear:Signature=nIzw2EzgOAck_WNIgmnHYOrTD8taW6g5MjRupBozwsUuoNhnncaFn9SnEbrrwZOjfwqAHXIAyWElcYqgKnt1Ag"

}

@app.route("/")

def credit():

    return "(Toffee-API)"

@app.route("/auto/<string:channel_id>.m3u8")

def handle_auto(channel_id):

    response = requests.get(API_ENDPOINT + f"cdn/live/{channel_id}/playlist.m3u8", headers=headers)

    myresponse = make_response(response.text.replace("../slang/", "/single/slang/").replace("?", "-"))

    myresponse.headers["Access-Control-Allow-Headers"]="Origin, Content-Type, Accept"

    myresponse.headers["Access-Control-Allow-Methods"]="GET, OPTIONS"

    myresponse.headers["Content-Type"] = "application/vnd.apple.mpegurl"

    myresponse.headers["Access-Control-Allow-Origin"]="*"

    return myresponse

@app.route("/single/<path:path>")

def handle_single(path):

    single_url = API_ENDPOINT + "cdn/live/" + path.replace("-", "?")

    print(single_url)

    response = requests.get(single_url, headers=headers)

    myresponse = make_response(response.text.replace("/live/", f"/ts/live/"))

    myresponse.headers["Access-Control-Allow-Origin"]="*"

    myresponse.headers["Access-Control-Allow-Headers"]="Origin, Content-Type, Accept"

    myresponse.headers["Access-Control-Allow-Methods"]="GET, OPTIONS"

    myresponse.headers["Content-Type"] = "application/vnd.apple.mpegurl"

    return myresponse

@app.route("/ts/<path:tspath>")

def handle_ts(tspath):

    ts_url="https://bldcmprod-cdn.toffeelive.com/" + str(tspath)

    resp=requests.get(ts_url) 

    out=make_response(resp.content)

    out.headers["Access-Control-Allow-Origin"]="*"

    out.headers["Access-Control-Allow-Headers"]="Origin, Content-Type, Accept"

    out.headers["Access-Control-Allow-Methods"]="GET, OPTIONS"

    out.headers["Content-Type"] = "application/octet-stream"

    return out

  

"""

if __name__ == "__main__":

    app.run(debug=True)

"""
