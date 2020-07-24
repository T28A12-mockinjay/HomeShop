from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField        # when there is no primary key django makes its own primary key with name "id"
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    image = models.ImageField(upload_to="shop/images",default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=3000)
    pub_date = models.DateField()

    def __str__(self):
        return self.name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)        # when there is no primary key django makes its own primary key with name "id"
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=50,default="")
    query = models.CharField(max_length=3000,default="")


    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=3000,default="")
    name = models.CharField(max_length=3000,default="")
    email = models.CharField(max_length=200,default="")
    add = models.CharField(max_length=200,default="")
    city = models.CharField(max_length=200,default="")
    state = models.CharField(max_length=200,default="")
    zip_code= models.CharField(max_length=200,default="")
    phone= models.CharField(max_length=200,default="")

    def __str__(self):
        return  self.name

class OrderUpdates(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)   # if you haven't specified the value for variable then default value will be the current time.

    def __str__(self):
        st = str(self.order_id)
        return st
        #return self.update_desc[0:9] + "..."

