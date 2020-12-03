from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    pub_date = models.DateField()

    # ForeignKey会生成字段publisher_id实现一对多
    publisher = models.ForeignKey("Publish",on_delete=models.CASCADE)

    # ManyToManyField会创建第三张表Book_authors实现 多对多 的关系
    authors = models.ManyToManyField("Author")

class Publish(models.Model):

    name = models.CharField(max_length=32)
    addr = models.CharField(max_length=32)
    email = models.CharField(max_length=32)


class Author(models.Model):
    # books = models.ManyToManyField("Book")
    name = models.CharField(max_length=32)
    tel = models.CharField(max_length=32)
    # OneToOneField会创建一个唯一约束字段ad_id字段实现一对一关系
    ad = models.OneToOneField("AuthorDetail",on_delete=models.CASCADE)

class AuthorDetail(models.Model):

    addr = models.CharField(max_length=32)
    gf = models.CharField(max_length=32)




# class Book2Author(models.Model):
#     book= models.ForeignKey("Book",on_delete=models.CASCADE)
#     author= models.ForeignKey("Author",on_delete=models.CASCADE)
