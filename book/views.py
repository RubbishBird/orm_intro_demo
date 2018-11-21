from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

def index(request):
    #增加数据
    # book = Book(name='红楼梦',author='曹雪芹',price='150')
    # book.save()
    # return HttpResponse("图书插入成功")

    #查询数据
    # book = Book.objects.get(pk=1)
    # book = Book.objects.filter(name='三国演义').first()
    # print(book)
    # return HttpResponse("图书插入成功")

    #删除数据
    # book  = Book.objects.get(pk=1)
    # book.delete()

    #修改数据
    book = Book.objects.get(pk=2)
    book.price = '300'
    book.save()
    return HttpResponse("图书插入成功")