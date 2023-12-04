from django.db import models

class QuoteRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=100)
    time_period = models.CharField(max_length=50)
    specify = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

