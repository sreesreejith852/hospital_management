from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello(request):
    movie_data={
        'movies':[
        { 
        'title':'god father',
        'year':'1990',
        'summary':'movieeeeeeeee',
        'sucess':False
        },
        {
        'title':'ravana prabhu',
        'year':'1998',
        'summary':'movieeeeeeeee',
        'sucess':False
        },
        {
        'title':'vettam',
        'year':'1998',
        'summary':'movieeeeeeeee',
        'sucess':False
        },
          {
        'title':'narasimham',
        'year':'1998',
        'summary':'movieeeeeeeee',
        'sucess':False
        },
       
       
        ]

    }
    return render(request,'base.html',movie_data)
