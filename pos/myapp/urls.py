from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
	path('test/', views.testfile, name='testfile'),
	path('', views.homepage, name='homepage'),
	#sale
	path('inv_list/', views.inv_list, name='inv_list'),
	path('detail_inv/<int:id>/', views.detail_inv, name='detail_inv'),
	path('create_invoice/', views.create_invoice, name='create_invoice'),
	path('itm_add_invitm/', views.itm_add_invitm, name='itm_add_invitm'),
	path('print_preview/<int:id>/', views.print_preview, name='print_preview'),
	path('delete_item_invoice/', views.delete_item_invoice, name='delete_item_invoice'),

	# setup menu
	path('itemlist/', views.itemlist, name='itemlist'),
	path('itemcreate/', views.itemcreate, name='itemcreate'),
	path('item_update/', views.item_update, name='item_update'),
	# path('/update_view/<int:id>/', views.update_view, name='update_view'),

	#reports
	path('sale_item_report/', views.sale_item_report, name='sale_item_report'),
]