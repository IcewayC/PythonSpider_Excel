# -*- coding: utf-8 -*-

import urllib2, re, xlwt


def get_content(): #urllib2获取html页面
    url = 'http://search.51job.com/list/070200,000000,0000,00,9,99,Python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    a = urllib2.urlopen(url)
    return a.read().decode('gbk')


def get(): #用正则获取内容
    html = get_content()
    reg = re.compile(r'class="t1 ">.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S)
    items = re.findall(reg, html)
    # print items[0][1]
    return items


def excel_write(items): #保存到excel文件中
    newTable = 'test.xls' #excel文件名
    wb = xlwt.Workbook(encoding='utf-8') #新建excel文件
    ws = wb.add_sheet('test1') #新建sheet工作表
    headData = ['招聘职位', '公司', '地址', '薪资', '日期'] #表头信息

    for colnum in range(0, 5):
        ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))

    index = 1 #行数

    for item in items:
        for i in range(0, 5):
            ws.write(index, i, item[i])
        index += 1

    wb.save(newTable) #保存完成


if __name__ == '__main__':
    excel_write(get())