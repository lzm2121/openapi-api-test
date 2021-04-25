import json
import datetime

def json_read():
    data = '{"name": "json","age": 13}'
    data_json = json.loads(data)
    print(data_json)
    print(data_json["name"])
    str_json = json.dumps(data_json)
    print(str_json)
    data1 = {'name': 'Cassie', 'sex': '女', 'grade': '二年级'}
    data_json.update(data1)
    print(data_json)

def time_print():
    now_time = datetime.datetime.now()
    my_time = '2021.3.20 13:40:35'
    print(now_time.strftime('%Y.%m.%d %H:%M:%S')) # 将日期格式转换为字符串格式
    print(datetime.datetime.strptime(my_time, '%Y.%m.%d %H:%M:%S'))  # 将字符串格式转换为日期格式
# 类的初始化方法
class Age:
    def __init__(self, age):
        self.age = age + 1
        self.name = 'Cassie'

    def Setage(self, my_age):
        print(self.name + "'s age is", my_age + self.age)

stu = [{'name': 'Cassie', 'grade': 97}]
def degree(name, grade):
    if not all([name, grade]):
        return {'code': 1, 'msg': "所有参数不能为空"}

    for stu_name in stu:
        if name == stu_name['name']:
            return {'code': 1, 'msg': "该名字已存在"}
    else:
        if grade >= 80:
            return {'code': 0, 'msg': "优秀"}
        elif (grade > 60) and (grade < 80):
            return {'code': 0, 'msg': "合格"}
        else:
            return {'code': 0, 'msg': "不合格"}

def str_related(str):
    if str is not '20001':
        print('两个字符串相等')
    else:
        print(str+'2')
        print('hello')
        print('change')

if __name__ == "__main__":
    json_read()
    time_print()
    age = Age(12)
    my_age = age.Setage(14)
    str_related('20001')