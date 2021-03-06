from django.db import models


class Word(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="word")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Definition(models.Model):
    description = models.TextField(verbose_name="definition")
    # Each description is related to a word.
    # If the word is removed all descriptions will be removed as well.
    word = models.ForeignKey('Word', on_delete=models.CASCADE)

    def __str__(self):
        return self.description
