"""
URL configuration for client project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from produk.views import *

def satu(request):
    judul="Home"
    hal = {
        'titel':judul,
    }
    return render(request, "home.html", hal)


def dua(request):
    judul="About"
    hal = {
        'titel':judul,
    }
    return render(request, "about.html", hal)


def tiga(request):
    judul="Services"
    hal = {
        'titel':judul,
    }
    return render(request, "services.html", hal)


def empat(request):
    judul="Price"
    hal = {
        'titel':judul,
    }
    return render(request, "price.html", hal)


def lima(request):
    judul="Contact"
    hal = {
        'titel':judul,
    }
    return render(request, "contact.html", hal)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", satu),
    path("about/", dua),
    path("services/", tiga),
    path("price/", empat),
    path("contact/", lima),
    path("addbrg/", tambah_barang),
    path('Vbrg/', Barang_View),
    path('ubah/<int:id_barang>', ubah_brg,name='ubah_brg'),
    path('hapus/<int:id_barang>', hapus_brg,name='hapus_brg'),
    path("addjenis/", tambah_jenis),
    path('Jbrg/', Jenis_View),
    path('Ubah/<int:id_jenis>', ubah_jenis,name='ubah_jenis'),
    path('Hapus/<int:id_jenis>', hapus_jenis,name='hapus_jenis'),
]
