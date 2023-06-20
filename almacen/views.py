from django.shortcuts import render
from .models import Almacen
from .forms import AlmacenForm

# Create your views here.
def reg_tienda (request):
    if request.method == 'POST':
        form = AlmacenForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    else:
        form = AlmacenForm()
        return render(request,'registro_tienda.html',{'form':form})