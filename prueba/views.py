from django.shortcuts import render, redirect
from .models import Reporter, Article
from .forms import FormArticle
from django.contrib import messages
# Create your views here.

def inicio(request):
    reportes = Reporter.objects.all()
    return render(request,'index.html', {"reportes": reportes})

def nuevo_reporte(request):
    
    if request.method == "POST":
        R = Reporter(full_name = request.POST.get('reporte'))
        R.save()

    return render(request, 'form_reporte.html')

def nuevo_articulo(request):
    if request.method == "POST":
        form = FormArticle(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Articulo agregado con éxito')
                
            except Exception as e:
                print(e)
        return redirect('inicio')
            
            
    else:
        form = FormArticle()
        
    return render(request, 'form_articulo.html', {'form': form})

def listar_Articulos(request):
    articulos = Article.objects.all()
    return render(request, 'vista_articulos.html', {'articulos': articulos})