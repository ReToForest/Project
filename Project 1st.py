from flask import Flask
app = Flask (__name__)


@app.route('/hello',methods=['GET','POST'])
def hello ():
    return "hello world"


@app.route('/hi',methods=['POST'])
def hi():
    return "hi"


# string 接受任意不包含斜杠的文本
# int 接受正整数
# float 接受正浮点数
# path 接受包含斜杠的文本
@app.route('/user/<int:id>')
def index(id):
    if id == 1:
        return "hihihihihihi"
    if id == 2:
        return "heiheiheiheihei"
    if id == 3:
        return "man!"
    return "11111"

if __name__ == '__main__':
    app.run()
