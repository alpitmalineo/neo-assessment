from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from accounts.enums import RoleType
from accounts.forms import SignUpForm, EditUserForm
from accounts.models import User
from accounts.utils import is_admin_or_is_hod_or_is_staff, is_hod
from dashboard.enums import StatusType
from dashboard.models import Leave


# Create your views here.
@user_passes_test(is_admin_or_is_hod_or_is_staff, login_url='accounts:logout')
def dashboard(request):
    users = User.objects.filter(role_type=RoleType.STAFF, department=request.user.department, is_active=True).count()
    pending_leaves = Leave.objects.filter(user__department=request.user.department,
                                          status=StatusType.PENDING).order_by('id').count()
    approved_leaves = Leave.objects.filter(user__department=request.user.department,
                                           status=StatusType.APPROVED).order_by('id').count()
    rejected_leaves = Leave.objects.filter(user__department=request.user.department,
                                           status=StatusType.REJECTED).order_by('id').count()
    context = {'users': users, 'pending_leaves': pending_leaves, 'approved_leaves': approved_leaves,
               'rejected_leaves': rejected_leaves}
    return render(request, 'accounts/dashboard.html', context)


def role(request):
    return render(request, 'registration/role.html')


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('accounts:dashboard')
        else:
            return redirect('accounts:dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                request.session.set_expiry(3600)
                if user.is_admin:
                    return redirect('accounts:dashboard')
                else:
                    return redirect('accounts:dashboard')
            else:
                messages.info(request, 'Username OR Password is Incorrect !')
        context = {}
        return render(request, 'registration/login.html', context)


def hod_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.role_type = RoleType.HOD
            user_obj.save(['role_type'])
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    return render(request, 'registration/hod_signup.html', {'form': form})


def staff_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.role_type = RoleType.STAFF
            user_obj.save(['role_type'])
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    return render(request, 'registration/hod_signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts:login')


@user_passes_test(is_hod, login_url='accounts:logout')
def add_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/add-user.html', {'form': form})


@user_passes_test(is_hod, login_url='accounts:logout')
def user(request):
    users = User.objects.filter(role_type=RoleType.STAFF, department=request.user.department)
    context = {'users': users, }
    return render(request, 'accounts/user.html', context)


class UpdateUserView(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = "accounts/edit-user.html"
    form_class = EditUserForm
    login_url = '/login/'
    success_url = reverse_lazy('accounts:user')


@user_passes_test(is_hod, login_url='accounts:logout')
def delete_user(request, id):
    user_obj = User.objects.get(id=id)
    user_obj.delete()
    return redirect('accounts:user')


@user_passes_test(is_hod, login_url='accounts:logout')
def user_detail(request, id):
    users = get_object_or_404(User, id=id)
    return render(request, 'accounts/user-details.html', {'users': users})


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Password Changed", extra_tags='green')
            return redirect('accounts:dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'registration/password-change-form.html', context)
