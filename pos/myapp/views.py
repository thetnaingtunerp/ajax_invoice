from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.shortcuts import (get_object_or_404,
                            render,
                            HttpResponseRedirect)


from .models import *
from .forms import *
# Create your views here.
def testfile(request):
	return render(request, 'test.html')



#Home Page Product View
def homepage(request):
    itm = item.objects.all()
    context = {'itm':itm}
    return render(request, 'homepage.html', context)

# Setup Menu 
def itemlist(request):
    itm = item.objects.all()
    form = ItemForm()
    context = {'itm':itm, 'form':form}
    return render(request, 'itemlist.html', context)

def itemcreate(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('myapp:itemlist')
    else:
        form = ItemForm()
    return render(request, 'itemlist.html', {'form': form})


def item_update(request):
    if request.method == 'POST':
        itmname = request.POST.get('itmname')
        slug = request.POST.get('slug')
        price = request.POST.get('price')
        iid = request.POST.get('iid')
        i = item.objects.filter(id=iid).update(item_name=itmname,slug=slug, price=price)
        return redirect('myapp:itemlist')
    else:
        return redirect('myapp:itemlist')




# after updating it will redirect to detail_View
def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}

    # add the dictionary during initialization
    context["data"] = item.objects.get(id = id)
        
    return render(request, "detail_view.html", context)

# update view for details
def update_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(item, id = id)

    # pass the object as instance in form
    form = ItemForm(request.POST, request.FILES or None, instance = obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)




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


def itm_add_invitm(request):
    itm = request.GET.get('itm')
    ipri = request.GET.get('ipri')
    iqty = request.GET.get('iqty')
    invid = request.GET.get('invid')
    itmid = request.GET.get('itmid')
    
    itmi = int(itmid) #item id
    r = int(ipri)
    qty = int(iqty)
    am = int(r * qty)
    itm_obj = item.objects.get(id=itmi)
    inv_obj = invoice.objects.get(id = int(invid))
    i = invitem(inv=inv_obj, item=itm, qty=qty, rate=r, amount=am)
    i.save()
    inv_obj.total += am
    inv_obj.save()

    itm_obj.stock -= qty
    itm_obj.save()

    return JsonResponse({'status':'success'})


def print_preview(request,id):
    context ={}
 
    # add the dictionary during initialization
    context["invitm"] = invitem.objects.filter(inv=id)
    context["data"] = invoice.objects.get(id = id)
    context["p"] = invoice_heading.objects.get(id=1)
     
    return render(request, "print_preview.html", context)
    

def delete_item_invoice(request):
    itmid = request.GET.get('itmid')
    invid = request.GET.get('invid')
    tid = int(itmid)
    iid = int(invid)

    inv_obj = invitem.objects.get(id=tid)
    amt = inv_obj.amount

    #update invoice total 
    inv = invoice.objects.get(id=iid)
    tt = inv.total
    iov_total = tt-amt
    inv.total = iov_total
    inv.save()

    inv_obj.delete()
    return JsonResponse({'status':'success'})




#Sale Item Report 

def sale_item_report(request):
    ivt = invitem.objects.all()
    context = {'ivt':ivt}
    return render(request, 'sale_item_report.html',context)

def sale_amount_report(request):
    inv = invoice.objects.all()
    context = {'inv': inv}
    return render(request, 'sale_amount_report.html', context)
