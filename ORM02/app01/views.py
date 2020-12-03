from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01.models import Book,Publish,AuthorDetail,Author


def add_new(request):

    # 单表添加
    # Publish.objects.create(name="橘子出版社",addr="北京",email="234@qq.com")

    # 一对多添加方式1
    # book = Book.objects.create(title="三国",price=122,pub_date="2012-12-12",publisher_id=2)
    # 一对多添加方式2
    # pub_obj = Publish.objects.get(name="苹果出版社")
    # Book.objects.create(title="红楼梦", price=122, pub_date="2012-12-12",publisher=pub_obj)

    # 多对多添加记录
    #待 实现###########################################################

    book = Book.objects.get(pk=1) # book.authors: 第三张表的操作管理
    # 绑定多对多关系
    # alex = Author.objects.get(pk=1)
    # egon = Author.objects.get(pk=2)
    # book.authors.add(alex,egon)
    # book.authors.add(1,2)
    book.authors.add(*[1,2])
    # 多对多的解绑
    # book.authors.remove(1,2)
    # 多对多关系清除
    #book.authors.clear()

    # 多对多的重置
    book.authors.set([1,])

    return HttpResponse("添加成功!")


def publish_func(request):

    # 跨表查询分为两类:  基于对象查询(子查询)   基于双下划线查询(join查询)
    ############################################## 基于对象查询 ##############################################

    # 1 查询西游记的出版社的 邮箱
    title = request.POST.get("Publish")
    books = Book.objects.filter(title=title)

    #books = Book.objects.filter(price=122)
    # print(book.title)
    # print(book.price)
    # print(book.publisher_id) # 1
    #
    # print(book.publisher) # 与book对象关联的出版社model对象
    # print(book.publisher.email)

    return render(request, "select.html",locals())

    # 2 查询西游记所有作者的名字
    #books = book.authors.all()  # 与book关联的所有作者的集合对象 queyset [alex,egon]
    #print(books) # <QuerySet [<Author: Author object (1)>, <Author: Author object (2)>]>
    #print(books.values("name"))  # <QuerySet [{'name': 'alex'}, {'name': 'egon'}]

    #return render(request,"select.html",{"books":books})


def author_func(request):

    # 跨表查询分为两类:  基于对象查询(子查询)   基于双下划线查询(join查询)
    ############################################## 基于对象查询 ##############################################
    title = request.POST.get("Author")
    books = Book.objects.filter(title=title)
    # 2 查询西游记所有作者的名字
    l_select2 = []
    for book in books:
        book2 = book.authors.all()  # 与book关联的所有作者的集合对象 queyset [alex,egon]
        #print(book2.values("name"))
        for i in book2:
            print(i.name)
            l_select2.append(i)
    print(l_select2)
    # print(books) # <QuerySet [<Author: Author object (1)>, <Author: Author object (2)>]>
    # print(books.values("name"))  # <QuerySet [{'name': 'alex'}, {'name': 'egon'}]
    return render(request, "select2.html",locals())

###
def index(request):

    # 将所有书籍读取出来
    books = Book.objects.all()
    publish_fss = Publish.objects.all()
    author_fss = Author.objects.all()
    #print(publish_fss)

    return render(request,"index.html",locals())


def add(request):

    if request.method=="GET":
         return render(request,"add.html")
    else:
        # 将提交的书籍保存到数据库
        title = request.POST.get("title")
        price = request.POST.get("price")
        publisher_id = request.POST.get("publisher_id")
        pub_date = request.POST.get("pub_date")

        book = Book.objects.create(title=title,price=price,pub_date=pub_date,publisher_id=publisher_id)
        #book = Book.objects.create(title="三国", price=122, pub_date="2012-12-12", publisher_id=2)
        print(book)

        return redirect("/books/")


def delete(request,del_id):
    #print("del_id",del_id)
    #删除

    book = Book.objects.filter(id=del_id).delete()

    return redirect("/books/")

    # return HttpResponse("删除成功")


def edit(request,edit_id):
    print("edit_id",edit_id)
    if request.method == "GET":
        book_edit = Book.objects.get(id=edit_id)

        return render(request,"edit.html",{"book_edit":book_edit})
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        publisher_id = request.POST.get("publisher_id")
        #nid = request.POST.get("nid")
        pub_date = request.POST.get("pub_date")

        book = Book.objects.get(id=edit_id)
        book.price = price
        book.title = title
        book.publisher_id = publisher_id
        book.pub_date = pub_date
        book.save()
        return redirect("/books/")


def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        if request.POST.get("user") == "fss" and request.POST.get("pwd") == "123":
            return redirect("/books/")
        else:
            errlog = "LOGIN ERROR!!!"
            return render(request,"login.html",{"errlog":errlog})

