from django.db import models

# Create your models here.
# 1명 한 test 
class Test(models.Model):
    feelings_action = models.TextField(max_length=100,null = True)
    tendencies = models.TextField(max_length=20,null = True)


def __str__(self):
        return self.test