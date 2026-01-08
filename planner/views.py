from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Assignment

@login_required
def assignment_list(request):
    assignments = Assignment.objects.filter(user=request.user)
    return render(request, 'planner/assignment_list.html', {'assignments': assignments})

@login_required
def assignment_create(request):
    if request.method == 'POST':
        Assignment.objects.create(
            user=request.user,
            title=request.POST['title'],
            subject=request.POST['subject'],
            due_date=request.POST['due_date']
        )
        return redirect('assignment_list')
    return render(request, 'planner/assignment_form.html')

@login_required
def assignment_complete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, user=request.user)
    assignment.is_completed = True
    assignment.save()
    return redirect('assignment_list')

@login_required
def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, user=request.user)
    assignment.delete()
    return redirect('assignment_list')
