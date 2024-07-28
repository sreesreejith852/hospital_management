# from django.urls import path
# from .views import NoteListCreateView

# urlpatterns = [
#     path('api/v1/notes/', NoteListCreateView, name='note-list-create'),
#     # path('api/v1/notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
# ]

from django.urls import path
from notes.views import NoteListCreateView, NoteRetrieveUpdateDestroyView

urlpatterns = [
    path('notes/v1', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/v1/notes/<int:pk>',NoteRetrieveUpdateDestroyView.as_view(), name='note-retrieve-update-destroy'),
    path('', NoteListCreateView.as_view(), name='note-list-create'),
]