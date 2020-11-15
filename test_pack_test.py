from statzcw import zcount,zmed,zmean,zmode,zvariance,zstdev,zcorr,zstderr
import unittest
class Packtest_Test(unittest.TestCase):
    def test_statzcw(self):
        datax = [10,8,13,9,11,14,6,4,12,7,5]
        datay = [9.14,8.14,8.74,8.77,9.26,8.1,6.13,3.1,9.13,7.26,4.74]
        # try:
        assert zcount.zcount1(datax) == 11
        assert zmean.zmean1(datax) == 9.0
        assert zvariance.find_var(datax) == 10.0
        assert zmed.zmedian(datax) == 10.0
        assert zmed.zmedian(datay) == 8.74
        # except AssertionError as e:
        #     print(e)


