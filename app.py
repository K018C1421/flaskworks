from flask import Flask, render_template, request, redirect
import mysql.connector as db
import datetime
import os

#import json

db_param = {
    'user' : 'mysql',
    'host' : 'localhost',
    'password' : '',
    'database' : 'tododb'
}

app = Flask(__name__)

#ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif'])
#app.config['UPLOAD_FOLDER'] = './static/uploads'
#
#def allowed_file(filename):
#    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    conn = db.connect(**db_param)
    cur = conn.cursor()
    stmt = 'SELECT * FROM todolist'
    cur.execute(stmt)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', todolist=rows)

@app.route('/send', methods=['POST'])
def send():
    print(request.files)
    dt = datetime.datetime.now()
    date = dt.strftime('%Y-%m-%d %H:%M')
    title = request.form.get('title')
    if date=="" or title=="": 
        return redirect('/')
    
    #if image and allowed_file(image.filename):
    #    image.save('static/uploads/' + image.filename)
    conn = db.connect(**db_param)
    cur = conn.cursor()

    stmt = 'SELECT * FROM todolist WHERE title=%s'
    cur.execute(stmt, (title,))
    rows = cur.fetchall()
    if len(rows)==0:
        cur.execute('INSERT INTO todolist(date, title) VALUES(%s, %s)', (date, title))
    else:
        cur.execute('UPDATE todolist SET date=%s WHERE title=%s', (date, title))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    del_list = request.form.getlist('del_list')
    conn = db.connect(**db_param)
    cur =conn.cursor()
    for id in del_list:
        stmt = 'SELECT * FROM todolist WHERE id=%s'
        cur.execute(stmt, (id,))
        rows = cur.fetchall()
        #os.remove('./static/uploads/' + rows[0][3])
        stmt = 'DELETE FROM todolist WHERE id=%s'
        cur.execute(stmt, (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/')

#@app.route('/data', methods=['GET'])
#def data():
#    keyword = request.args.get('keyword')
#    conn = db.connect(**db_param)
#    cur = conn.cursor()
#    if keyword and keyword != "":
#        stmt = 'SELECT * FROM list WHERE title LIKE %s'
#        cur.execute(stmt, ('%'+keyword+'%',))
#    else:
#        stmt = "SELECT * FROM list"
#        cur.execute(stmt)
#    rows = cur.fetchall()
#    url = 'http://127.0.0.1:5000/static/uploads'
#    data = []
#    for id, title, price, image in rows:
#        data.append({ 'id':id, 'title':title, 'price':price, 'image':url+image })
#    ret = '{"result":' + json.dumps(data) + '}'
#    return ret

if __name__ == '__main__':
    app.debug = True
    app.run()