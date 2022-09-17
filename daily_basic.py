#导入扩展
import tushare as ts
import time
import requests

proxies = { "http": None, "https": None}
requests.get("http://ff2.pw", proxies=proxies)

# 初始化token
# #自己的api
# pro = ts.pro_api('26b0dc39a8d4ff866a455c30afcb7d54422bac12e908908387965d75')

# 租的api
pro = ts.pro_api('ff528ab0b57c301d1b924a00578b49e18a8ebe63be8eebadf5ef3052')

root = "/Users/colourful/Desktop/Try/stock_predict_baseline/daily_basic/"

#查询当前所有正常上市交易的股票列表
stock_list = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
stock_list.to_csv(root + "stock_online.csv", index=False)


# print(data['ts_code'][0])
# print(len(data['ts_code']))

#每日指标
for i in range(len(stock_list['ts_code'])):
    if i % 50 == 0:
            time.sleep(60)
    else:
        temp = str(stock_list['ts_code'][i])
        df_00 = pro.daily_basic(ts_code = temp, start_date='19900101', end_date='20000101')
        df_10 = pro.daily_basic(ts_code = temp, start_date='20000101', end_date='20100101')
        df_20 = pro.daily_basic(ts_code = temp, start_date='20100101', end_date='20200101')
        df_22 = pro.daily_basic(ts_code = temp, start_date='20200101', end_date='20220908')
        df = df_22.append(df_20.append(df_10.append(df_00)))
        df.to_csv(root + temp + '.csv', index=False)