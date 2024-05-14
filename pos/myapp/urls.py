from django.urls import path
from .views import *
from . import views
app_name = 'myapp'
urlpatterns = [
	path('', views.testfile, name='testfile'),
	#sale
	path('inv_list/', views.inv_list, name='inv_list'),
	path('detail_inv/<int:id>/', views.detail_inv, name='detail_inv'),
	path('create_invoice/', views.create_invoice, name='create_invoice'),
	path('itm_add_invitm/', views.itm_add_invitm, name='itm_add_invitm'),
	path('print_preview/<int:id>/', views.print_preview, name='print_preview'),

	# setup menu
	path('itemlist/', views.itemlist, name='itemlist'),

	#reports
]