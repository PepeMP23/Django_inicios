from django.http import HttpResponse
from django.template import loader
from .models import Student

def students(request):
    mystudents = Student.objects.all().values()
    template = loader.get_template('all_students.html')
    context = {
        'mystudent': mystudents,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mystudent = Student.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mystudent': mystudent,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
   
def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))