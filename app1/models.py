from django.db import models

# Create your models here.

class Book(models.Model):

    #自增，设置primary_key（唯一且自增）
    id = models.AutoField(primary_key=True)

    #字符串，相当于sql语句中的char
    title = models.CharField(max_length=32)

    #时间
    pub_date = models.DateField()

    #小数，后面参数最大八位数包含两个小数位
    price = models.DecimalField(max_digits=8,decimal_places=2)

    publish = models.CharField(max_length=32)

    def __str__(self):
        return self.title