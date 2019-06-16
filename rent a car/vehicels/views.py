from django.shortcuts import render
from vehicels.models import vehicel

# Create your views here.

def vehicels_index(request):
    vehicels = vehicel.objects.all()
    context = {
        'vehicels': vehicels
    }
    return render(request, 'vehicels_index.html', context)

def vehicel_detail(request, pk):
    vehicels = vehicel.objects.get(pk=pk)
    context = {
        'vehicel': vehicels
    }
    return render(request, 'vehicel_detail.html', context)