from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from accounts.utils import is_staff, is_hod, is_admin_or_is_hod_or_is_staff
from dashboard.forms import LeaveForm, EditLeaveForm
from dashboard.models import Leave


# Create your views here.
@user_passes_test(is_staff, login_url='accounts:logout')
def apply_leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.user = request.user
            leave.save()
            return redirect('dashboard:leaves')
    else:
        form = LeaveForm()
    return render(request, 'dashboard/apply-leave.html', {'form': form})


@user_passes_test(is_staff, login_url='accounts:logout')
def leaves(request):
    leaves = Leave.objects.filter(user=request.user).order_by('id')
    paginator = Paginator(leaves, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'leaves': leaves, 'page_obj': page_obj}
    return render(request, 'dashboard/leaves.html', context)


class UpdateLeaveView(LoginRequiredMixin, generic.UpdateView):
    model = Leave
    template_name = "dashboard/update-leave.html"
    form_class = EditLeaveForm
    login_url = '/login/'
    success_url = reverse_lazy('dashboard:leave_manage')


@user_passes_test(is_hod, login_url='accounts:logout')
def leave_manage(request):
    hod = request.user
    department = hod.department
    print(department)
    leaves = Leave.objects.filter(user__department=department).order_by('id')
    print(leaves)
    paginator = Paginator(leaves, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'leaves': leaves, 'page_obj': page_obj}
    return render(request, 'dashboard/leave-manage.html', context)


@user_passes_test(is_admin_or_is_hod_or_is_staff, login_url='accounts:logout')
def leave_detail(request, id):
    leave = get_object_or_404(Leave, id=id)
    return render(request, 'dashboard/leave-details.html', {'leave': leave})


@user_passes_test(is_staff, login_url='accounts:logout')
def delete_leave(request, id):
    leave = Leave.objects.get(id=id)
    leave.delete()
    return redirect('dashboard:leaves')
