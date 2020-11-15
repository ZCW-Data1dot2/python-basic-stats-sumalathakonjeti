from statzcw import zcount,zmed,zmean,zmode,zvariance,zstdev,zcorr,zstderr


file_path ='dataZero.csv'
file_path1 ='dataOne.csv'
file_path2 ='dataTwo.csv'
file_path3='dataThree.csv'
list_x = zcount.get_csv(file_path,'x')
list_x1 = zcount.get_csv(file_path1,'x')
list_x2 = zcount.get_csv(file_path2,'x')
list_x3 = zcount.get_csv(file_path3,'x')
list_y = zcount.get_csv(file_path,'y')
list_y1 = zcount.get_csv(file_path1,'y')
list_y2 = zcount.get_csv(file_path2,'y')
list_y3 = zcount.get_csv(file_path3,'y')
print("dataZero.csv")
print(zcount.zcount1(list_x),zmean.zmean1(list_x),zvariance.find_var(list_x),zmean.zmean1(list_y),zvariance.find_var(list_y),zcorr.correlation(list_x,list_y))
print("dataOne.csv")
print(zcount.zcount1(list_x1),zmean.zmean1(list_x1),zvariance.find_var(list_x1),zmean.zmean1(list_y1),zvariance.find_var(list_y1),zcorr.correlation(list_x1,list_y1))
print("dataTwo.csv")
print(zcount.zcount1(list_x2),zmean.zmean1(list_x2),zvariance.find_var(list_x2),zmean.zmean1(list_y2),zvariance.find_var(list_y2),zcorr.correlation(list_x2,list_y2))
print("dataThree.csv")
print(zcount.zcount1(list_x3),zmean.zmean1(list_x3),zvariance.find_var(list_x3),zmean.zmean1(list_y3),zvariance.find_var(list_y3),zcorr.correlation(list_x3,list_y3))

print("   System Statistics package results    ")
print("dataZero.csv")
print(zmed.zmedian(list_x),zmed.zmedian(list_y),zmode.z_mode(list_x),zmode.z_mode(list_y),zstdev.standard_dev(list_x),zstdev.standard_dev(list_y) ,zstderr.standard_error(list_x),zstderr.standard_error(list_y))
print("dataOne.csv")
print(zmed.zmedian(list_x1),zmed.zmedian(list_y1),zmode.z_mode(list_x1),zmode.z_mode(list_y1),zstdev.standard_dev(list_x1),zstdev.standard_dev(list_y1) ,zstderr.standard_error(list_x1),zstderr.standard_error(list_y1))
print("dataTwo.csv")
print(zmed.zmedian(list_x2),zmed.zmedian(list_y2),zmode.z_mode(list_x2),zmode.z_mode(list_y2),zstdev.standard_dev(list_x2),zstdev.standard_dev(list_y2) ,zstderr.standard_error(list_x2),zstderr.standard_error(list_y2))
print("dataThree.csv")
print(zmed.zmedian(list_x3),zmed.zmedian(list_y3),zmode.z_mode(list_x3),zmode.z_mode(list_y3),zstdev.standard_dev(list_x3),zstdev.standard_dev(list_y3) ,zstderr.standard_error(list_x3),zstderr.standard_error(list_y3))



# print(" Count of X")
# print(zcount.zcount1(list_x),zcount.zcount1(list_x1),zcount.zcount1(list_x2),zcount.zcount1(list_x3))
# print(" Count of Y")
# print(zcount.zcount1(list_y),zcount.zcount1(list_y1),zcount.zcount1(list_y2),zcount.zcount1(list_y3))
# print(" Mean of X")
# print(zmean.zmean1(list_x),zmean.zmean1(list_x1),zmean.zmean1(list_x2),zmean.zmean1(list_x3))
# print("Sample Variance of X")
# print(zvariance.find_var(list_x),zvariance.find_var(list_x1),zvariance.find_var(list_x2),zvariance.find_var(list_x3))
# print(" Mean of Y")
# print(zmean.zmean1(list_y),zmean.zmean1(list_y1),zmean.zmean1(list_y2),zmean.zmean1(list_y3))
# print("Sample Variance of Y")
# print(zvariance.find_var(list_y),zvariance.find_var(list_y1),zvariance.find_var(list_y2),zvariance.find_var(list_y3))
# print("Correlation between X and Y")
# print(zcorr.correlation(list_x,list_y),zcorr.correlation(list_x1,list_y1),zcorr.correlation(list_x2,list_y2),zcorr.correlation(list_x3,list_y3))
# print(" Median of X")
# print(zmed.zmedian(list_x),zmed.zmedian(list_x1),zmed.zmedian(list_x2),zmed.zmedian(list_x3))
# print(" Median of Y")
# print(zmed.zmedian(list_y),zmed.zmedian(list_y1),zmed.zmedian(list_y2),zmed.zmedian(list_y3))
# print(" Mode of X")
# print(zmode.z_mode(list_x),zmode.z_mode(list_x1),zmode.z_mode(list_x2),zmode.z_mode(list_x3))
# print(" Mode of Y")
# print(zmode.z_mode(list_y),zmode.z_mode(list_y1),zmode.z_mode(list_y2),zmode.z_mode(list_y3))
# print(" Standard deviation of X")
# print(zstdev.standard_dev(list_x),zstdev.standard_dev(list_x1),zstdev.standard_dev(list_x2),zstdev.standard_dev(list_x3))
# print(" Standard deviation of Y")
# print(zstdev.standard_dev(list_y),zstdev.standard_dev(list_y1),zstdev.standard_dev(list_y2),zstdev.standard_dev(list_y3))
# print(" Standard error of  X")
# print(zstderr.standard_error(list_x),zstderr.standard_error(list_x1),zstderr.standard_error(list_x2),zstderr.standard_error(list_x3))
# print(" Standard error of  Y")
# print(zstderr.standard_error(list_y),zstderr.standard_error(list_y1),zstderr.standard_error(list_y2),zstderr.standard_error(list_y3))
#
#
