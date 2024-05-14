from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
# Create your views here.
def testfile(request):
	return render(request, 'test.html')


# Setup Menu 
def itemlist(request):
    itm = item.objects.all()
    context = {'itm':itm}
    return render(request, 'itemlist.html', context)






def inv_list(request):
	inv = invoice.objects.all().order_by('-id')
	context = {'inv':inv}
	return render(request, 'inv_list.html', context)

def detail_inv(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["invitm"] = invitem.objects.filter(inv=id)
    context["data"] = invoice.objects.get(id = id)
    context["itm"] = item.objects.all()
         
    return render(request, "detail_inv.html", context)




def create_invoice(request):
    cu = request.GET.get('cu')
    inv_obj = invoice.objects.create(customer=cu, total=0)
    return JsonResponse({'status':'success'})

# {itm:itm, ipri:ipri, iqty:iqty},
def itm_add_invitm(request):
    itm = request.GET.get('itm')
    ipri = request.GET.get('ipri')
    iqty = request.GET.get('iqty')
    invid = request.GET.get('invid')
    r = int(ipri)
    qty = int(iqty)
    am = int(r * qty)
    # print(am)
    inv_obj = invoice.objects.get(id = int(invid))
    i = invitem(inv=inv_obj, item=itm, qty=qty, rate=r, amount=am)
    i.save()
    inv_obj.total += am
    inv_obj.save()
    return JsonResponse({'status':'success'})


def print_preview(request,id):
    context ={}
 
    # add the dictionary during initialization
    context["invitm"] = invitem.objects.filter(inv=id)
    context["data"] = invoice.objects.get(id = id)
    context["p"] = invoice_heading.objects.get(id=1)
     
    return render(request, "print_preview.html", context)
    




