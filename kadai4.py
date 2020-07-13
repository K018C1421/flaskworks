from flask import Flask, render_template

app = Flask(__name__)
profilelist = []

@app.route('/user/<username>/')
def addprofile(username):
    profilelist.append(username)
    return render_template('index.html', profile=username)

@app.route('/list/')
def showlist():
    return render_template('list.html', list=profilelist)

if __name__ == '__main__':
    app.debug = True
    app.run()