from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django import views
from django.http.request import HttpRequest
from django.urls import reverse_lazy

from .models import Document


class NewDocumentView(views.View):
    def get(self, request: HttpRequest):
        return render(request, 'document.html', {
            'documents': Document.objects.filter(owner=request.user),
        })

    def post(self, request: HttpRequest):
        owner = request.user
        title = request.POST.get('title')
        content = request.POST.get('content')
        document = Document.objects.create(owner=owner, title=title, content=content)

        return redirect(reverse_lazy('document', kwargs={'doc_id':document.id}))


class DocumentView(views.View):
    def get(self, request: HttpRequest, doc_id: int):
        try:
            document = Document.objects.get(pk=doc_id)
        except ObjectDoesNotExist:
            document = None

        return render(request, 'document.html', {
            'documents': Document.objects.filter(owner=request.user),
            'document': document,
        })

    def post(self, request: HttpRequest, doc_id: int):
        title = request.POST.get('title')
        content = request.POST.get('content')

        document = Document.objects.get(pk=doc_id)
        document.title = title
        document.content = content
        document.save()

        return redirect(reverse_lazy('document', kwargs={'doc_id':document.id}))


def delete_document(request: HttpRequest, doc_id: int):
    try:
        Document.objects.get(pk=doc_id).delete()
    except ObjectDoesNotExist:
        pass  # deleting a document that doesn't exist is fine? maybe?

    return redirect(reverse_lazy('new_document'))
