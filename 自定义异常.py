
class MyException(Exception):
    pass

try:
    raise MyException('my exception')
except MyException as e:
    print(e)



class Myerror(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    raise Myerror('自定义异常')
except Myerror as e:
    print('异常类型为：',e.msg)
