# <>提取参数
# <int:id> int转换器

#自定义转换器

from werkzeug.routing import BaseConverter
from flask import Flask

app = Flask(__name__)

class RegexConverter(BaseConverter):
    '''自定义转换器类'''
    def __init__(self,url_map,regex):
        # 调用父类方法
        super(RegexConverter,self).__init__(url_map)
        self.regex = regex

    def to_python(self, value):
        # 父类方法、功能实现
        print('to-python方法被调用')
        return value
    
# 将自定义的转换器的类添加到flask应用中
app.url_map.converters['re'] = RegexConverter

@app.route('/index/<re("\d{10}"):value>')
def index(value):
    print(value)
    return 'hello!!!'

if __name__ == '__main__':
    app.run()
