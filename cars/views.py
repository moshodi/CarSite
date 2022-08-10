from signal import pthread_kill
from django.shortcuts import render,redirect
from django.urls import reverse
from . import models


def list(request):
    cars = models.Car.objects.all()
    context = {'cars': cars}
    return render(request,'cars/list.html',context)

def add(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand,year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def delete(request):
    if request.POST:
        id = request.POST['pk']
        try:
            models.Car.objects.get(id=id).delete()
            return redirect(reverse('cars:list'))
        except:
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/delete.html')