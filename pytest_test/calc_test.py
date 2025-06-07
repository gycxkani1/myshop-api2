import pytest
from calc import Calc

class TestCalc(): # 类名必须以Test开头，否则找不到
    def setup_class(self):
        print("在每个类之前执行一次"+"\n")
    def teardown_class(self):
        print("在每个类之后执行一次"+"\n")
    def setup_method(self):
        print("在每个方法之前执行"+"\n")
    def teardown_method(self):
        print("在每个方法之后执行"+"\n")
    def test_add(self): # 测试函数必须以test_开头，否则pytest不会识别
        c = Calc()
        result = c.add(2, 3)
        assert result == 5
    def test_sub(self):
        c = Calc()
        result = c.sub(2, 3)
        assert result == -2
if __name__ == '__main__':
    # 运行pytest_test/calc_test.py文件
    pytest.main(["-s","-v","--html=pytest_test/report/report.html","pytest_test/calc_test.py"]) 
#     # -s: 显示print输出
#     # -v: 显示详细信息