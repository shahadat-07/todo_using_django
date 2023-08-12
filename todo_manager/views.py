from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.urls import reverse
from todo_manager.models import TaskModel
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import TodoForm

# Create your views here.


class FormView(ListView):
    form_class = TodoForm
    initial = {"key": "value"}
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("show_tasks"))

        return render(request, self.template_name, {"form": form})


class ShowTasksView(ListView):
    model = TaskModel
    template_name = 'show_tasks.html'
    context_object_name = 'tasks'


class EditTaskView(UpdateView):
    model = TaskModel
    fields = ['taskTitle', 'taskDescription']
    template_name = 'edit_task.html'
    success_url = reverse_lazy('show_tasks')


class DeleteTaskView(DeleteView):
    model = TaskModel
    # Replace with your task list URL
    template_name = 'delete_task.html'
    success_url = reverse_lazy('show_tasks')
