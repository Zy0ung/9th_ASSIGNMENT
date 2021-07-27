from django.db import models
from django.db.models.deletion import CASCADE

class Blog(models.Model): # models 모듈 안에 있는 Model 클래스 상속
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to = "blog/", blank=True, null=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content=models.CharField(max_length=200)
    author=models.CharField(max_length=50)
    blog=models.ForeignKey(Blog, on_delete=CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    
class Cat(models.Model):
    cat_name=models.CharField(max_length=100)
    cat_sex=models.CharField(max_length=10)
    cat_img=models.ImageField(upload_to="blog/", blank=True, null=True)
    cat_trait=models.TextField(max_length=100)
    pub_date=models.DateTimeField()
    
    def __str__(self):
        return self.cat_name