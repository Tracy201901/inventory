from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponseRedirect
from mysite.models.mysqlOperate import MysqlOperate
from django.views.decorators.csrf import csrf_exempt
from mysite.views import timeStamp
import time

mysqlOperate = MysqlOperate()


def getInboundList():
    """从数据库中取出列表数据，并将tuple转化成字典"""
    data = mysqlOperate.db_select("SELECT * FROM inventory.inbound")
    inbound_list = []
    for line in data:
        print(data)
        dict = {}
        dict['id'] = line[0]
        dict['goods'] = line[1]
        dict['inbound_num'] = line[2]
        t = line[3]
        dict['inbound_date'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))
        dict['comment'] = line[4]
        inbound_list.append(dict)
    print(inbound_list)
    return inbound_list


#库存管理页面：data库存管理表格数据，type添加商品时分类项的下啦列表数据
@login_required
def inbound(request):
    goods = mysqlOperate.db_select("SELECT goods FROM inventory.inventory")
    data = getInboundList()
    return render(request, 'inbound.html', {"data":data, "goods":goods})


#添加商品
@csrf_exempt
def add(request):
    if request.method == "POST":
        goods = request.POST.get('goods')
        inbound_num = request.POST.get('inbound_num')
        inbound_date = str(timeStamp.getTimeStamp())
        comment = request.POST.get('comment')
        mysqlOperate.db_execute("INSERT INTO inventory.inbound(goods, inbound_num, inbound_date, comment) VALUES ('"+goods+"','"+inbound_num+"','"+inbound_date+"','"+comment+"')")

    return HttpResponseRedirect("inbound")


#库存管理页面-删除分类
@csrf_exempt
def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        mysqlOperate.db_execute("DELETE  FROM inventory.inbound  WHERE id='"+ id +"'")
        data = getInboundList()
        return render(request, 'inboundTable.html', {'data': data})
