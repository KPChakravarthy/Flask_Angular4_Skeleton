import pymysql
import json

def getUsers():
    db = pymysql.connect("sql12.freesqldatabase.com","sql12232432","DS5Nyu2Ts6","sql12232432" )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()
    for row in data:
        print json.dumps(data)
        # print(row[1], row[2], row[3])
    return data
# print(data)