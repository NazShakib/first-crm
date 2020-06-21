from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class customer(models.Model):
	user = models.OneToOneField(User,blank=True, null =True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200,null =True)
	email = models.EmailField(max_length=30,null =True)
	phone = models.CharField(max_length = 13,null =True)
	profile_pic = models.ImageField(default="profile1.png",null= True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True,null =True)
	
	def __str__(self):
		return self.name

#    CATEGORY = [
#        ('Indoor', 'Indoor'),
#        ('Out Door', 'Out Door'),
#     ] 

class Tag(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 


	name = models.CharField(max_length=200,null= True)
	price = models.FloatField(null= True)
	category = models.CharField(max_length=200, choices=CATEGORY,null= True)
	description = models.CharField(max_length=200,null= True)
	date_created = models.DateTimeField(auto_now_add=True, null= True)
	tags = models.ManyToManyField(Tag)
	
	def __str__(self):
		return self.name
	


class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(customer, null= True, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, null= True, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null= True)
	status = models.CharField(max_length=200, choices=STATUS,null= True)
	note = models.CharField(max_length=200,null= True)

	def __str__(self):
	 return self.product.name

