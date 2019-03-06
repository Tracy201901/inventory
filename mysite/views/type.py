from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, HttpResponseRedirect
from mysite.models.mysqlOperate import MysqlOperate
from django.views.decorators.csrf import csrf_exempt



mysqlOperate = MysqlOperate()


def getTypeList():
    """从数据库中取出分类列表数据，并将tuple转化成字典"""
    data = mysqlOperate.db_select("SELECT * FROM inventory.type")
    type_list = []
    for line in data:
        dict = {}
        dict['id'] = line[0]
        dict['type'] = line[1]
        dict['comment'] = line[2]
        type_list.append(dict)
    return type_list


#分类管理页面
@login_required
def type(request):
    type_list = getTypeList()
    return render(request, "type.html", {'data': type_list})


#分类管理页面-添加分类
@csrf_exempt
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        sql = "INSERT INTO inventory.type(type, comment) VALUES ('" + name +"','"+ comment +"')"
        mysqlOperate.db_execute(sql)
    return HttpResponseRedirect("type")


#分类管理页面-删除分类
@csrf_exempt
def delete(request):
    if request.method == 'POST':
        type_id = request.POST.get('id')
        mysqlOperate.db_execute("DELETE  FROM inventory.type  WHERE id='"+ type_id +"'")
        type_list = getTypeList()
        print(type_list)
        return render(request, 'typeList.html', {'data': type_list})
