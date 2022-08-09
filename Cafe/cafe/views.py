from django.shortcuts import redirect, render
from.models import Menyu
from.forms import MenyuForm
# Create your views here.

def index(request):
    cafe=Menyu.objects.all()
    context={
    'cafe': cafe
    }
    return render (request, 'index.html', context)

def menyu(request):
    menyuies=Menyu.objects.all()
    context={
    'menyuies': menyuies
    }
    return render (request, 'menyu.html', context)


def menyu_detail(request,pk):
    menyu=Menyu.objects.get(pk=pk)
    context={
    "menyu":menyu
    }
    return render(request,'menyu_detail.html',context)



def about(request):
    about=Menyu.objects.all()
    context={
    'about': about
    }

    return render(request,'about.html', context)
    
def menyu_create(request):
    form=MenyuForm()
    if request.method=='POST':
        form=MenyuForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menyu')

    context={
    'form':form
    }
    return render(request,'create_menyu.html',context)
     

def menyu_update(request,pk):
    menyu=Menyu.objects.get(pk=pk)
    forms=MenyuForm(instance=menyu)
    
    if request.method=='POST':
        forms=MenyuForm(request.POST, instance=menyu)
        if forms.is_valid():
            forms.save()
            return redirect('menyu')
    context={
        'forms':forms
    }
    return render(request,'update_menyu.html',context)


def menyu_delete(request,pk):
    menyu=Menyu.objects.get(pk=pk)
    menyu.delete()
    return redirect('menyu')


def sector(request):
    sector=Menyu.objects.all()
    context={
    'sector': sector
    }

    return render(request,'sector.html', context)


def connect(request):
    connect=Menyu.objects.all()
    context={
    'connect': connect
    }

    return render(request,'connect.html', context)