from django.db import models

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='mentors/')
    description_usmle = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.name}'


class Logo(models.Model):
    img = models.ImageField(upload_to='logo/')
    link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.link}'

class Link(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'{self.name}'

class About(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    link = models.CharField(max_length=100, default='qwerty')

    def __str__(self) -> str:
        return f'{self.name}'

class Stat(models.Model):
    number = models.IntegerField()
    description = models.TextField(max_length=255)
    suffix = models.CharField(max_length=10, default='+')

    def __str__(self) -> str:
        return f'{self.number}'

class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    schedule = models.TextField(max_length=255)
    feature = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.name}'

