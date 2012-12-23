from django.db import models

class Post(models.Model):
    subject = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    article = models.TextField()
    
    def __unicode__(self):
        return self.subject

class User(models.Model):
    user_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50, blank = True)
    
    def __unicode__(self):
        return self.user_name
    
    def has_valid_email(self):
        if self.email:
            return True
        else:
            return False
    
class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User, null = True, blank = True)
    parent_comment = models.ForeignKey('self', null = True, blank = True)
    text = models.TextField()
    subject = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    up_vote = models.IntegerField(null = True, blank = True)
    down_vote = models.IntegerField(null = True, blank = True)

    def __unicode__(self):
        return self.subject
    
    
