from django.db import models

class Post(models.Model):
    firstname = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()
    san = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='myblog/%Y/%m/%d')
    likes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.firstname

    class Meta:
        verbose_name_plural = 'Post'
class Dawlet(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField()
    san = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='myblog/%Y/%m/%d')
    price = models.DecimalField(max_digits=10, decimal_places=4)
    slug = models.SlugField(max_length=125, null=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Dawlet'

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category name')
    slug = models.SlugField(max_length=125)

    def __str__(self):
        return f'{self.name}'

    def det_absolute_url(self):
        return f'/home/category/{self.slug}'
    




    
# class Categories(models.Model):
#     name = models.CharField(max_length=30)
#     san = models.IntegerField(max_length=30)