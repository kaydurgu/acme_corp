from django.db import models
from worker.models import Profile
class Product(models.Model):
    ELECTRONICS = 'EL'
    FASHION = 'FA'
    HOME = 'HO'
    TOYS = 'TO'
    BOOKS = 'BO'
    SPORTS = 'SP'
    BEAUTY = 'BE'
    AUTOMOTIVE = 'AU'
    GROCERY = 'GR'
    HEALTH = 'HE'
    OFFICE = 'OF'
    OTHER = 'OT'
    CATEGORY_CHOICES = [
        (ELECTRONICS, 'Electronics'),
        (FASHION, 'Fashion'),
        (HOME, 'Home'),
        (TOYS, 'Toys'),
        (BOOKS, 'Books'),
        (SPORTS, 'Sports'),
        (BEAUTY, 'Beauty'),
        (AUTOMOTIVE, 'Automotive'),
        (GROCERY, 'Grocery'),
        (HEALTH, 'Health'),
        (OFFICE, 'Office Supplies'),
        (OTHER, 'Other'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=OTHER)
    manufactured_date = models.DateField()
    expiration_date = models.DateField()
    barcode = models.CharField(max_length=25)
    location = models.CharField(max_length=55)
    responsible_worker = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='responsible_worker')

    def __str__(self):
        return self.name
