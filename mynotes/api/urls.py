from django.urls import path 
from .views import (
    NoteCreateView,
    getNotes,
    getNote,
    updateNote,
    deleteNote

)
urlpatterns = [
    path('notes/',getNotes,name='notes'),
    path('notes/create/',NoteCreateView.as_view()),
    path('notes/<int:pk>/update/',updateNote,name='update-note'),
    path('notes/<int:pk>/delete/',deleteNote,name='delete-note'),
    path('notes/<int:pk>/',getNote,name='note')

]
