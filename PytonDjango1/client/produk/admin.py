from django.contrib import admin

# Register your models here.
from.models import Barang, Jenis

class kolomBarang(admin.ModelAdmin):
    list_display=['kodebrg', 'nama', 'stok', 'harga', 'link_gbr', 'jenis_id']
    search_field=['kodebrg', 'nama']
    list_filter=('jenis_id',)
    list_per_page=3

admin.site.register(Barang, kolomBarang)
admin.site.register(Jenis)