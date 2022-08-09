from django.db import models
from account.models import CustomUser

# Create your models here.


class Menyu(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='CustomUser')
    menyu_image=models.ImageField(upload_to='media',null=True,blank=True)


    


    def __str__(self) -> str:
        return self.content