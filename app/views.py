from django.shortcuts import render, HttpResponseRedirect
from .models import student_info
from .forms import data

# Create your views here.
def add_show(request):
    if request.method=='POST':
        a = data(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['name']
            em = a.cleaned_data['email']
            co = a.cleaned_data['contact']


            m = student_info(name=nm,
                             email=em,
                             contact=co)
            m.save()
    else:
        a = data()
    stu = student_info.objects.all()
    return render(request, 'app/add_show.html', {'a' : a, 'b':stu})


#update
def update_data(request, id):
    if request.method == 'POST':
        u = student_info.objects.get(pk=id)
        d = data(request.POST, instance=u)
        if d.is_valid():
            d.save()
            d = data()
        
    else:
        u = student_info.objects.get(pk=id)
        d = data(instance=u)
    return render(request, 'app/update.html', {'id':id, 'form':d})


# delete data

def delete(request, id):
    if request.method=='POST':
        d = student_info.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/')

