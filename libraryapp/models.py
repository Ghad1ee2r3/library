from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Memberships(models.Model):
    namebook = models.CharField(max_length=120)
    user= models.CharField(max_length=120)
    datereturn= models.DateField(default=timezone.now)
    #book= models.OneToOneField(Book, default=" ", on_delete=models.CASCADE)



class Book(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    yearRelease = models.DateField(default=timezone.now)
    #GENERAL = "G"
    #EDUCATIONAL = "E"# educational
    #NOVELS = "N"#novels
    # choices=[(GENERAL,"General culture"),(EDUCATIONAL,"Educational"),(NOVELS,"Novels")]
    genre = models.CharField( max_length=120,)
    available = models.BooleanField(default=True)
    memberships= models.ForeignKey(Memberships, default=" ", on_delete=models.CASCADE)
    librarian= models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    isbn = models.IntegerField()
    #teacher= models.ForeignKey(User, default=1, on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse('list-detail', kwargs={'book_id':self.id})



    #def get_absolute_url(self , jquery):
    #    return reverse('list-detail', kwargs={'book_id':self.id})
