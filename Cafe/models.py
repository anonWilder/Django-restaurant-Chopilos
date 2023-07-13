from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField
from users.models import Profile as profile


# CATEGORY_CHOICES = (
#     ('S', 'Shirt'),
#     ('SW', 'Sport wear'),
#     ('OW', 'Outwear')
# # )

# class Category(models.Model):
#     name = models.CharField(max_length=100, verbose_name='分类名称')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "cate"
#         verbose_name_plural = verbose_name

#     def get_absolute_url(self):
#         return reverse('core:category', kwargs={'pk': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('core:category', args=[self.slug])

    def __str__(self):
        return self.name


LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    one_click_purchasing = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    preview_price = models.CharField(max_length=100,default="0.00")
    price = models.FloatField()
    user = models.ForeignKey(to=profile, on_delete=models.CASCADE)
    # item_type = models.CharField(max_length=50, choices=(
    #     ('1', 'p'), ('0', 't')), default='1')
    discount_price = models.FloatField(blank=True, null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.CharField(blank=True,max_length=850,null=True,default="/static/images/banner3.png")
    # breakfast = models.BooleanField(default=False)
    protein = models.BooleanField(default=False)
    special = models.BooleanField(default=False)
    drinks = models.BooleanField(default=False)
    break_fast = models.BooleanField(default=False)
    starters = models.BooleanField(default=False)
    rice = models.BooleanField(default=False)
    pasta_and_nodles = models.BooleanField(default=False)
    sauce_and_stew = models.BooleanField(default=False)
    salad = models.BooleanField(default=False)
    sandwich_and_burgers = models.BooleanField(default=False)
    side = models.BooleanField(default=False)
    pepper_soup = models.BooleanField(default=False)
    grills = models.BooleanField(default=False)
    african_soup = models.BooleanField(default=False)
    dessert = models.BooleanField(default=False)

    # this are the bar menu listed

    bar_menu_listed = models.CharField(max_length=100,default="This is the bar menu listed below to fill up")
    cocktails = models.BooleanField(default=False)
    slippery_signatures = models.BooleanField(default=False)
    mocktails = models.BooleanField(default=False)
    milk_shakes = models.BooleanField(default=False)

    smoothies = models.BooleanField(default=False)
    soft_drinks = models.BooleanField(default=False)
    tequila = models.BooleanField(default=False)
    wines = models.BooleanField(default=False)

    champagne = models.BooleanField(default=False)
    cognac = models.BooleanField(default=False)
    whiskey = models.BooleanField(default=False)
    shisha = models.BooleanField(default=False)
    vape = models.BooleanField(default=False)
    
    timestamp = models.DateTimeField(blank=True, null=True)
    created_on = models.DateField(auto_now=True)
    item_created_date = models.DateField(auto_now=True)
    # image_path = models.CharField(max_length=200)
    # category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)

    def __str__(self):
        return f'{self.title} - {self.pk}'

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey(
        'Payment', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    '''
    1. Item added to cart
    2. Adding a billing address
    (Failed checkout)
    3. Payment
    (Preprocessing, processing, packaging etc.)
    4. Being delivered
    5. Received
    6. Refunds
    '''

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        if self.coupon:
            total -= self.coupon.amount
        return total


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = CountryField(multiple=False)
    zip = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Addresses'


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code

class contactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    massage = models.TextField()

    def __str__(self):
        return self.email

class Gallery(models.Model):
    gallery = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Gallery"

class Event(models.Model):
    image = models.ImageField()
    # email =  models.EmailField(max_length=400,default="", blank=True,null=True)
    title =  models.CharField(max_length=400,default="Event")
    # address = models.CharField(max_length=100,default="873, Ozumba Mbadiwe , Victoria Island, Lagos")
    new = models.BooleanField(default=False)
    event_date = models.DateField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("core:event_details", kwargs={
            'pk': self.pk
    })

class PostImage(models.Model):
    post = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.post.title
    
class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    type = models.CharField(max_length=15,default=False)
    phone = models.CharField(max_length=15)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    person = models.CharField(max_length=100)
    massage = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("core:reserved", kwargs={
            'pk': self.pk
        })

class DataCount(models.Model):
    name = models.CharField(max_length=1000)
    count = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.pk}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)
