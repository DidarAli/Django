from django.db import models

# Create your models here.

from django.urls import reverse
class Kafedra(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=100)
    institut_name = models.CharField(max_length=100)
    date_of_create = models.DateField(null=True, blank=True)
   
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('kafedra-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.name, self.institut_name)
		

class Predmet(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=100)
    
   
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('predmet-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)		