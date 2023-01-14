from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response
from rest_framework import status , generics

from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
# Create your views here.


class NoteCreateView(generics.CreateAPIView):
    queryset = Note
    serializer_class = NoteSerializer

@api_view()
def getNotes(request):
    notes =  Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data,status.HTTP_200_OK)


@api_view()
def getNote(request,pk):
    note =  get_object_or_404(Note,pk=pk)
    serializer = NoteSerializer(note,many=False)
    return Response(serializer.data,status.HTTP_200_OK)
    


@api_view(['PUT'])
def updateNote(request,pk):
    data = request.data 
    note = get_object_or_404(Note,id=pk)
    serializer = NoteSerializer(instance=note,data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save() 
    return Response(serializer.data,status.HTTP_202_ACCEPTED)


@api_view(['DELETE'])
def deleteNote(request,pk):
    note = get_object_or_404(Note,id=pk)
    serializer = NoteSerializer(note)
    print(serializer)
    note.delete()
    return Response(serializer.data,status.HTTP_204_NO_CONTENT)


