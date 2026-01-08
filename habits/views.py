from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Habit

@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habits/habit_list.html', {'habits': habits})

@login_required
def habit_create(request):
    if request.method == 'POST':
        Habit.objects.create(
            user=request.user,
            name=request.POST['name']
        )
        return redirect('habit_list')
    return render(request, 'habits/habit_form.html')

@login_required
def habit_done(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    habit.mark_done()
    return redirect('habit_list')

@login_required
def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    habit.delete()
    return redirect('habit_list')
