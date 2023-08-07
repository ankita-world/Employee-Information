from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def home(request):
    return render(request, 'enroll/index.html')


def showDetail(request):
    emp_data = Employee.objects.all()
    return render(request, 'enroll/showDetails.html', {'employee': emp_data})


def addEmployee(request):
    if request.method == 'POST':
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            eid = fm.cleaned_data['idNo']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            salary = fm.cleaned_data['salary']
            Employee(name=nm, idNo=eid, email=em, password=pw, salary=salary).save()
        return redirect('/show_detail/')

    else:
        fm = EmployeeForm()
    return render(request, 'enroll/addEmployee.html', {'form': fm})


# delete function

def delete_data(request, pk):
    pi = Employee.objects.get(id=pk)
    if request.method == 'POST':
        pi.delete()
        return redirect('/show_detail/')
    context = {"data": pi}
    return render(request, 'enroll/delete.html', context)


# update/edit function

def update_data(request, id):
    if request.method == 'POST':
        pi = Employee.objects.get(pk=id)
        fm = EmployeeForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/show_detail/')
    else:
        pi = Employee.objects.get(pk=id)
    fm = EmployeeForm(instance=pi)
    return render(request, 'enroll/update.html', {'form': fm})
