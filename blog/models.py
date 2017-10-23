from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    #STATUS_CHOICES = (
        #('draft', 'Draft'),
        #('published', 'Published'),
    #)

    author = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    #status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    #class Meta:
        #ordering = ('-published_date',)

    def publish(self):
        self.published_date = timezone.now()
        #self.status ='published'
        self.save()

    def __str__(self):
        return self.title
