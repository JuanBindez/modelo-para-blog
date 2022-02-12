from django.shortcuts import render

# Create your views here.
def hello_home(request):
    return render(request, 'index.html')

def hello_calc(request):
    return render(request, 'calc.html')