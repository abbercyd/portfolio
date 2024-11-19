from django.db import models

class Project(models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length= 200)
    image =models.ImageField(upload_to = 'projects/' )
    technologies = models.CharField(max_length=64)
    link = models.URLField(blank= True)

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.company

class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



