from django.shortcuts import render, get_object_or_404
from college.models import Branch, Student, Staff
from college.forms import StaffForm, StudentForm, BranchForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/staff/login/')
def staff_branch(request):
    branches = Branch.objects.all()
    return render(request, 'staff/branch.html', {'branches': branches})


@login_required(login_url='/staff/login/')
def staff_list(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    staff_list = branch.staff_set.all()
    return render(request, 'staff/staff_list.html', {'staff_list': staff_list, 'branch': branch})


@login_required(login_url='/staff/login/')
def staff_details(request, branch_id, staff_id):
    branch = Branch.objects.get(id=branch_id)
    staff = branch.staff_set.get(pk=staff_id)
    return render(request, 'staff/staff_details.html', {"staff": staff, 'branch': branch})


@login_required(login_url='/staff/login/')
def save_staff(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/st_b/{}/'.format(branch.id))
        return render(request, 'staff/create_staff.html', {'form': form})
    form = StaffForm()
    return render(request, 'staff/create_staff.html', {'form': form})


@login_required(login_url='/staff/login/')
def update_satff(request, branch_id, staff_id):
    # breakpoint()
    branch = get_object_or_404(Branch, id=branch_id)
    staff = branch.staff_set.get(id=staff_id)
    if request.method == "POST":
        form = StaffForm(request.POST, request.FILES, instance=staff)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/st_b/{}/'.format(branch_id))
        return render(request, 'staff/staff_update.html', {'form': form})
    form = StaffForm(instance=staff)
    return render(request, 'staff/staff_update.html', {'form': form})


@login_required(login_url='/staff/login/')
def delete_satff(request, branch_id, staff_id):
    branch = Branch.objects.get(id=branch_id)
    staff = branch.staff_set.get(id=staff_id)
    staff.delete()
    return HttpResponseRedirect('/staff/st_b/{}/'.format(branch_id))


@login_required(login_url='/staff/login/')
def create_staff_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/')
        return render(request, 'staff/staff_branch_create.html', {'form': form})
    form = BranchForm()
    return render(request, 'staff/staff_branch_create.html', {'form': form})


# student_details
@login_required(login_url='/std_br/login/')
def student_branch(request):
    branches = Branch.objects.all()
    return render(request, 'student/student_branches.html', {'branches': branches})


@login_required(login_url='/std_br/login/')
def student_list(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    students = branch.student_set.all()
    return render(request, 'student/student_list.html', {'students': students, 'branch': branch})


@login_required(login_url='/std_br/login/')
def student_details(request, branch_id, student_id):
    branch = Branch.objects.get(id=branch_id)
    # breakpoint()
    student = branch.student_set.get(pk=student_id)
    return render(request, 'student/student_details.html', {"student": student, 'branch': branch})


# @login_required(login_url='/std_br/login/')
def save_student(request, branch_id):
    branch = Branch.objects.get(id=branch_id)
    if request.method == 'POST':
        # breakpoint()
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return HttpResponse('APPLICTON SUBMITED SUCCESSFULLY')
            return HttpResponseRedirect('/std_br/{}/'.format(branch.id))
        return render(request, 'student/create_student.html', {'form': form, 'branch': branch})
    form = StudentForm()
    return render(request, 'student/create_student.html', {'form': form, 'branch': branch})


@login_required(login_url='/std_br/login/')
def update_student(request, branch_id, student_id):
    # breakpoint()
    branch = get_object_or_404(Branch, id=branch_id)
    student = branch.student_set.get(id=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/std_br/{}/'.format(branch_id))
        return render(request, 'student/student_update.html', {'form': form, 'branch': branch, 'student': student})
    form = StudentForm(instance=student)
    return render(request, 'student/student_update.html', {'form': form, 'branch': branch, 'student': student})


@login_required(login_url='/std_br/login/')
def delete_student(request, branch_id, student_id):
    branch = Branch.objects.get(id=branch_id)
    student = branch.student_set.get(id=student_id)
    student.delete()
    return HttpResponseRedirect('/std_br/{}/'.format(branch_id))


def home_page(request):  # , std_branch_id, student_id):
    # std_branch = Branch.objects.get(id=std_branch_id)
    # student = std_branch.student_set.get(id=student_id)
    return render(request, 'home.html', )  # {'std_branch': std_branch, 'student': student})


def staff_signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/staff/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/staff/login/')
        else:
            return render(request, 'staff/signin.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'staff/signin.html', {'form': form})


def staff_login(request):
    if request.user.is_authenticated:
        return render(request, 'staff/branch.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/staff/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'staff/log_in.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'staff/log_in.html', {'form': form})


def staff_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')


def student_signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/staff/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/std_br/login/')
        else:
            return render(request, 'student/signin.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'student/signin.html', {'form': form})


def student_login(request):
    if request.user.is_authenticated:
        return render(request, 'student_branches.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/std_br/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'student/log_in.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'student/log_in.html', {'form': form})


def student_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')
