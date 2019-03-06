"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite.views import index, type, inventory, inbound, warning, outbound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index.index),
    path('login',index.login),
    path('type',type.type),#分类管理页面
    path('type_add', type.add),#添加分类
    path('type_delete', type.delete), #删除分类
    path('inventory', inventory.inventory),  # 库存管理页面
    path('inventory_add', inventory.add),  # 添加商品信息
    path('inventory_delete', inventory.delete), #删除商品信息
    path('inbound',inbound.inbound),#入库管理页面
    path('inbound_add',inbound.add),#商品入库
    path('inbound_delete',inbound.delete),#删除商品入库信息
    path('warning', warning.warning),#预警信息详情
    path('warning_add',warning.add),#添加预警信息
    path('warning_delete',warning.delete),#删除预警信息
    path('outbound',outbound.outbound),#出库页面
    path('outbound_add',outbound.add),#商品出库
    path('outbound_delete',outbound.delete),#删除出库信息
]
