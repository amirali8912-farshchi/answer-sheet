from django.db import models

class Font(models.Model):
    data_b64 = models.TextField()  # فونت به صورت Base64
