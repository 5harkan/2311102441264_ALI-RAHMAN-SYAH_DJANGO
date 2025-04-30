from idlelib.rpc import request_queue
from importlib.resources import contents

from django.shortcuts import render, redirect
from berita.models import Kategori, Artikel
# Create your views here.
def dashboard(request):
    template_name = "dashboard/index.html"
    context = {
        'title' : "halaman dashboard"
    }
    return render(request, template_name, context)

def kategori_list(request):
    template_name = "dashboard/content/kategori_list.html"
    kategori = Kategori.objects.all()
    print(kategori)
    context = {
        'title'     : "halaman kategori",
        'kategori'  : kategori
    }
    return render(request, template_name, context)

def kategori_add(request):
    templates_name = "dashboard/content/kategori_add.html"
    if request.method == "POST":
        nama_input = request.POST.get('nama_kategori')
        Kategori.objects.create(
            nama = nama_input
        )
        return redirect(kategori_list)
    context = {
        'title' : 'tambah kategori',
    }
    return render(request, templates_name, context)

def kategori_update(request, id_kategori):
    templates_name = "dashboard/content/kategori_update.html"
    kategori = Kategori.objects.get(id=id_kategori)
    if request.method == "POST":
        nama_input = request.POST.get('nama_kategori')
        kategori.nama = nama_input
        kategori.save()
        return redirect(kategori_list)
    context = {
        'title'     : 'Edit Kategori',
        'kategori'  : kategori
    }
    return render(request, templates_name, context)

def kategori_delete(request, id_kategori):
    Kategori.objects.get(id=id_kategori).delete()
    return redirect(kategori_list)