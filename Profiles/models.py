from django.db import models
from Signups.models import Signups


# Create your models here.
class Biog(models.Model):
    user_id = models.ForeignKey(Signups, on_delete = models.CASCADE)
    user_bio = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Biog'
        
    def __str__(self):
        return self.user_bio

class Imageuploads(models.Model):
    image_name = models.ImageField(upload_to = 'imagepost/', null = False)
    image_caption = models.TextField(max_length=3000, null=True)
    profile = models.ForeignKey(Signups, on_delete = models.CASCADE)

    class Meta:
        db_table = 'Imageuploads'

    def __str__(self):
        return self.image_caption

class Comments(models.Model):
    post_id = models.ForeignKey(Imageuploads, on_delete = models.CASCADE)
    comment_by = models.ForeignKey(Signups, on_delete = models.CASCADE)
    comment_post = models.TextField(max_length=3000)
    posted_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Comments'

    def __str__(self):
        return self.comment_post

class Likes(models.Model):
    post_id = models.ForeignKey(Imageuploads, on_delete = models.CASCADE)
    liked_by = models.ForeignKey(Signups, on_delete = models.CASCADE)
    liked_date = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'Likes'

    def __str__(self):
        return self.liked_by