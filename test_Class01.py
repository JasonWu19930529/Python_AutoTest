import time


class TestClass01:

    now = int(time.time())
    # 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
    timeStruct = time.localtime(now)
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", timeStruct)

    def setup_class(self):

        print("自动化测试开始-{}".format(self.strTime))

    def test_method01(self):

        assert 1 == 1

    def test_method02(self):

        assert 2 == 2


    def teardown_class(self):

        print("自动化测试结束-{}".format(self.strTime))