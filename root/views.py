import time

from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login ,logout

from root.forms import SignInForm, SignUpForm, ContactForm
from .models import Course , GiveUnit


def index(request):
    # return HttpResponse('sdaglsdgnksd')

    return render(request, 'index.html' )


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        context = {
                "error1": '',
                "error2": '',

            }

        if request.POST.get('password1') != request.POST.get('password2'):
            context["error2"] = 'گذرواژه و تکرار گذرواژه یکسان نیستند'
        if User.objects.filter(username=request.POST.get('username')).exists():
            context["error1"] = '‫نام کاربری شما در سیستم موجود است‬'
        if context["error1"] or context["error2"]:
            return render(request, "signup.html", context)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})





# context = {
#         "error1": False,
#         "error2": False,
#         "error3": False
#     }
#
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if User.objects.filter(email=request.POST.get('email')).exists():
#             context["error3"] = True
#         if request.POST.get('password1') != request.POST.get('password2'):
#             context["error2"] = True
#         if User.objects.filter(username=request.POST.get('username')).exists():
#             context["error1"] = True
#         if context["error1"] or context["error2"] or context["error3"]:
#             return render(request, "blank.html", context)
#         if form.is_valid():
#             user = form.save()
#             level = form.cleaned_data['type']
#             if level == 'Teacher':
#                 user.groups.add(Group.objects.get(name='Teacher'))
#             else:
#                 user.groups.add(Group.objects.get(name='Student'))
#             return redirect('')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})












# def signin(request):
#
#     form = SignInForm(request.POST)
#     print('step1')
#     if form.is_valid():
#         print('step2')
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#     # username = request.POST['username']
#     # password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Redirect to a success page.
#             print('oooooooooooooooookkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
#
#             return redirect('/')
#         else:
#             # Return an 'invalid login' error message.
#             print('nnnnnnnnnnnnnnoooooooooooooooooooooooooooooo')
#
#             return render(request, 'signin.html')
#
#     return render(request, 'signin.html', {'form' : form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/")
        else:
            return render(request, 'signin.html' , {'error' : 'نام کاربری یا رمز عبور اشتباه است.'})
    return render(request, 'signin.html')





# def contactus(request):
#     # form_class = ContactForm
#     form = ContactForm(request.POST)
#
#     # new logic!
#     if request.method == 'POST':
#         # form = form_class(data=request.POST)
#         if form.is_valid:
#             title = request.POST.get('title', '')
#             myemail = request.POST.get('email', '')
#             text = request.POST.get('text', '')
#
#             # send_mail(title, [text, myemail], myemail , ['m.javad139177@gmail.com‬‬'])
#             # ‫‪webe19lopers @ gmail.com
#             return render(request, 'done.html', )
#     return render(request, 'contactus.html', {
#         'form': form,
#     })


def contactus(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            title = request.POST.get("title")
            text = request.POST.get("text")
            email = request.POST.get("email")
            my_email = EmailMessage(
                    title,
                    f"{text}  {email}",
                    'GaMa forever' + '<webelopers.esband@gmail.com>',
                    ["webe19lopers@gmail.com"],
                )
            my_email.send()
            return render(request, "done.html")
    return render(request, "contactus.html")

def logout_(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required(login_url='/login/')
def profile(request):


    return render(request, 'profile.html', {'username': request.user.username, 'firstname': request.user.first_name,
                                            'lastname': request.user.last_name, 'pic': 'fmkls'})


@login_required(login_url='/login/')
def editprofile(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.profile_pic = request.POST.get('profile_pic')
        user.save()
        return render(request, 'profile.html', {'username': request.user.username, 'firstname': request.user.first_name,
                                                'lastname': request.user.last_name,
                                                })
    return render(request, 'editprofile.html', )





@login_required(login_url='/login/')
def panel(request):
    return render(request , 'panel.html')


# def new_course(request):
#     # form = NewCoursForm(request.POST)
#
#
#     # new logic!
#     if request.method == 'POST':
#         # form = form_class(data=request.POST)
#         # if form.is_valid:
#         department = request.POST.get('department')
#         name = request.POST.get('name')
#         course_number = request.POST.get('course_number')
#         group_number = request.POST.get('group_number')
#         teacher = request.POST.get('teacher')
#         start_time = request.POST.get('start_time')
#         end_time = request.POST.get('end_time')
#         first_day = request.POST.get('first_day')
#         second_day = request.POST.get('second_day')
#
#         obj = Class(department=department , name=name , course_number= course_number , group_number=group_number , teacher= teacher , start_time=start_time , end_time=end_time , first_day=first_day , second_day=second_day)
#         obj.save()
#
#
#             # send_mail(title, [text, myemail], myemail , ['m.javad139177@gmail.com‬‬'])
#             # ‫‪webe19lopers @ gmail.com
#         return render(request, 'done.html' )
#
#
#     return render(request , 'new_course.html')

def new_course(request):
    if request.method == "POST":
        error_time = False
        department = request.POST.get("department")
        name = request.POST.get("name")
        course_number = request.POST.get("course_number")
        group_number = request.POST.get("group_number")
        teacher = request.POST.get("teacher")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        first_day = request.POST.get("first_day")
        second_day = request.POST.get("second_day")
        exam_date = request.POST.get('exam_date')

        try:
            time.strptime(start_time, '%H:%M')
        except ValueError:
            error_time = True
            return render(request, "new_course.html", {"error_time": error_time})

        try:
            time.strptime(end_time, '%H:%M')
        except ValueError:
            error_time = True
            return render(request, "new_course.html", {"error_time": error_time})

        try:
            time.strptime(exam_date , '%yyyy:mm:dd')
        except ValueError:
            error_time =True

        course = Course(department=department, name=name, course_number=course_number, group_number=group_number, teacher=teacher, start_time=start_time , exam_date=exam_date, end_time=end_time, first_day=first_day, second_day=second_day)
        course.save()
        return render(request, "panel.html")

    return render(request, "new_course.html")


def courses(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        unit = request.POST.get('unit')
        course = Course.objects.filter(id=unit)
        user = User.objects.filter(username=request.user.username)

        giveUnit = GiveUnit(name=course.name , user=user)
        giveUnit.save()
        return render(request , 'courses.html', {"units": GiveUnit })

    return render(request, "courses.html", {"courses": courses})


def search(request):
    if request.method =='POST':
        # ser = request.POST.get('search_query')
        # department = request.POST.get('department')
        # teacher = request.POST.get('teacher')
        # course = request.POST.get('course')
        search_query =request.POST.get('search_query')
        # if department and teacher and course:
        #     courses = Course.objects.filter(department=search_query , teacher=search_query , course=search_query)

        # if department:
        #     courses = Course.objects.filter(department=search_query)
        # if teacher:
        #     courses = Course.objects.filter(teacher=search_query)
        # if course:
        #     courses = Course.objects.filter(name=search_query)



        courses = Course.objects.filter(department=search_query)
    return render(request , 'courses.html' , { 'result' : courses})


