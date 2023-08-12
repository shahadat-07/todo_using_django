from django.urls import path
from todo_manager.views import FormView, ShowTasksView, EditTaskView, DeleteTaskView

urlpatterns = [
    path('', FormView.as_view(), name="home"),
    path('show_tasks/', ShowTasksView.as_view(), name='show_tasks'),
    path('task/<int:pk>/edit/', EditTaskView.as_view(), name='edit_task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),


]
