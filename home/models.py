from typing import Any
from django.db import models
from taggit.managers import TaggableManager
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Shared(models.Model):
    title = models.CharField(_('Title'),max_length=125)
    desc = models.CharField(_('Title'),max_length=125)

    class Meta:
        abstract = True


class CategoryPost(models.Model):
    title = models.CharField(_('Title'),max_length=125)

    def __str__(self):
        return self.title
    
class CommentPost(models.Model):
    comment = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=125)
    email = models.EmailField()
    website = models.CharField(max_length=125, null=True, blank=True)

    def __str__(self) -> str:
        return self.user_name
    
class LikePost(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.title} for like'


class Post(Shared):
    img = models.ImageField(upload_to='post/')
    category = models.ForeignKey(CategoryPost,on_delete=models.CASCADE)
    tags = TaggableManager()
    date = models.DateTimeField(auto_now=True)


    def count_like(self):
        return self.likes.count()
    

    def count_comment(self):
        return self.comments.count()
   

    def __str__(self):
        return self.title
    

class CategoryPortfolio(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title


class Portfolio(Shared):
    img = models.ImageField(upload_to='portfolio/')
    category = models.ForeignKey(CategoryPortfolio,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.title
    
    
class Service(Shared):
    logo = models.ImageField(upload_to='service/logo')

    def __str__(self):
        return self.title
    
    
class Order(models.Model):
    user_name = models.CharField(max_length=125)
    title_service = models.ForeignKey(Service,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title_service.title} for {self.user_name}'
    
    
class PricePlan(models.Model):
    title  = models.ForeignKey(Service,on_delete=models.CASCADE)
    info = models.CharField(max_length=125)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    cretaria_text = models.TextField()

    def __str__(self):
        return self.title.title 
    
    
class Comments(models.Model):
    username = models.CharField(max_length=125)
    comment = models.TextField()
    user_job = models.CharField(max_length=125)
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])

    def __str__(self):
        return self.username
    

class NewsLetterSubs(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class ContactUser(models.Model):
    first_name = models.CharField(max_length=125)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()

    def __str__(self):
        return self.first_name