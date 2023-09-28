from django.shortcuts import render 
from django.http import HttpResponse 
from django.template import loader
from .models import Member
from django.db.models import Q

def members(request): 
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    #mydata = Member.objects.all()
    #mydata = Member.objects.all().values()
    #mydata = Member.objects.values_list('firstname')
    #mydata = Member.objects.filter(firstname='Jose').values()
    #mydata = Member.objects.filter(lastname='Refsnes', id=2).values()
    #mydata = Member.objects.filter(firstname='Jose').values() | Member.objects.filter(firstname='Tobias').values()
    #mydata = Member.objects.filter(Q(firstname='Jose') | Q(firstname='Tobias')).values()
    #mydata = Member.objects.all().values().filter(firstname__startswith='J')
    #mydata = Member.objects.filter(firstname__startswith='L').values()
    #mydata = Member.objects.all().order_by('firstname').values()
    #mydata = Member.objects.all().order_by('-firstname').values()
    mydata = Member.objects.all().order_by('lastname', '-id').values()

    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))
