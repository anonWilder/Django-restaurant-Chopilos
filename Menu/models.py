from django.db import models

# Create your models here.
class HotDeal(models.Model):
    image = models.ImageField(upload_to='hot_deal_images/')
    title = models.CharField(max_length=100)
    discount = models.PositiveIntegerField()
    offer_end_period = models.CharField(max_length=8)
    #instruction = models.TextField()

    def __str__(self):
        return self.title


