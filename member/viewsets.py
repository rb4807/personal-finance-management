from rest_framework import viewsets
from . import models
from . import serializers

class ExpenseViewsets(viewsets.ModelViewSet):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer