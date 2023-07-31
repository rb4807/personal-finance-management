from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')

# expense_list

@login_required
def expense_list(request):
    user_expenses = Expense.objects.filter(user=request.user)
    return render(request, 'member_list.html', {'user_expenses': user_expenses})

# create_expense

@login_required
def create_expense(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        
        Expense.objects.create(user=request.user, category=category, description=description, date=date, amount=amount)
        return redirect('expense_list')
    else:
        return render(request, 'member_form.html')

# update_expense

@login_required
def update_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        category = request.POST.get('category')
        description = request.POST.get('description')
        date = request.POST.get('date')
        amount = request.POST.get('amount')
        
        expense.category = category
        expense.description = description
        expense.date = date
        expense.amount = amount
        expense.save()
        return redirect('expense_list')
    else:
        return render(request, 'update_expense.html', {'expense': expense})

# delete_expense

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    else:
        return render(request, 'member_list.html', {'expense': expense})






