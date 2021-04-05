from flask import Flask, jsonify, abort, request, current_app
from sqlalchemy import create_engine #sqlalchemy helped convert strings to dates seamlessly
import mysql.connector as mysql
import pandas as pd

app = Flask(__name__)

db = mysql.connect(
    # connect to the mysql server running in container with service name: db. CAUTION data here are not persisted past container lifespan
    host = "db",
    user = "root",
    passwd = "root",
    db = "db"
    #,charset='latin1'
    #,collation='latin1_danish_ci'
)
con_str = "mysql+mysqlconnector://root:root@db/db"
engine = create_engine(con_str)


@app.route('/api/links', methods=['GET'])
def get_links():
    cur = db.cursor()
    query = 'select * from dbalinks'
    cur.execute(query)
    print('TABLE COLUMNS: ',cur.column_names,'\n')

    myresult = cur.fetchall()

    for x in myresult:
        print(x)
    return jsonify(myresult)

@app.route('/api/link', methods=['POST'])
def add_link(links=[]):
    con_str = "mysql+mysqlconnector://root:root@db/db"
    engine = create_engine(con_str)
    df = pd.DataFrame({'Links': links}, index=[-1])
    df = df.applymap(str)
    df.to_sql('dbalinks',con=engine, if_exists='append', index = False)
    print('Added:', links)

if __name__ == '__main__':
    app.run(debug=True)