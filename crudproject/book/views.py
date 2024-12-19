from django.shortcuts import render,redirect,HttpResponseRedirect
from . models import User
from . forms import StudentRegisteration
# Create your views here.

def add_show(request):
    if request.method=='POST':
        f=StudentRegisteration(request.POST)
        if f.is_valid():
            nm=f.cleaned_data['Name']
            em=f.cleaned_data['Email']
            passw=f.cleaned_data['Password']
            reg=User(Name=nm,Email=em,Password=passw)
            reg.save()
        return redirect('/')
    else:
        f=StudentRegisteration()
        stu=User.objects.all()
        return render(request,'book/addandshow.html',{'form':f,'list':stu})
    
def delete_logic(request,id):
    pi=User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')

def update_logic(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegisteration(request.POST,instance=pi)
        fm.save()
        return redirect('/')
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegisteration(instance=pi)
        return render(request,'book/updatestudent.html',{'form':fm})
 
    
