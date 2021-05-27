import sys
class PythonLearn(object):
    """重复打印"""
    def print_times(self, var="hello "):
        a = input().split('/')
        b = [int(i) for i in a]
        for i in b:
            sys.stdout.write(str(i) + ' ')
        sys.stdout.write(var * 3 + '\n')

if __name__ == '__main__':
    python_learn = PythonLearn()
    python_learn.print_times("hi ")
