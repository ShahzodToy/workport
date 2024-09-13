from django.db import models

class Shared(models.Model):
    title = models.CharField(max_length=125)
    desc = models.CharField(max_length=125)

    class Meta:
        abstract = True

class Post(Shared):
    img = models.ImageField(upload_to='post/')
    category = models.CharField(max_length=125)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Portfolio(Shared):
    img = models.ImageField(upload_to='portfolio/')
    category = models.CharField(max_length=125)

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

    def __str__(self):
        return self.username