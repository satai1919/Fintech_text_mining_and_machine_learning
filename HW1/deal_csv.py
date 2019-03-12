import crawler
import json
import time
filename = "ETF_List_Filtered.csv"
file = open(filename, "r")
#name = "output.csv"
#output = open(name, "w")
#
#
a = file.readline()
#a = a.split(",")
##print(a[-1])
#output.write(""+a[0]+", "+a[-1]+"")
##output.close()

# 34 etfs
for i in range(34):
    a = file.readline()
    #print(a)
    a = a.split(",")
    #print(type(a))
    
    # 15 pages in total
    session = crawler.login()
    for j in range(1,16):
        url = "https://ycharts.com/companies/"+a[0]+"/net_asset_value.json?endDate=12/31/2018&pageNum="+str(j)+"&startDate=12/31/2015"
        reqs = session.get(url)
        rj = json.loads(reqs.text)
        to_deal = rj["data_table_html"]
        time.sleep(1)
        print(type(to_deal))
    

#output.close()