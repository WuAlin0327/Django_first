from django.db import models

# Create your models here.
#书籍表

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

#表关系模型创建：创建一个出版社表，关联然后书籍出版社绑定出版社表的ID
#假设每本书只有一个作者

# 创建作者表
class Author(models.Model):
    aid = models.AutoField(primary_key=True)
    a_name = models.CharField(max_length=16)
    age = models.IntegerField()

# 先创建出版社表

class Publish(models.Model):
    pid = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=16)
    p_addr = models.CharField(max_length=32)

# 然后创建书籍表
class Books(models.Model):
    bid = models.AutoField(primary_key=True)
    b_name = models.CharField(max_length=16)
    price = models.DecimalField(max_digits=8,decimal_places=2)

    #创建关联表时不需要在关联字段后面加_id,ORM会自动加
    # 关联表关系：一对多关系
    # to=表的时候可以加引号也可以不加，不加引号的话必须被关联的表在关联表上面，to_field也可以不写主键，不写的话默认是关联表的主键
    publish = models.ForeignKey(to="Publish",to_field="pid",on_delete=models.CASCADE)

    # 关联表关系：一对一
    #on_delete=models.CASCADE在一对多的时候必须要加，一对多的时候也必须要加,如果不加会报on_delete错误
    # null = True  #允许关联字段为空
    author = models.OneToOneField(to=Author,to_field='aid',on_delete=models.CASCADE)

    # 关联表关系：多对多。会另外生成第三张表，不会在该表内生成字段
    # 字段名 = models.ManyToManyField(to='关联表')
