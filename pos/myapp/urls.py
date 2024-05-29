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
	path('sale_amount_report/', views.sale_amount_report, name='sale_amount_report'),

	#Purchase
	path('supplier_info/', views.supplier_info, name='supplier_info'),
	path('suppliercreate/', views.suppliercreate, name='suppliercreate'),
	path('update_supplier/', views.update_supplier, name='update_supplier'),
	path('supplier_to_vouc/', views.supplier_to_vouc, name='supplier_to_vouc'),
	path('purchase_invoice_view/', views.purchase_invoice_view, name='purchase_invoice_view'),
	path('add_purchase_voc/<int:id>/', views.add_purchase_voc, name='add_purchase_voc'),
	path('save_itm_purvoc/', views.save_itm_purvoc, name='save_itm_purvoc'),
]