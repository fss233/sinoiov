from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
import json


def index(request):

   # 将所有书籍读取出来
    books=[]
    with open("book.txt","r") as f:
        for line in f.readlines():
            books.append(json.loads(line))
    #print(books) # [{},{},{}]

    return render(request,"index.html",locals())



def add(request):

    if request.method=="GET":
         return render(request,"add.html")
    else:
        # 将提交的书籍保存到数据库
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        nid = request.POST.get("nid")

        book = {"title":title,"price":price,"publish":publish,"nid":nid}

        with open("book.txt","a") as f:

            f.write(json.dumps(book)+"\n")

        return redirect("/")


def delete(request,del_id):
    #print("del_id",del_id)

    #删除
    with open("book.txt", "r") as f:
        for line in f.readlines():
            print("fss_JS")
            print(json.loads(line)['nid'])
            if json.loads(line)['nid'] == del_id:
                print("del ok .")
                book = {"title": json.loads(line)['title'], "price": "del", "publish": "del", "nid": '0'}
                with open("book.txt", "a") as fss:
                    fss.write(json.dumps(book)+"\n")
            else:
                pass

    return redirect("/")

    # return HttpResponse("删除成功")


def edit(request,edit_id):
    print("edit_id",edit_id)
    if request.method == "GET":
        with open("book.txt", "r") as f:
            for line in f.readlines():
                # print("fss_JS")
                # print(json.loads(line)['nid'])
                if json.loads(line)['nid'] == edit_id:
                    print("edit ok .")
                    book_edit = {"title":json.loads(line)['title'], "price":json.loads(line)['price'], "publish":json.loads(line)['publish'],"nid":json.loads(line)['nid']}
                    print(book_edit)
                    #print(type(book_edit))
                    #{'title': '一千零一夜', 'price': '99', 'publish': '南阳出版社', 'nid': '3'}
                else:
                    pass

        return render(request,"edit.html",locals())
    else:
        title = request.POST.get("title")
        price = request.POST.get("price")
        publish = request.POST.get("publish")
        #nid = request.POST.get("nid")
        nid = request.POST.get("nid")
        book = {"title": title, "price": price, "publish": publish, "nid": nid}

        with open("book.txt", "a") as f:

            f.write(json.dumps(book) + "\n")

        return redirect("/")

