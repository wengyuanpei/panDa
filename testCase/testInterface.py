# 改脚本目录平级目录下需要创建一个report目录存放报告

from ddt import  ddt,data,unpack
import requests
import json
import time
import os
import unittest

from  scrmV1.configUrl.interfaceUrl import *      #在相同的目录下建一个interfaceUrl 文件，封装测试目录
from scrmV1.configParameter.interfaceParameter import *    #在相同的目录下建一个interfaceUrl 文件，封装测试目录
from scrmV1.common.HTMLTestReport import HTMLTestRunner
from scrmV1.common.reportPath import reportPath

@ddt
class test_Interface(unittest.TestCase):

    def setUp(self):
        print('**********************************测试开始****************************************')

        self.header= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0",
            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type":"application/x-www-form-urlencoded",
            "Authorization":""}




    #使用取数据驱动的方式传参

    # '''
    #用户行为轨迹接口请求头
    @unpack
    @data(
        * paraMeter1()
    )

    #用户行为轨迹接口请求头token值为空接口返回900
    def test_interface_1(self,Authorization,customerId,code):

        print('请求参数1:'+Authorization,'请求参数2:'+customerId,'请求参数3:'+code)
        self.header["Authorization"]=Authorization
        header=self.header

        url=interfaceUrl1()

        params = {
            "customerId":customerId
                }
        rq_get = requests.get(url=url, params=params,headers=header)
        code_rq0=rq_get.status_code
        print('请求状态码'+str(code_rq0))

        # 获取返回状态码
        # print(rq_get.text)

        code_rq1=json.loads(rq_get.text).get('code')
        # print('1返回状态码' +code_rq1)
        #断言
        self.assertEqual(code_rq1,code,'接口返回参数失败')
        print('服务端返回参数',rq_get.text)
        print('***********************************************************************************')
        # print(rq_get.request.headers)
        # print(rq_get.cookies)
        
        
        
        
    #导出客户管理列表接口
    @unpack
    @data(
        * paraMeter2()
    )
    def test_interface_2(self,queryType,customerName,empId,customerSource,customerFollowStateId,followLatestTimeStart,followLatestTimeEnd,code,Authorization):
        
        print('请求参数'+queryType,customerName,empId,customerSource,customerFollowStateId,followLatestTimeStart,followLatestTimeEnd,code,Authorization)
        
        self.header["Authorization"] = Authorization
        header = self.header

        url = interfaceUrl2()

        params={'queryType':queryType,
                'customerName':customerName,
                'empId':empId,
                'customerSource':customerSource,
                'customerFollowStateId':customerFollowStateId,
                'followLatestTimeStart':followLatestTimeStart,
                'followLatestTimeEnd':followLatestTimeEnd
        }

        rq_get = requests.get(url=url, params=params,headers=header)
        # print(rq_get.cookies)
        code_rq01=rq_get.status_code
        print('2请求状态码'+str(code_rq01))
        try:
            code_b=rq_get.text.encode()
            print(code_b)
            self.assertEqual(str(code_rq01), code, '接口返回参数失败')
        except:
            code_back=rq_get.text.encode().decode()[9:12]
            print(rq_get.text.encode().decode()[9:12])
            # print('编码后的文件'+rq_get)
            print('***********************************************************************************')
            #断言
            self.assertEqual(code_back,code,'接口返回参数失败')

    #添加客户跟进记录接口
    @unpack
    @data(
        *paraMeter3()
    )
    def test_interface_3(self,customerId,content,Authorization,code):
        self.header["Authorization"] = Authorization
        header = self.header
        # url=interfaceUrl3()
        url = interfaceUrl3()
        data={
            'customerId':customerId,
            'content':content
        }
        rq_get = requests.post(url=url, data=data, headers=header)

        code_rq0 = rq_get.status_code
        print('请求状态码' + str(code_rq0))

        # 获取返回状态码
        # print(rq_get.text)

        code_rq1 = json.loads(rq_get.text).get('code')
        # print('1返回状态码' +code_rq1)
        # 断言

        print('服务端返回参数', rq_get.text)
        self.assertEqual(code_rq1, code, '接口返回参数失败')
        print('***********************************************************************************')
        # print(rq_get.request.headers)
        # print(rq_get.cookies)

    #查询跟进记录接口   
    @unpack
    @data(
        *paraMeter4()
    )
    def test_interface_4(self,customerId,Authorization,code):

        print('请求参数:'+Authorization,customerId,code)
        self.header["Authorization"]=Authorization
        header=self.header

        url=interfaceUrl4()

        params = {
            "customerId":customerId
                }
        rq_get = requests.get(url=url, params=params,headers=header)
        code_rq0=rq_get.status_code
        print('请求状态码'+str(code_rq0))

        # 获取返回状态码
        # print(rq_get.text)

        code_rq1=json.loads(rq_get.text).get('code')
        # print('1返回状态码' +code_rq1)
        #断言
        self.assertEqual(code_rq1,code,'接口返回参数失败')
        print('服务端返回参数',rq_get.text)
        print('***********************************************************************************')
        # print(rq_get.request.headers)
        # print(rq_get.cookies)

    
    

    #修改跟进记录接口
    @unpack
    @data(
        *paraMeter5()
    )
    def test_interface_4(self,id,content,empId,Authorization,code):

        print('请求参数:'+Authorization,customerId,code)
        self.header["Authorization"]=Authorization
        header=self.header

        url=interfaceUrl5()

        params = {
            "id":id,
            'content':content,
            'empId':empId
                        }
        
        rq_get = requests.put(url=url, params=params,headers=header)
        code_rq0=rq_get.status_code
        print('请求状态码'+str(code_rq0))

        # 获取返回状态码
        # print(rq_get.text)

        code_rq1=json.loads(rq_get.text).get('code')
        # print('1返回状态码' +code_rq1)
        #断言
        self.assertEqual(code_rq1,code,'接口返回参数失败')
        print('服务端返回参数',rq_get.text)
        print('***********************************************************************************')
        # print(rq_get.request.headers)
        # print(rq_get.cookies)
    



    #删除跟进记录
    @unpack
    @data(
        *paraMeter6()
    )
    def test_interface_4(self, id, Authorization, code):
        print('请求参数:' + Authorization, id, code)
        self.header["Authorization"] = Authorization
        header = self.header

        url = interfaceUrl6()

        params = {
            "id": id,
            'content': content,
            'empId': empId
        }

        rq_get = requests.delete(url=url, params=params, headers=header)
        code_rq0 = rq_get.status_code
        print('请求状态码' + str(code_rq0))

        # 获取返回状态码
        # print(rq_get.text)

        code_rq1 = json.loads(rq_get.text).get('code')
        # print('1返回状态码' +code_rq1)
        # 断言
        self.assertEqual(code_rq1, code, '接口返回参数失败')
        print('服务端返回参数', rq_get.text)
        print('***********************************************************************************')
        # print(rq_get.request.headers)
        # print(rq_get.cookies)




    #查询所有客户阶段接口
    @unpack
    @data(
        *paraMeter7()
    )
    def test_interface_4(self, Authorization, code):
        print('请求参数:' + Authorization, id, code)
        self.header["Authorization"] = Authorization
        header = self.header

        url = interfaceUrl7()

        params = {

        }

        rq_get = requests.get(url=url, params=params, headers=header)
        code_rq0 = rq_get.status_code
        print('请求状态码' + str(code_rq0))

        # 获取返回状态码
        # print(rq_get.text)

        code_rq1 = json.loads(rq_get.text).get('code')
        # print('1返回状态码' +code_rq1)
        # 断言
        self.assertEqual(code_rq1, code, '接口返回参数失败')
        print('服务端返回参数', rq_get.text)
        print('***********************************************************************************')
        # print(rq_get.request.headers)
        # print(rq_get.cookies)





        #查询客户阶段详情列表接口
        @unpack
        @data(
            *paraMeter8()
        )
        def test_interface_4(self, Authorization, code):
            print('请求参数:' + Authorization, id, code)
            self.header["Authorization"] = Authorization
            header = self.header

            url = interfaceUrl8()

            params = {

            }

            rq_get = requests.get(url=url, params=params, headers=header)
            code_rq0 = rq_get.status_code
            print('请求状态码' + str(code_rq0))

            # 获取返回状态码
            # print(rq_get.text)

            code_rq1 = json.loads(rq_get.text).get('code')
            # print('1返回状态码' +code_rq1)
            # 断言
            self.assertEqual(code_rq1, code, '接口返回参数失败')
            print('服务端返回参数', rq_get.text)
            print('***********************************************************************************')
            # print(rq_get.request.headers)
            # print(rq_get.cookies)

    # '''

    #删除客户阶段接口
    @unpack
    @data(
        *paraMeter9()
    )
    def test_interface_4(self, id , Authorization , code):
        print('请求参数:' + Authorization, id, code)
        self.header["Authorization"] = Authorization
        header = self.header

        url = interfaceUrl8()

        params = {
            "id":id
        }

        rq_get = requests.delete(url=url, params=params, headers=header)
        code_rq0 = rq_get.status_code
        print('请求状态码' + str(code_rq0))

        # 获取返回状态码
        # print(rq_get.text)

        code_rq1 = json.loads(rq_get.text).get('code')
        # print('1返回状态码' +code_rq1)
        # 断言
        self.assertEqual(code_rq1, code, '接口返回参数失败')
        print('服务端返回参数', rq_get.text)
        print('***********************************************************************************')
        # print(rq_get.request.headers)
        # print(rq_get.cookies)




    def tearDown(self):
        print('******************************************测试结束*****************************************')








#
# if __name__=='__main__':
#     unittest.main()




#获取报告路径
# current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
# absPath = os.path.abspath('../result')
# print('报告创建时间' + current_time)
# repot_path = os.path.join(absPath, 'interface_report' + str(current_time))
# print('测试报告路径', repot_path)

repot_path=reportPath()
#创建目录
# os.mkdir(repot_path)

#加载测试类
suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_Interface))
runner = unittest.TextTestRunner()

# 生成测试报告


repot_path_n = repot_path  + '.html'
fp = open(repot_path_n, 'wb')
reportRun=HTMLTestRunner(stream=fp, title='接口测试报告',
                                       description='接口测试演示报告详情,脚本版本号V202202',
                                        tester='测试人员-翁远陪')


runner.run(suite)
fp.close()
