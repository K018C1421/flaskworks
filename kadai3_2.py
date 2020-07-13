from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    list = {"‰pŒê":87, "”Šw":90, "‘Œê":45, "—‰È":76, "Ğ‰ï":31}
    return render_template('index.html', list=list)

if __name__ == '__main__':
    app.debug = True
    app.run()