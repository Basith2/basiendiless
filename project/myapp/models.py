from django.db import models

# Create your models here.
class user_login(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id},{self.uname}'

class alumni_details(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    pic = models.CharField(max_length=500)
    id_pic = models.CharField(max_length=500)
    branch_id = models.IntegerField()
    pass_year = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    dob = models.CharField(max_length=100)
    addr = models.CharField(max_length=500)
    pin = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    def __str__(self):
        return f'{self.user_id},{self.email}'



class alumni_job(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    job_title = models.CharField(max_length=100)
    org_name = models.CharField(max_length=100)
    org_addr = models.CharField(max_length=100)
    pin = models.IntegerField()



class college_details(models.Model):
    id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=100)
    addr = models.CharField(max_length=500)
    pin = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    email = models.CharField(max_length=25)

class college_profile_pic(models.Model):
    pic_path = models.CharField(max_length=100)


class event_details(models.Model):
    id = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    pic_path = models.CharField(max_length=130)
    dt = models.CharField(max_length=30)
    tm = models.CharField(max_length=30)

class event_pics(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.IntegerField()
    pic = models.CharField(max_length=200)

class branch_details(models.Model):
    branch_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=30)


class alumni_posts(models.Model):
    title = models.CharField(max_length=100)
    alumni_id = models.IntegerField()
    pic_path = models.CharField(max_length=100)
    descr = models.CharField(max_length=200)

