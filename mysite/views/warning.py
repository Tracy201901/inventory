from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponseRedirect
from mysite.models.mysqlOperate import MysqlOperate
from django.views.decorators.csrf import csrf_exempt


mysqlOperate = MysqlOperate()


def getWarningList():
    """从数据库中取出列表数据，并将tuple转化成字典"""
    data = mysqlOperate.db_select("SELECT * FROM inventory.warning")
    warning_list = []
    for line in data:
        dict = {}
        dict['id'] = line[0]
        dict['goods'] = line[1]
        dict['warning_num'] = line[2]
        dict['comment'] = line[3]
        warning_list.append(dict)
    return warning_list


#库存管理页面：data库存管理表格数据，type添加商品时分类项的下啦列表数据
@login_required
def warning(request):
    goods = mysqlOperate.db_select("SELECT goods FROM inventory.inventory")
    print('商品',goods)
    data = getWarningList()
    return render(request, 'warning.html', {"data":data, "goods":goods})


#添加商品
@csrf_exempt
def add(request):
    if request.method == "POST":
        print(request.POST)
        goods = request.POST.get('goods')
        warning_num = request.POST.get('warning_num')
        comment = request.POST.get('comment')
        mysqlOperate.db_execute("INSERT INTO inventory.warning(goods, warning_num, comment) VALUES ('"+goods+"','"+warning_num+"','"+comment+"')")
    return HttpResponseRedirect("warning")


#库存管理页面-删除分类
@csrf_exempt
def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        mysqlOperate.db_execute("DELETE  FROM inventory.warning  WHERE id='"+ id +"'")
        data = getWarningList()
        return render(request, 'warningTable.html', {'data': data})
