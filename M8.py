import mariadb
import sys
from geopy import distance

try:
    conn = mariadb.connect(
        user="PLACEHOLDER",
        password="PLACEHOLDER",
        host="localhost",
        port=3306,
        database="flight_game"
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    sys.exit(1)

cur = conn.cursor()
#Task 1
icao=input("Enter ICAO code of airport: ")
sql_code="SELECT name, municipality from airport where ident = ?"
try:
    cur.execute(sql_code,(icao,))
    for (name,municipality) in cur:
        print(f"Name: {name}, town: {municipality}")
except mariadb.Error as e:
    print(f"Error creating table: {e}")    
#Task 2
acode=input("Enter the area code: ")
sql_code2="SELECT name from airport where iso_country = ? order by type"
try:
    cur.execute(sql_code2, (acode,))
    for (name) in cur:
        print(f"Airport name: {name}")
except mariadb.Error as e:
    print(f"Error creating table: {e}")       
#Task 3
ic1=input("Enter the first ICAO code: ")
ic2=input("Enter the second ICAO code: ")
sql_code3="SELECT latitude_deg, longitude_deg FROM airport where ident = ?"
try:
    cur.execute(sql_code3, (ic1,))
    for (latitude_deg, longitude_deg) in cur:
        lat1=latitude_deg
        lon1=longitude_deg
    cur.execute(sql_code3, (ic2,))
    for (latitude_deg, longitude_deg) in cur:
        lat2=latitude_deg
        lon2=longitude_deg
    print(distance.distance((lat1,lon1), (lat2,lon2)).km)
except mariadb.Error as e:
    print(f"Error creating table: {e}")  
cur.close()
conn.close()