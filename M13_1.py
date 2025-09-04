import json
import math
from flask import Flask, Response
#Task 1
app = Flask(__name__)
@app.route('/prime_number/<num1>')
def isPrimer(num1):
    try:
        num1=int(num1)
        bol=True
        for i in range(2,math.trunc(math.sqrt(num1))+1):
            if (num1%i==0):
                bol=False
            response = {
                "Number" : num1,
                "isPrime" : bol
            }
        return response
    except ValueError:
        response = {
            "message": "Invalid number inputed",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response
@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)            
        

