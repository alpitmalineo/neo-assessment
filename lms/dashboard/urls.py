from django.urls import path, include

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('apply-leave/', views.apply_leave, name='apply_leave'),
    path('leaves/', views.leaves, name='leaves'),
    path('update-leave/<int:pk>/', views.UpdateLeaveView.as_view(), name='update_leave'),
    path('leaves-manage/', views.leave_manage, name='leave_manage'),
    path('leave-detail/<int:id>/', views.leave_detail, name='leave_detail'),
    path('delete-leave/<int:id>/', views.delete_leave, name='delete_leave'),
]
