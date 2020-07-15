import pytest
from tools.api import request_tool
'''
自动生成 数字 20,80   #生成20到80之间的数字 例：56
自动生成 字符串 5 中文数字字母特殊字符 xuepl        #生成以xuepl开头加上长度2到5位包含中文数字字母特殊字符的字符串，例子：xuepl我1
自动生成 地址
自动生成 姓名
自动生成 手机号
自动生成 邮箱
自动生成 身份证号
'''
@pytest.mark.xgzhuangtai
@pytest.mark.xgmoney
def test_addProd(pub_data):
    pub_data["productCode"] = "自动生成 字符串 5 数字 whyan"
    method = "POST"  #请求方法，全部大写
    feature = "商品模块"  # allure报告中一级分类
    story = '创建商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/addProd"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Content-Type': 'application/json', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
               "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    json_data='''{
  "brand": "和路雪",
  "colors": [
    "应援色"
  ],
  "price": 99999,
  "productCode": "${productCode}",
  "productName": "可爱多",
  "sizes": [
    "敲击大"
  ],
  "type": "雪糕"
}'''
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据
    json_path = [{"skuCode": '$.data[0].skuCode'}]
    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(json_path=json_path,method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,json_data=json_data)

@pytest.mark.xgzhuangtai
def test_getSkuByProdCode(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '根据产品编码查商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
               "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': '${productCode}'}
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)
    pub_data["createTime"] = r.json()["data"][0]["createTime"]
    pub_data["updateTime"] = r.json()["data"][0]["updateTime"]


@pytest.mark.xgzhuangtai
def test_soldOut(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '产品改下架'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/soldOut"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
               "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'productCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

@pytest.mark.xgzhuangtai
def test_3(pub_data):


    method = "GET"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '根据下架条件查询商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSKU/1/3"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
               "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'endTime': '${updateTime}', 'startTime': '${createTime}', 'status': '2'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)


@pytest.mark.xgzhuangtai
def test_toPreSale(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '产品改预售'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/toPreSale"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
               "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'productCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)


@pytest.mark.xgzhuangtai
def test_4(pub_data):


    method = "GET"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '根据预售条件查询商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSKU/1/3"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
               "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'endTime': '${updateTime}', 'startTime': '${createTime}', 'status': '0'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)


@pytest.mark.xgmoney
def test_changePriceByProdCode(pub_data):
    method = "POST"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '根据产品编码批量修改商品价格'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/changePriceByProdCode"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Origin': 'http://192.168.1.151:8084', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
               "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    data={'price': '1000000', 'prodCode': '${productCode}'}

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,data=data)

@pytest.mark.xgmoney
def test_getSkuByProdCode1(pub_data):
    method = "GET"  #请求方法，全部大写
    feature = "产品模块"  # allure报告中一级分类
    story = '改金额后根据产品编码查商品'  # allure报告中二级分类
    title = "全字段正常流_1"  # allure报告中用例名字
    uri = "/product/getSkuByProdCode"  # 接口地址
    headers = {'Host': '192.168.1.151:8084', 'Connection': 'keep-alive', 'accept': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36', 'Referer': 'http://192.168.1.151:8084/swagger-ui.html?urls.primaryName=product%20apis', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9',
               "token": pub_data["token"]}
    status_code = 200  # 响应状态码
    expect = ""  # 预期结果
    params={'prodCode': '${productCode}'}
    # json path，参数类型为列表 根据jsonpath提取响应正文中的数据

    # --------------------分界线，下边的不要修改-----------------------------------------
    # method,pub_data和url为必传字段
    r = request_tool.request(method=method,url=uri,pub_data=pub_data,status_code=status_code,headers=headers,expect=expect,feature=feature,story=story,title=title,params=params)

