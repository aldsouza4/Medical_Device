from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

# class index_view(TemplateView):
#     template_name = 'base.html'

def index_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(name, email, message)

    return render(request, 'index.html')


def solution_view(request):
    return render(request, 'solutions.html')


def technology_view(request):
    return render(request, 'technology.html')


def customer_view(request):
    return render(request, 'customer.html')


def company_view(request):
    return render(request, 'company.html')


def login_view(request):
    return render(request, 'login.html')

