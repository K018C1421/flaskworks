import datetime
import calendar
from flask import Flask

app = Flask(__name__)

@app.route('/')

def dt():
    Dt = datetime.datetime.now()
    strDt = Dt.strftime('%m/%d %H:%M')
    return strDt

if __name__ == '__main__':
    app.debug = True
    app.run()