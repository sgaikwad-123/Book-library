from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    front_page = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    
    def __str__(self):
        return self.title