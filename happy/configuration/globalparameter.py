import time

'''
配置全局参数
'''
project_path = 'G:\\seleniumpython\\happy\\'  # 项目的绝对路径，在Windows上使用时

# 获取项目路径
#project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
print(project_path)

# 测试用例代码存放路径（用于构建suite，注意该文件下的文件都应该以test开头命名）
test_case_path = project_path + "\\test_case"

# excel测试数据文档存放路径
test_data_path = project_path + "\\data\\testData.xlsx"

# 日志文件存储路径
log_path = project_path + "\\log\\mylog.log"
print(u'日志文件：' + log_path)  # u 表示 utf8

# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path + "\\report\\"
report_name = report_path + time.strftime('%Y%m%d%H%S', time.localtime())

# 异常截图存储路径，并以当前时间作为图片名称前缀
img_path = project_path + "\\image\\" + time.strftime('%Y%m%d%H%S', time.localtime())

# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.163.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找，然后可以在foxmail这些工具中验正
email_name = 'zxy_zty12@163.com'  # 发件人名称
email_password = 'zxyzty1314'  # 发件人SMTP的授权密码
email_to = 'zxy.zty@qq.com'  # 收件人
