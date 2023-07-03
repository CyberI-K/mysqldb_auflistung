from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL-Konfiguration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'information_schema'

# MySQL-Verbindung initialisieren
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT SCHEMA_NAME FROM SCHEMATA")
    databases = cur.fetchall()
    cur.close()

    return render_template('index.html', databases=databases)


if __name__ == '__main__':
    app.run()