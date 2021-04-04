from django.urls import path

from .views import NewDocumentView, DocumentView, delete_document

urlpatterns = [
    path('', NewDocumentView.as_view(), name='new_document'),
    path('<int:doc_id>/', DocumentView.as_view(), name='document'),
    path('<int:doc_id>/delete', delete_document, name='delete_document')
]
