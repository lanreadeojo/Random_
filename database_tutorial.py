from django.db import models


class Genre(models.Model):
    """ A model representing a book genre"""
    name = models.CharField(max_length = 200, help_text = 'Enter a book genre e.g (Fiction or nonFiction)')

    def __str__(self):
        """String for representing the model object"""
        return self.name

from django.urls import reverse
# used to generate URLs by reversing the URL patterns


class Book(models.Model):
    """ Model representing a book (but not a specific copy of a book
    )."""
    title = models.CharField(max_length= 200)

    #Foreighn key used because book can only have one author,
    # but authors can have multiple books
# Author as a string rather than object because it hasn't bee
#declared yet in the file
    author = models.ForeignKey('Author', on_delete = models.SET_NULL,
            null = True)

    summary = models.TextField(max_length = 1000, help_text = 'Enter a brief description of the book')

    isbn = models.CharField('ISBN', max_length=13, unique = True, help_text ='13 Character <a href= "https: //www.isbn-international.org/content/what-isbn"> ISBN number<a>')

    # ManyToManyField used because genre can contain many book. books can cover many genres.
    # Genre class has already been we can specify the object above.

    genre = models.ManyToManyField(Genre, help_text = 'selects a genre for this book')

    def __str__(self):
        """ String fro representing the Model object."""
        return self.title
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args = [str(self.id)])