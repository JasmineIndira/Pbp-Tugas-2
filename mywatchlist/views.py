from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    movies_watched = MyWatchList.objects.filter(watched = True).count()
    movies_unwatched = MyWatchList.objects.filter(watched = False).count()
    movie_result = ''

    if (movies_watched >= movies_unwatched):
        movie_result = "Selamat, kamu sudah banyak menonton!"
    else:
        movie_result = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_movie': MyWatchList.objects.all(),
        'nama': "Jasmine Indira Wibowo",
        'movie_result': movie_result,
    }
    return render(request, "MyWatchList.html", context)

def show_xml(request):
    mywatchlist_data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", mywatchlist_data), content_type="application/xml")

def show_xml_by_id(request, id):
    mywatchlist_data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", mywatchlist_data), content_type="application/xml")

def show_json(request):
    mywatchlist_data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", mywatchlist_data), content_type="application/json")

def show_json_by_id(request, id):
    mywatchlist_data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", mywatchlist_data), content_type="application/json")