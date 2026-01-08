from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from planner.models import Assignment
from habits.models import Habit
from datetime import date

@login_required
def dashboard(request):
    assignments = Assignment.objects.filter(
        user=request.user,
        is_completed=False
    ).order_by('due_date')[:5]

    habits = Habit.objects.filter(user=request.user)

    context = {
        'assignments': assignments,
        'habits': habits,
        'today': date.today(),
    }
    return render(request, 'dashboard/dashboard.html', context)
