from django.db import models

class Post(models.Model):
    subject = models.CharField(max_length = 100)
    pub_date = models.DateTimeField(auto_now_add=True)
    article = models.TextField()
    
    def __unicode__(self):
        return self.subject

class Comment(models.Model):
    post = models.ForeignKey(Post)
    user_name = models.CharField(max_length=30, blank=True)
    text = models.TextField()
    subject = models.CharField(max_length = 100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.subject
    
    
