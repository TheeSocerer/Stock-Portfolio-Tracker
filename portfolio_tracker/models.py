from django.db import models


class Portfolios(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()


    def __str__(self):
        return self.first_name + " " + self.last_name
