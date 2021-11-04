from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

# class index_view(TemplateView):
#     template_name = 'index.html'

def index_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(name, email, message)


    return render(request, 'index.html')
