from django.urls import path
from hello import views

urlpatterns = [
    # path("", views.first, name="first.html"),
    #path("Trainee_registration/", views.trainee_registration, name="Trainee_registration.html"),
    path("login/", views.login_get, name="login"),
    #path("trainer_registration/", views.trainer_registration, name="trainer_registration.html"),
    path("trainer_index/", views.trainer_index, name="trainer_index"),
    path("trainer_adding_student/", views.trainer_adding_student, name="trainer_adding_student.html"),
    path("trainer_profile/", views.trainer_profile, name="trainer_profile.html"),
    path("student_index/", views.student_index, name="student_index"),
    path("student_profile/", views.student_profile, name="student_profile.html"),
    path("student_history/", views.student_history, name="student_history.html"),
    #path("trainer_registration/add_trainer/", views.add_trainer, name="add_trainer"),
    #path("Trainee_registration/add_trainee/", views.add_trainee, name="add_trainee"),
    path("registration/", views.registration, name="registration"),
    
    path("registration/add_trainer/", views.add_trainer, name="add_trainer"),
    path("registration/add_trainee/", views.add_trainee, name="add_trainee"),



    path("login/login_user/", views.login_user,name="login_user"),
    path("login/logout/", views.logout_view,name="logout"),
    path("trainer_adding_student/add_student/", views.add_student, name="trainer_adding_student"),
    path('trainer_index/<str:work_student_name>', views.student_name_para, name = 'work_assign.html'),
    path("work_assign/",views.work_assgin,name="work_assign.html"),
    path("trainer_index/add_work/",views.add_work,name="add_work"),
    path("student_index/answer/",views.answer,name="answer"),

]