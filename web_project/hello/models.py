from django.db import models

class Trainermodel(models.Model):
    trainer_fname=models.CharField(max_length=50)
    trainer_lname=models.CharField(max_length=50)
    trainer_email=models.EmailField(max_length=50)
    trainer_phone=models.IntegerField()
    trainer_dob=models.DateTimeField()
    trainer_password=models.CharField(max_length=50)

    def __str__(self):
        return self.trainer_fname+self.trainer_lname


class Traineemodels(models.Model):
    trainee_fname=models.CharField(max_length=50)
    trainee_lname=models.CharField(max_length=50)
    trainee_email=models.EmailField(max_length=50)
    trainee_phone=models.IntegerField()
    trainee_dob=models.DateTimeField()
    trainee_password=models.CharField(max_length=50)

    def __str__(self):
        return self.trainee_fname+self.trainee_lname

class Works(models.Model):
    works_trainer_name=models.CharField(max_length=50)
    works_work_assgin_date=models.DateTimeField(auto_now_add=True)
    works_subject=models.CharField(max_length=100)
    works_question=models.TextField()
    works_work_status=models.BooleanField(default=False)
    works_student_name=models.CharField(max_length=50)
    works_upload_date=models.DateTimeField(null=True)
    works_student_answer=models.TextField(default=False)

    def __str__(self):
        return self.works_trainer_name+" "+self.works_student_name
        
class Adding(models.Model):
    add_trainer_name=models.CharField(max_length=50)
    add_student_name=models.CharField(max_length=50)
    add_student_phone=models.IntegerField()
    
    def __str__(self):
        return self.add_trainer_name