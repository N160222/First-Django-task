from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Traineemodels,Trainermodel,Adding,Works
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime

from notifications.signals import notify




def logout_view(request):
    logout(request)
    return redirect('login')

def first(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render({}, request))

# def trainee_registration(request):
#     template=loader.get_template('Trainee_registration.html')
#     return HttpResponse(template.render({}, request))

def registration(request):
    template=loader.get_template('registration.html')
    return HttpResponse(template.render({}, request))

def login_get(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

# def trainer_registration(request):
#     template=loader.get_template('trainer_registration.html')
#     return HttpResponse(template.render({}, request))


@login_required
@user_passes_test(lambda u: u.is_staff)
def trainer_index(request):
    trainer_student_get=Adding.objects.filter(add_trainer_name=request.user).values()
    context = {
    'trainer_students': trainer_student_get,
  }

    template=loader.get_template('trainer_index.html')
    return HttpResponse(template.render(context, request))


@login_required
@user_passes_test(lambda u: u.is_staff)
def trainer_adding_student(request):
    student_get=Adding.objects.filter(add_trainer_name=request.user).values()
    context = {
    'mystudents': student_get,
  }
    template=loader.get_template('trainer_adding_student.html')
    return HttpResponse(template.render(context, request))


@login_required
@user_passes_test(lambda u: u.is_staff)
def trainer_profile(request):
    trainer_get=Trainermodel.objects.filter(trainer_email=request.user).values()
    context = {
    'trainer_data': trainer_get,
  }
    template=loader.get_template('trainer_profile.html')
    return HttpResponse(template.render(context, request))

@login_required
@user_passes_test(lambda u: not(u.is_staff))
def student_index(request):
    student_get=Works.objects.filter(works_student_name=request.user,works_work_status=False).values()
    context = {
    'student_index_data': student_get,
  }
    template=loader.get_template('student_index.html')
    return HttpResponse(template.render(context,request ))
@login_required
@user_passes_test(lambda u: not(u.is_staff))
def student_profile(request):
    student_get=Traineemodels.objects.filter(trainee_email=request.user).values()
    context = {
    'student_data': student_get,
  }
    
    template=loader.get_template('student_profile.html')
    return HttpResponse(template.render(context, request))



@login_required
@user_passes_test(lambda u: not(u.is_staff))
def student_history(request):

    student_works_data=Works.objects.filter(works_student_name=request.user)
    context={
        "student_works_data":student_works_data,
    }
    template=loader.get_template('student_history.html')
    return HttpResponse(template.render(context, request))

def add_trainer(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        username = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        password = request.POST['password']
        if not(Trainermodel.objects.filter(trainer_email=username).exists()):
            user = User.objects.create_user(username=username,password=password)
            user.is_staff=True
            user.save()

            member = Trainermodel(trainer_fname=firstname, trainer_lname=lastname,trainer_email=username,trainer_phone=phone,trainer_dob=dob,trainer_password=password)
            member.save()
            print("New Trainer Added!!!!!!")
            login(request,user)
            return HttpResponseRedirect(reverse('trainer_index'))
        else:
            print("User Exists!!!!!!!!!!!!!")
            return HttpResponseRedirect(reverse("registration"))


    return render(request,'/')


def add_trainee(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        password = request.POST['password']
        if not(Traineemodels.objects.filter(trainee_email=username).exists()):
            user = User.objects.create_user(username=username,password=password)
            user.is_staff=False
            user.save()
            member = Traineemodels(trainee_fname=firstname, trainee_lname=lastname,trainee_email=username,trainee_phone=phone,trainee_dob=dob,trainee_password=password)
            member.save()
            print("New Trainee Added!!!!!!")
            login(request,user)
            return HttpResponseRedirect(reverse('student_index'))
        else:
            print("User Exists!!!!!!!!!!!!!")
            return HttpResponseRedirect(reverse("registration"))
    return render(request,'/')

def login_user(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        # print(username)
        # user=authenticate(Traineemodels.trainee_email=username,Traineemodels.trainee_password=password)
        user = authenticate(username=username,password=password)
        # print(user)
        
        if user is not None:
            if user.is_staff:
                login(request,user)
                return HttpResponseRedirect(reverse('trainer_index'))
            else:
                login(request,user)
                return redirect("student_index")
        else:
            print('Authentication is Failed')
            return redirect('login')

def add_student(request):
    if request.method=="POST":
        stu_name=request.POST["email"]
        stu_phone=request.POST["phone"]
        if Traineemodels.objects.filter(trainee_email=stu_name).exists():
            # if Adding.objects.values_list('add_student_name', flat=True).get(add_trainer_name=request.user) is None:
            adding_trainers_values=Adding.objects.filter(add_trainer_name=request.user).values()
            if not(adding_trainers_values.filter(add_student_name=stu_name).exists()):
                print("Studnet added")
                member=Adding(add_student_name=stu_name,add_student_phone=stu_phone,add_trainer_name=request.user)
                member.save()
                return HttpResponseRedirect(reverse('trainer_adding_student.html'))
            else:
                print("Student already exists!!!!")
                return HttpResponseRedirect(reverse('trainer_adding_student.html'))
        else:
            print("User Doesn't exist!!!!!!!!")
            return HttpResponseRedirect(reverse('trainer_index'))
   
    # return HttpResponseRedirect(reverse('trainer_adding_student.html'))


def student_name_para(request,work_student_name):


    print(request.user)
    print(work_student_name)

    tra_stu_data=Works.objects.filter(works_trainer_name=request.user, works_student_name=work_student_name).values()
    print(tra_stu_data)
    context={
        "tra_stu_data":tra_stu_data,
        'work_student_name' : work_student_name,
    }
    return render(request, 'work_assign.html', context)


def work_assgin(request):
    return HttpResponseRedirect(reverse('work_assign.html'))

def add_work(request):
    if request.method=="POST":
        trainer_name_work = request.POST['trainer_name_work']
        student_name_work = request.POST['student_name_work']
        subject = request.POST['subject']
        question = request.POST['question']
        work_date_assign=datetime.now()
        member=Works(works_trainer_name=trainer_name_work,works_student_name=student_name_work,works_subject=subject,works_question=question)
        member.save()
        return HttpResponseRedirect(reverse('trainer_index'))

def answer(request):
    if request.method=="POST":
        work_id = request.POST['work_id']
        trainer_name_answer = request.POST['trainer_name_work']
        student_name_answer = request.POST['student_name_work']
        student_answer=request.POST['Answer']
        work_date_upload=datetime.now()

        obj, created = Works.objects.update_or_create(
    id=work_id, works_student_name=student_name_answer,
    defaults={'works_upload_date': datetime.now(),'works_student_answer':student_answer,'works_work_status':True},
)

        #notifications sending
        notify.send(student_name_answer, recipient=trainer_name_answer, verb='Done', description=request.POST.get(student_name_answer+'Done'))

        print("Work Answered!!!!!!!!!!")
        return HttpResponseRedirect(reverse('student_index'))








