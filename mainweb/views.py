from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def tech_info(request):
    return render(request, 'tech_info.html')

def news(request):
    return render(request, 'news.html')

def testing_equip_view(request):
    return render(request, 'testing_equip.html')

def precision_view(request):
    return render(request, 'categories/precision.html')

def forging_view(request):
    return render(request, 'categories/forging.html')

def cutting_view(request):
    return render(request, 'categories/cutting.html')

def mining_view(request):
    return render(request, 'categories/mining.html')

def rollers_view(request):
    return render(request, 'categories/rollers.html')
