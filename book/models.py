from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=100,null=False)
    price = models.FloatField(null=False,default=0)

    def __str__(self):
        return "<book:{name},{author},{price}>".format(name=self.name,author=self.author,price=self.price)