from member.viewsets import ExpenseViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('expense',ExpenseViewsets)