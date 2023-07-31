from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    OPTIONS = (
        ('Books', 'Books 1'),
        ('Education', 'Education 2'),
        ('Travel', 'Travel 3'),
        ('Eletronics', 'Eletronics 4'),
        ('Other', 'Other 5'),
    )
    category = models.CharField(max_length=100, choices=OPTIONS)
    description = models.TextField()
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name



