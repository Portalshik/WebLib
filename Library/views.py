from django.shortcuts import render

from .models import Books


def index(request):
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
    return render(request, 'index.html', {'books': books})
