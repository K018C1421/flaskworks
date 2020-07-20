from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    name = request.form.get('name')
    mail = request.form.get('mail')
    return render_template('receive.html', nm=name, ml=mail)

if __name__ == '__main__':
    app.debug = True
    app.run()