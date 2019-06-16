from django.db import models
from django.contrib.auth.models import User
#Product class


class Product(models.Model):
	title = models.CharField(max_length=50, default=None) #default set to None
	pub_date = models.DateTimeField(null=True)
	body = models.TextField(max_length=500, default=None) #default set to None
	image = models.ImageField(upload_to='images/')
	url = models.TextField(max_length=50, default=None)
	icon = models.ImageField(upload_to='images/')
	vote_totals = models.IntegerField(default=1) #default user gets 1 vote
	hunter = models.ForeignKey(User, on_delete=models.CASCADE) #get id of user of other model if User is removed also delete the product

	def __str__(self): #data model method
		return self.title #set the name of the object to the title in admin

	def summary(self):
		return self.body[:100] #return only the first 100 characters

	def pub_date_pretty(self):
		return self.pub_date.strftime('%m.%d.%Y') #month, day, year




#hunter