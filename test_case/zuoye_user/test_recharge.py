import pytest

from tools.api import request_tool
from tools.data import excel_tool

# data = excel_tool.get_test_case("test_case/zuoyeuser/充值接口测试数据.xlsx")
#
# @pytest.mark.parametrize("account_name,money,expect",data[1],ids=data[0])
# def test_recharge_recharge(pub_data,account_name,money,expect):
#     pub_data["account_name"] = account_name
#     pub_data["money"] = money
#     method = "POST"  #请求方法，全部大写
#     feature = "用户模块"  # allure报告中一级分类
#     story = '用户充值'  # allure报告中二级分类
#     uri = "/acc/recharge"  # 接口地址
#     headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cookie': 'csrftoken=1ihD7JgiyuUji8hF6tqGT1ac0yZto28faIkfE1W0Ij9sAHweIOFV56tlK2cl8HG1; ip=222.67.190.141; addr=%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%97%B5%E8%A1%8C%E5%8C%BA; Stu-Token=cc1ffa1f879c4abb8d42bef3f74d40a2; StuID=425'}
#     status_code = 200  # 响应状态码
#     expect = expect  # 预期结果
#     json_data='''{
#   "accountName": "${account_name}",
#   "changeMoney": "${money}"
# }'''
#
#     # --------------------分界线，下边的不要修改-----------------------------------------
#     # method,pub_data和url为必传字段
#     r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,json_data=json_data)


data = excel_tool.get_test_case("test_case/zuoyeuser/测试用例工作表.xls")

@pytest.mark.parametrize("account_name,money,expect",data[1],ids=data[0])
def test_recharge_recharge(pub_data,account_name,money,expect):
    pub_data["account_name"] = account_name
    pub_data["money"] = money


    method = "POST"  #请求方法，全部大写
    feature = "用户模块"  # allure报告中一级分类
    story = '用户充值'  # allure报告中二级分类

    uri = "/acc/recharge"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=user%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
               "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = expect  # 预期结果
    json_data='''{
  "accountName": "${account_name}",
  "changeMoney": "${money}"
}'''

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,json_data=json_data)
