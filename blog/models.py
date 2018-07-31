from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'blog_images/')

    def __str__(self):
        return self.title

    def get_summary(self):
        x = self.body
        return x[0:20]+".."

    

