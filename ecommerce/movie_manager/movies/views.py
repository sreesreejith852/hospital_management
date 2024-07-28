from django.shortcuts import render
import psycopg2
from django.db import transaction
from . models import MovieInfo
from .forms import MovieForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def create(request):
    frm = MovieForm()
    print('aaaaaaaaaaaaaa')
    if request.POST:
        # id = request.POST.get('id')
        title = request.POST.get('title')
        year = request.POST.get('year')
        summary = request.POST.get('summary')
        movies = MovieInfo(
            title = title,
            year = year,
            summary = summary

        )
        movies.save()
     
    return render(request,'create.html')



def list(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})
    


def edit(request,pk):
    instance = MovieInfo.objects.get(pk=pk)
    title = request.POST.get('title')
    year = request.POST.get('year')
    summary = request.POST.get('summary')
    instance_edit =MovieInfo( {'title':title,'year':year,'summary':summary})
    print(instance_edit,"fffffffffffffff")
    print(title,"ggggggggg")
    print(instance,"hhhhhhhhhhhhhhhhhhh")
    print("nonameeeeeeeeeee")
    # if request.POST:
    #     title = request.POST.get('title')
    #     year = request.POST.get('year')
    #     summary = request.POST.get('summary')

    #     try:
    #         print("aaaaaaaaaaaaaaaaaaaaaaa")
    #         print("sreeeeeeeeeeeeeee")
    #         instance = MovieInfo.objects.get(pk=pk)
    #         instance.title = title
    #         print(instance,"ccccccccdd")
    #         instance.year = year
    #         instance.summary = summary
    #         instance.save()

    #         return HttpResponse("dhsdhdihoifdhid")
    #     except:
    #         print("dgygfudifhdfhdifohfidfob")
    #         return HttpResponse("sdhuidhsu")    
    return render(request,'create.html')  


def delete(request,pk):
    details = MovieInfo.objects.get(pk=pk)
    details.delete()
    movie_set=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})