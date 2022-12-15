from django.shortcuts import render

from .models import Books, Categories, Authors
from .forms import SearchForm


def index(request):
    if request.GET:
        return render(request, 'index.html', {'search': search(request)})
    else:
        data = Books.objects.all()
        books = []

        for i in data:
            tags = []
            if i.tag.count() >= 2:
                for j in range(1, i.tag.count() + 1):
                    tags.append(i.tag.get(id=j))
            else:
                tags.append(i.tag.get())

            authors = []
            if i.author.count() >= 2:
                for j in range(1, i.author.count() + 1):
                    authors.append(i.author.get(id=j))
            else:
                authors.append(i.author.get())

            books.append({
                'name': str(i.book_name),
                'authors': authors,
                'category': str(i.category),
                'reissue': str(i.reissue_num),
                'pub_date': str(i.publication_date),
                'created_at': str(i.created_at),
                'tags': tags
            })
        return render(request, 'index.html', {'books': books, 'form': SearchForm})


def search(request):
    req_search = request.GET
    match req_search['filter']:
        case 'category':
            return Books.objects.get(category=Categories.objects.get(category=req_search['search']))
        case 'name':
            return Books.objects.get(book_name=req_search['search'])
        case 'author':
            return Books.objects.get(author=Authors.objects.get(author=req_search['search']))
