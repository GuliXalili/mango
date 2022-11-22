from django.db import models

class Choco(models.Model):
    name = models.CharField(max_length=20)
    engridients = models.TextField(max_length=700)
    price = models.FloatField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Cakes(models.Model):
    name = models.CharField(max_length=20)
    engridients = models.TextField(max_length=700)
    price = models.FloatField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    height = models.IntegerField(default=10)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Flow(models.Model):
    name = models.CharField(max_length=20)
    color = models.TextField(max_length=20)
    price = models.FloatField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=20)
    genre = models.CharField(max_length=20)
    pages = models.IntegerField(default=70)
    price = models.FloatField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Prof(models.Model):
    name = models.CharField(max_length=20)
    uniform = models.CharField(max_length=50)
    selery = models.IntegerField(default=1000000)
    date = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Mess(models.Model):
    name = models.CharField(max_length=20)
    users = models.IntegerField(default=50000)
    date = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
