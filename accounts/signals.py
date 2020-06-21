from django.db.models.signals import post_save
from django.dispatch import receiver

from . models import customer
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# @receiver(post_save,sender=User)
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        customer.objects.create(
                user= instance,
                name = instance.username,
                email = instance.email
            )
        print('profile created...!')
post_save.connect(customer_profile, sender=User) 

# def customer_update(sender, instance, created, **kwargs):
#     if created==False:
#         instance.pro



