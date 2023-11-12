from django.shortcuts import render, redirect
from produk.forms import FormBarang, JenisBarang
from produk.models import Barang, Jenis
from django.contrib import messages
# Create your views here.

def tambah_barang(request):
    if request.POST:
        form=FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form=FormBarang()
            konteks={
                'form':form,
            }
            return render(request,'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        konteks={
            'form':form,
        }
        return render(request,'tambah_barang.html',konteks)

def ubah_brg(request, id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks={
            'form':form,
            'barangs':barangs
        }
    return render(request,'ubah_brg.html',konteks)

def Barang_View(request):
    barangs=Barang.objects.all()
    konteks={
        'barangs':barangs,
    }

    return render(request,'tampil_brg.html',konteks)

def hapus_brg(request,id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    messages.success(request,"Data Terhapus")

    return redirect('/Vbrg/')


# Tabel Jenis
def tambah_jenis(request):
    if request.POST:
        form=JenisBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form=JenisBarang()
            konteks={
                'form':form,
            }
            return render(request,'tambah_jenis.html',konteks)
    else:
        form=JenisBarang()
        konteks={
            'form':form,
        }
        return render(request,'tambah_jenis.html',konteks)

def ubah_jenis(request, id_jenis):
    jeniss=Jenis.objects.get(id=id_jenis)
    if request.POST:
        form=JenisBarang(request.POST,instance=jeniss)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Diubah")
            return redirect('ubah_jenis',id_jenis=id_jenis)
    else:
        form=JenisBarang(instance=jeniss)
        konteks={
            'form':form,
            'jeniss':jeniss
        }
    return render(request,'ubah_jenis.html',konteks)

def Jenis_View(request):
    jeniss=Jenis.objects.all()
    konteks={
        'jeniss':jeniss,
    }

    return render(request,'tampil_jenis.html',konteks)

def hapus_jenis(request,id_jenis):
    jeniss=Jenis.objects.filter(id=id_jenis)
    jeniss.delete()
    messages.success(request,"Data Terhapus")

    return redirect('/Jbrg/') 