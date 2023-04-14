#app.py
#flask 에서 Flask, render_template 임포트
from flask import Flask, render_template
from flask import request

#Flask 객체 인스턴스 생성
app = Flask(__name__)

#/으로 접속시 실행
@app.route('/') #접속하는 url 매핑
def index():

    return render_template('index5.html')    #리턴할 html 지정

@app.route('/test') #접속하는 url 매핑
def index2():

    return render_template('index2.html') 

if __name__ == '__main__' :
    app.run(debug=True)