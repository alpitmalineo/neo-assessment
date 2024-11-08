from django.urls import path, include

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.role, name='role'),
    path('login/', views.login_view, name='login'),
    path('hod-signup/', views.hod_signup, name='hod_signup'),
    path('staff-signup/', views.staff_signup, name='staff_signup'),
    path('logout/', views.logout_view, name='logout'),
    path('add-user/', views.add_user, name='add_user'),
    path('user/', views.user, name='user'),
    path('update-user/<int:pk>/', views.UpdateUserView.as_view(), name='update_user'),
    path('user-detail/<int:id>/', views.user_detail, name='user_detail'),
    path('delete-user/<int:id>/', views.delete_user, name='delete_user'),
    path('change-password/', views.change_password, name='change-password'),

]
