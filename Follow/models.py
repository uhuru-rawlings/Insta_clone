from django.db import models
from Signups.models import Signups

# Create your models here.
class Follow(models.Model):
    current_user = models.IntegerField()
    followed_account = models.ForeignKey(Signups, on_delete = models.CASCADE)
    date_followed = models.DateField(auto_now=True)
    
    # position = models.IntegerField()
    class Meta:
        db_table = "Follow"

    def __str__(self):
        return self.followed_account
