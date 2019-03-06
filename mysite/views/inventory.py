from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponseRedirect
from mysite.models.mysqlOperate import MysqlOperate
from django.views.decorators.csrf import csrf_exempt


mysqlOperate = MysqlOperate()


def getInventoryList():
    """从数据库中取出列表数据，并将tuple转化成字典"""
    data = mysqlOperate.db_select("SELECT * FROM inventory.inventory")
    inventory_list = []
    for line in data:
        dict = {}
        dict['id'] = line[0]
        dict['goods'] = line[1]
        dict['type'] = line[2]
        dict['num'] = line[3]
        dict['comment'] = line[4]
        inventory_list.append(dict)
    return inventory_list


#库存管理页面：data库存管理表格数据，type添加商品时分类项的下啦列表数据
@login_required
def inventory(request):
    type = mysqlOperate.db_select("SELECT type FROM inventory.type")
    data = getInventoryList()
    return render(request, 'inventory.html', {"data":data, "type":type})


#添加商品
@csrf_exempt
def add(request):
    if request.method == "POST":
        goods = request.POST.get('goods')
        type = request.POST.get('type')
        comment = request.POST.get('comment')
        mysqlOperate.db_execute("INSERT INTO inventory.inventory(goods, type, num, comment) VALUES ('"+goods+"','"+type+"','0','"+comment+"')")
    return HttpResponseRedirect("inventory")


#库存管理页面-删除分类
@csrf_exempt
def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        mysqlOperate.db_execute("DELETE  FROM inventory.inventory  WHERE id='"+ id +"'")
        data = getInventoryList()
        return render(request, 'inventoryTable.html', {'data': data})
