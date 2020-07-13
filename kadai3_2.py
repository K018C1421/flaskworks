from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    list = {"�p��":87, "���w":90, "����":45, "����":76, "�Љ�":31}
    return render_template('index.html', list=list)

if __name__ == '__main__':
    app.debug = True
    app.run()