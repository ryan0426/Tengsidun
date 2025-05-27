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

def dies_view(request):
    return render(request, 'categories/dies.html')

def wear_parts_view(request):
    return render(request, 'categories/wear_parts.html')

def heading_dies_view(request):
    return render(request, 'categories/heading_dies.html')

def bit_view(request):
    return render(request, 'categories/bit.html')

def rod_view(request):
    return render(request, 'categories/rod.html')

def cutting_tool_view(request):
    return render(request, 'categories/cutting_tool.html')

def cutter_view(request):
    return render(request, 'categories/cutter.html')

def ram_pot_view(request):
    return render(request, 'categories/ram_pot.html')

def non_magnetic_view(request):
    return render(request, 'categories/non_magnetic.html')

def precision_mold_view(request):
    return render(request, 'categories/precision_mold.html')

def other_tools_view(request):
    return render(request, 'categories/other_tools.html')

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

def testing_equip_view(request):
    return render(request, 'testing_equip.html')
