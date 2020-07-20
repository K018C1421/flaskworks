from flask import Flask, render_template, request
import datetime

app = Flask(__name__)
timestamp = []
numlist = []

@app.route('/')
def index():
    return render_template('index.html', length=0)

@app.route('/', methods=['POST'])
def send():
    num = request.form.get('num')
    dt_now = datetime.datetime.now()
    timestamp.append(dt_now.strftime('%m/%d %H:%M'))
    numlist.append(num)
    return render_template('index.html', t=timestamp, n=numlist, length=len(numlist))

if __name__ == '__main__':
    app.debug = True
    app.run()