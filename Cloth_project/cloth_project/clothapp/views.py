from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect,render

from clothapp.forms import ClothForm
from .models import Cloth

# Create your views here.

def index(request):
    cloth = Cloth.objects.all()
    return render(request,"index.html",{'result':cloth})

def details(request,cloth_id):
    cloth=Cloth.objects.get(id=cloth_id)
    return render(request,"detailed_view.html",{'res':cloth})

def add_cloth(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        img = request.FILES['img']
        des = request.POST.get('des')
        price = request.POST.get('price')

        cloth = Cloth(name=name,type=type,img=img,des=des,price=price)
        cloth.save()
    return render(request,"add_cloth.html")    

def update(request,id):
    cloth = Cloth.objects.get(id=id)
    form = ClothForm(request.POST or None,request.FILES,instance=cloth)
    if form.is_valid():
        form.save()
        return redirect('/')  
    return render(request,"edit.html",{'cloth':cloth,'form':form})     

def delete(request,id):
    if request.method == 'POST':
        cloth = Cloth.objects.get(id=id)
        cloth.delete()
        return redirect('/')
    return render(request,'delete.html')    
