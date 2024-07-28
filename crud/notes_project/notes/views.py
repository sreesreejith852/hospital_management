from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import render

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    def get_queryset(self):
        return Note.objects.all()
    def list(self,request,*args,**kwargs):
        notes =self.get_queryset()
        context = {'notes':notes}
        return render(request,'api.html',context)
    

class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer



    
