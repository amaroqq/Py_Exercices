import json
import mariadb

from flask import Flask, Response

app = Flask(__name__)
@app.route('/airport/<icao>')
def icaotest(icao):  
    try:
        conn = mariadb.connect(
            user="PLACEHOLDER",
            password="PLACEHOLDER",
            host="localhost",
            port=3306,
            database="flight_game"
        )
        cur = conn.cursor()
        icao=str(icao)
        sql_code="SELECT name, municipality from airport where ident = ?"
        cur.execute(sql_code,(icao,))
        for (name,municipality) in cur:
            response= {
                "ICAO" : icao,
                "Name": name,
                "Location": municipality
            }
        return response
    except ValueError:
        response = {
            "message": "Invalid number as addend",
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