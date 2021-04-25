import my_unittest
import unittest
from TestRunner import HTMLTestRunner
def myRun():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(my_unittest)

    runner = HTMLTestRunner(
        stream=open('mytest.html', "wb"),
        title="我的自动化测试"
    )

    runner.run(suite)

if __name__ == '__main__':
    myRun()