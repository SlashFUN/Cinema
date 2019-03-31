from django.db import models
from django.urls import reverse

class Genre(models.Model):
    """
        Model representing a Film genre (e.g. Science Fiction, Non Fiction).
        """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Language(models.Model):
        """Model representing a Language (e.g. English, French, Japanese, etc.)"""
        name = models.CharField(max_length=200,
                                help_text="Enter the film's natural language (e.g. English, French, Japanese etc.)")

        def __str__(self):
            """String for representing the Model object (in Admin site etc.)"""
            return self.name

class Film(models.Model):
    title = models.CharField(max_length=200)
    producer = models.ForeignKey('Producer', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the film")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this film")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular film instance.
        """
        return reverse('film-detail', args=[str(self.id)])
    def display_genre(self):
        """
                        Creates a string for the Genre. This is required to display genre in Admin.
                        """
        return ','.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'
        


import uuid  # Required for unique film rents


class FilmRent(models.Model):
    """
    Model representing a specific copy of a film (i.e. that can be watched free from the cinema).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular film across whole cinema")
    film = models.ForeignKey('Film', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Film availability')

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0}, ({1})'.format(self.id, self.film.title)

class Producer(models.Model):
        """
        Model representing an author.
        """
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        date_of_birth = models.DateField(null=True, blank=True)
        date_of_death = models.DateField('Died', null=True, blank=True)

        def get_absolute_url(self):
            """
            Returns the url to access a particular producer instance.
            """
            return reverse('producer-detail', args=[str(self.id)])

        def __str__(self):
            """
            String for representing the Model object.
            """
            return '{0}, {1}'.format(self.last_name, self.first_name)
