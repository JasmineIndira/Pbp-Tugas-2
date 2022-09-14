# TODO: Create your views here.
from django.shortcuts import render
from katalog.models import CatalogItem

# Views
def show_katalog(request):
    data_item_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_item_katalog,
    'nama': 'Jasmine Indira Wibowo',
    'id': '2106650374'
    }
    return render(request, "katalog.html", context)