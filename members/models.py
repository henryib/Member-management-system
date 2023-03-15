from django.db import models
from django.utils import timezone
today = timezone.now

# Create your models here.
class Member(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    hop = models.CharField(max_length=50)
    date_joined = models.DateField(default=today)
    occupation = models.CharField(max_length=50)
    extra_notes = models.TextField()

    def __str__(self):
        return f'Member: {self.first_name} {self.last_name}'
        
    
