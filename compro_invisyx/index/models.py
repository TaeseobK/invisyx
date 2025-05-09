from django.db import models

class ContactUs(models.Model) :
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=64)
    email = models.EmailField()
    company = models.CharField(max_length=64, null=True, blank=True)
    subject = models.CharField(max_length=128)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta :
        app_label = "index"
        managed = True
        db_table = "contact_us"