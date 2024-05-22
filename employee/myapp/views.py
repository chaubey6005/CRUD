from django.shortcuts import render, redirect
from .forms import EmployeeRegistration
from .models import User

# This function is used to add and show data
def add_show(request):
    if request.method == 'POST':
        fm = EmployeeRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            mo = fm.cleaned_data['mobile']
            ps = fm.cleaned_data['password']
            reg = User(name=nm, email=em, mobile=mo, password=ps)
            reg.save()
            fm = EmployeeRegistration()  #used to reset the form after successfull save 
    else:
        fm = EmployeeRegistration()
        #used to show the saved data
    emp = User.objects.all()
    return render(request,'addandshow.html',{'form':fm,'empl':emp, })
#This function will update/edit data
def update_data(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('add_show')
    else:
        pi = User.objects.get(pk=id)
        fm = EmployeeRegistration(instance=pi)
    return render(request, 'update.html',{'form':fm})

#This function is used to delete function
def delete_data(request,pid):
    pi=User.objects.filter(pk=pid)
    pi.delete()
    return redirect('add_show')