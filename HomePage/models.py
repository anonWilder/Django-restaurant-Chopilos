from django.db import models

# Create your models here.

#INDEX PAGE OFFER SECTION
class OfferSection(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='offer_images/')
#END

#INDEX PAGE SPECIAL SECTION
class SpecialSection(models.Model):
    image = models.ImageField(upload_to='special_images/')
    title = models.CharField(max_length=100)
    description = models.TextField()
#END

#INDEX PAGE HEADSLIDER
class SlideshowItem(models.Model):
    image = models.ImageField(upload_to='slideshow_images/')
    title = models.CharField(max_length=200)
    text = models.TextField()
#END

#INDEX CONTACT US SECTION
class ContactInfo(models.Model):
    booking_phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    opening_hours = models.CharField(max_length=100)

#END


#INDEX UPCOMING EVENT SECTION
class UpcomingEvent(models.Model):
    image1 = models.ImageField(upload_to='event_images/')
    image2 = models.ImageField(upload_to='event_images/')
    # Add other fields as required

#END

#INDEX GALLERY SECTION
class Gallery(models.Model):
    gallery = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Gallery"
#END

#INDEX DATA COUNT
class DataCount(models.Model):
    name = models.CharField(max_length=1000)
    count = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
#END