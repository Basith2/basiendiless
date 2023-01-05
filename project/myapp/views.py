from django.shortcuts import render
from datetime import datetime
# Create your views here.
from django.db.models import Max
from .models import user_login

def base(request):
    p = college_details.objects.all()
    context = {'p': p}
    return render(request, './myapp/base.html', context)
def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')

from django.http import HttpResponse
def no_page(request):
    return HttpResponse('<center>'
                        '<H2 style="color:#ff2929;">Sorry.</H2>'
                        '<H1 style="color:blue;">No Page Exists.</H>'
                        '</center>')


######################################------ADMIN------##########################################
def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)

def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        if npasswd == cpasswd:
            try:
                ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
                if ul is not None:
                    ul.passwd=npasswd
                    ul.save()
                    context = {'msg': 'Password Changed'}
                    return render(request, './myapp/admin_changepassword.html', context)
                else:
                    context = {'msg': 'Password Not Changed'}
                    return render(request, './myapp/admin_changepassword.html', context)
            except user_login.DoesNotExist:
                context = {'msg': 'Password Err Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        else:
            context = {'msg': 'Check New Password and Confirm Password'}
            return render(request, './myapp/admin_changepassword.html', context)

    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)



from . models import event_details
def admin_event_details_add(request):
    if request.method == 'POST':
        ename = request.POST.get('ename')
        description = request.POST.get('description')
        dt = request.POST.get('dt')
        tm = request.POST.get('tm')
        pic = request.FILES['pic']
        fs = FileSystemStorage()
        pic_path = fs.save(pic.name, pic)

        ed = event_details(ename=ename, description=description, pic_path=pic_path, dt=dt, tm=tm)
        ed.save()
        context = {'msg':'Event Details Added'}
        return render(request, 'myapp/admin_event_details_add.html',context)
    else:
        return render(request, 'myapp/admin_event_details_add.html')

def admin_event_details_view(request):
    ed = event_details.objects.all()
    context = {'event_list':ed}
    return render(request, 'myapp/admin_event_details_view.html',context)

def admin_event_details_delete(request):
    eid = request.GET.get('id')
    e = event_details.objects.get(id=int(eid))
    e.delete()
    ed = event_details.objects.all()
    context = {'event_list':ed,'msg':'Event Details Deleted.'}
    return render(request, 'myapp/admin_event_details_view.html',context)


def admin_event_details_edit(request):
    if request.method == 'POST':
        eid = request.POST.get('eid')
        ename = request.POST.get('ename')
        description = request.POST.get('description')
        dt = request.POST.get('dt')
        tm = request.POST.get('tm')

        e = event_details.objects.get(id=int(eid))
        e.ename = ename
        e.description = description
        e.dt = dt
        e.tm = tm
        e.save()
        context = {'msg':'Details Updated','ed': e, 'eid': eid}
        return render(request, 'myapp/admin_event_details_edit.html', context)

    else:
        eid = request.GET.get('id')
        e = event_details.objects.get(id=int(eid))
        context = {'ed': e,'eid':eid}
        return render(request, 'myapp/admin_event_details_edit.html', context)

from . models import event_pics
def admin_event_pics_add(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        pic = request.FILES['document']
        fs = FileSystemStorage()
        pic_path = fs.save(pic.name, pic)

        ep = event_pics(event_id=event_id,pic=pic_path)
        ep.save()

        context = {'event_id': event_id,'msg':'Pic Added.'}
        return render(request, 'myapp/admin_event_pics_add.html', context)

    else:
        event_id = request.GET.get('event_id')
        context = {'event_id': event_id}
        return render(request, 'myapp/admin_event_pics_add.html', context)

def admin_event_pics_view(request):
    event_id = request.GET.get('id')
    ep = event_pics.objects.filter(event_id=int(event_id))
    context = {'event_id': event_id,'pic_list':ep}
    return render(request, 'myapp/admin_event_pics_view.html', context)

def admin_event_pics_delete(request):
    pid = request.GET.get('id')
    ep1 = event_pics.objects.get(id=int(pid))
    ep1.delete()
    msg = 'Picture Removed'
    event_id = request.GET.get('event_id')
    ep = event_pics.objects.filter(event_id=int(event_id))
    context = {'event_id': event_id,'pic_list':ep,'msg':msg}
    return render(request, 'myapp/admin_event_pics_view.html', context)



from . models import college_details
def admin_add_college_details(request):
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        contact = request.POST.get('contact')
        url = request.POST.get('url')
        email = request.POST.get('email')
        cd = college_details(c_name=c_name, addr=addr, pin=pin, contact=contact, url=url, email=email)
        cd.save()
        return render(request, './myapp/admin_add_college_details.html')
    else:
        return render(request, './myapp/admin_add_college_details.html')

def admin_college_details_update(request):
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        contact = request.POST.get('contact')
        fax = request.POST.get('fax')
        url = request.POST.get('url')
        email = request.POST.get('email')
        cd = college_details.objects.get(id=1)
        cd.c_name=c_name
        cd.addr=addr
        cd.pin=pin
        cd.contact=contact
        cd.url=url
        cd.email=email
        cd.save()
        context = {'msg':'Profile Updated'}
        #return render(request, './myapp/admin_add_college_details.html',context)
        return admin_college_details_view(request)
    else:
        try:
            cd = college_details.objects.get(id=1)
            context = {'cd':cd}
            return render(request, './myapp/admin_college_details_update.html',context)
        except:
            msg = "Add College Details First!"
            context = {'msg':msg}
            return render(request, './myapp/admin_college_profile_view.html', context)



def admin_college_details_view(request):
    cd = college_details.objects.all()
    try:
        cp = college_profile_pic.objects.get(id=1)
        context = {'college_details': cd, 'pic': cp.pic_path}
    except:
        context ={'college_details':cd}
    return render(request, './myapp/admin_college_profile_view.html',context)

from . models import college_profile_pic
def admin_college_profile_pic_add(request):
    if request.method =='POST':
        pic = request.FILES['pic']
        fs = FileSystemStorage()
        pic_path = fs.save(pic.name, pic)
        cp = college_profile_pic(pic_path=pic_path)
        cp.save()
        return render(request, './myapp/admin_college_profile_pic_add.html')
    else:
        return render(request, './myapp/admin_college_profile_pic_add.html')

def admin_college_profile_pic_update(request):
    if request.method =='POST':
        pic = request.FILES['pic']
        fs = FileSystemStorage()
        pic_path = fs.save(pic.name, pic)
        cp = college_profile_pic.objects.get(id=1)
        cp.pic_path = pic_path
        cp.save()
        return admin_college_details_view(request)
    else:
        return render(request, './myapp/admin_college_profile_pic_update.html')

def admin_alumni_details_view(request):
    al_l = alumni_details.objects.all()
    context = {'alumni_list':al_l}
    return render(request, './myapp/admin_alumni_details_view.html',context)

from . models import branch_details
def admin_branch_details_add(request):
    if request.method == 'POST':
        branch_name = request.POST.get('branch_name')
        branch_code = request.POST.get('branch_code')
        bd = branch_details(branch_name=branch_name, branch_code=branch_code)
        bd.save()
        context = {'msg':'Branch Details Added'}
        return render(request, './myapp/admin_branch_details_add.html',context)
    else:
        return render(request, './myapp/admin_branch_details_add.html')

def admin_branch_details_view(request):
    b_l = branch_details.objects.all()
    context = {'branch_list':b_l}
    return render(request, './myapp/admin_branch_details_view.html', context)

def admin_branch_details_edit(request):
    if request.method == 'POST':
        branch_id = request.POST.get('branch_id')
        branch_name = request.POST.get('branch_name')
        branch_code = request.POST.get('branch_code')
        bd = branch_details.objects.get(id=branch_id)
        bd.branch_name = branch_name
        bd.branch_code = branch_code
        bd.save()
        context = {'msg':'Branch Details Updated','branch_id':branch_id, 'bd':bd}
        return render(request, './myapp/admin_branch_details_edit.html',context)
    else:
        branch_id = request.GET.get('id')
        bd = branch_details.objects.get(id=branch_id)
        context = {'branch_id':branch_id, 'bd':bd}
        return render(request, './myapp/admin_branch_details_edit.html', context)

def admin_branch_details_delete(request):
    branch_id = request.GET.get('id')
    bd = branch_details.objects.get(id=branch_id)
    bd.delete()

    b_l = branch_details.objects.all()
    context = {'branch_list':b_l, 'msg':'Branch Deleted'}
    return render(request, './myapp/admin_branch_details_view.html', context)

###############################################ALUMNI###############################################
def alumni_login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='alumni')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            user_id = request.session['user_id']
            ud = alumni_details.objects.get(user_id=int(user_id))
            ap = alumni_posts.objects.all().order_by('-id')

            ad = alumni_details.objects.all()


            context = {'uname': request.session['user_name'], 'ud': ud, 'post_list': ap,'al_list': ad}
            return render(request, 'myapp/alumni_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/alumni_login.html',context)
    else:
        return render(request, 'myapp/alumni_login.html')


def alumni_home(request):
    user_id = request.session['user_id']
    ap = alumni_posts.objects.all().order_by('-id')
    ud = alumni_details.objects.get(user_id=int(user_id))
    ad = alumni_details.objects.all()
    context = {'uname':request.session['user_name'],'ud':ud,'post_list': ap,'al_list': ad}
    return render(request,'./myapp/alumni_home.html',context)


def alumni_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return alumni_login(request)
    else:
        return alumni_login(request)

from django.core.files.storage import FileSystemStorage
from . models import alumni_job
from . models import alumni_details
def alumni_details_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')

        pic = request.FILES['pic']
        id_pic = request.FILES['id_pic']
        fs = FileSystemStorage()
        pic_path = fs.save(pic.name, pic)
        id_pic_path = fs.save(id_pic.name, id_pic)

        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        branch_id = request.POST.get('branch_id')
        pass_year = request.POST.get('pass_year')
        tab = request.POST.get('tab')
        job_title = request.POST.get('job_title')
        org_name = request.POST.get('org_name')
        org_addr = request.POST.get('org_addr')
        org_pin = request.POST.get('org_pin')

        password = request.POST.get('pwd')
        uname=email
        #status = "new"
        if gender == None:
            b_l = branch_details.objects.all()
            context = {'branch_list': b_l, 'val1':"Select Gender"}

            return render(request, 'myapp/alumni_details_add.html', context)


        ul = user_login(uname=uname, passwd=password, u_type='alumni')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']
        print('user_id....................',user_id)
        ud = alumni_details(user_id=user_id,name=name, gender=gender, dob=dob, branch_id=branch_id,pass_year=pass_year, addr=addr, pin=pin, pic=pic_path, id_pic=id_pic_path, contact=contact, email=email )
        ud.save()

        if tab == 'Yes':
            aj = alumni_job(user_id=user_id,job_title=job_title, org_name=org_name, org_addr=org_addr, pin=org_pin)
            aj.save()
        else:
            pass


        print(user_id)
        context = {'msg': 'user registered'}
        return render(request, 'myapp/alumni_login.html',context)

    else:
        b_l = branch_details.objects.all()
        context = {'branch_list':b_l}

        return render(request, 'myapp/alumni_details_add.html',context)


def alumni_details_edit(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')


        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        uname=email
        #status = "new"

        ul = user_login.objects.get(id=int(user_id))
        ul.uname=uname
        ul.save()


        ud = alumni_details.objects.get(user_id=int(user_id))
        ud.name=name
        ud.gender=gender
        ud.dob=dob
        ud.addr=addr
        ud.pin=pin

        ud.contact=contact
        ud.email=email
        ud.save()


        print(user_id)
        ud = alumni_details.objects.get(user_id=int(user_id))
        context = {'msg': 'Details Updated','ud': ud}
        return render(request, 'myapp/alumni_details_edit.html',context)

    else:
        user_id = request.session['user_id']
        ud = alumni_details.objects.get(user_id=int(user_id))
        context = {'uname': request.session['user_name'], 'ud': ud}
        return render(request, './myapp/alumni_details_edit.html',context)






def alumni_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/alumni_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/alumni_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/alumni_changepassword.html', context)
    else:
        return render(request, './myapp/alumni_changepassword.html')

def alumni_alumni_details_search(request):
    if request.method == 'POST':
        pass_year = request.POST.get('pass_year')
        al_name = request.POST.get('al_name')
        branch_id = int(request.POST.get('branch_id'))
        print('branch_id = ',branch_id)
        if branch_id == 0:
            al_list = alumni_details.objects.filter(name__contains=al_name, pass_year__contains=pass_year)
        else:
            al_list = alumni_details.objects.filter(name__contains=al_name, pass_year__contains=pass_year,branch_id=branch_id)
        branch_list = branch_details.objects.all()
        context = {'al_list':al_list, 'branch_list': branch_list}
        return render(request, './myapp/alumni_alumni_details_view.html', context)
    else:
        branch_list = branch_details.objects.all()
        context = {'branch_list': branch_list}
        return render(request, './myapp/alumni_alumni_details_search.html', context)



def alumni_alumni_details_view(request):
    return render(request, './myapp/alumni_alumni_details_view.html')


def alumni_job_details_view(request):
    user_id = request.session['user_id']
    j_l = alumni_job.objects.filter(user_id=user_id)
    context = {'j_list':j_l}
    return render(request, './myapp/alumni_job_details_view.html', context)


def alumni_job_details_delete(request):
    id = request.GET.get('id')
    jl = alumni_job.objects.filter(id=id)
    jl.delete()
    msg = 'Job Details Deleted'
    user_id = request.session['user_id']
    j_l = alumni_job.objects.filter(user_id=user_id)
    context = {'j_list':j_l, 'msg':msg}
    return render(request, './myapp/alumni_job_details_view.html', context)


def alumni_job_details_add(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        job_title = request.POST.get('job_title')
        org_name = request.POST.get('org_name')
        org_addr = request.POST.get('org_addr')
        pin = request.POST.get('org_pin')
        aj = alumni_job(user_id=user_id, job_title=job_title, org_name=org_name, org_addr=org_addr, pin=pin)
        aj.save()
        j_l = alumni_job.objects.filter(user_id=user_id)
        msg = 'New Job Details Added'
        context = {'j_list':j_l, 'msg':msg}
        return render(request, './myapp/alumni_job_details_view.html', context)
    else:
        return render(request, './myapp/alumni_job_details_add.html')



def alumni_job_details_edit(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        user_id = request.session['user_id']
        job_title = request.POST.get('job_title')
        org_name = request.POST.get('org_name')
        org_addr = request.POST.get('org_addr')
        pin = request.POST.get('org_pin')

        jl = alumni_job.objects.get(id=id)
        jl.job_title=job_title
        jl.org_name=org_name
        jl.org_addr=org_addr
        jl.pin=pin
        jl.save()

        msg = ' Job Details Updated'
        context = {'msg':msg, 'jl':jl}
        return render(request, './myapp/alumni_job_details_edit.html', context)
    else:
        id = request.GET.get('id')
        jl = alumni_job.objects.get(id=id)
        context = {'jl':jl}
        return render(request, './myapp/alumni_job_details_edit.html',context)

def alumni_event_details_view(request):
    ev_l = event_details.objects.all().order_by('-id')
    context = {'event_list':ev_l}
    return render(request, './myapp/alumni_event_details_view.html', context)


def alumni_event_pics_view(request):
    event_id = request.GET.get('id')
    ep = event_pics.objects.filter(event_id=int(event_id))
    context = {'event_id': event_id,'pic_list':ep}
    return render(request, 'myapp/alumni_event_pics_view.html', context)


from . models import alumni_posts
def alumni_posts_add(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        title = request.POST.get('title')

        pic = request.FILES['pic']
        fs = FileSystemStorage()
        pic_path = fs.save(pic.name, pic)

        descr = request.POST.get('descr')

        ap = alumni_posts(alumni_id=user_id, title=title, pic_path=pic_path, descr=descr)
        ap.save()
        msg = 'POST ADDED'
        context = {'msg':msg}
        return render(request, './myapp/alumni_posts_add.html', context)
    else:
        return render(request, './myapp/alumni_posts_add.html')

def alumni_posts_delete(request):
    id = request.GET.get('id')
    p = alumni_posts.objects.get(id=id)
    p.delete()
    msg = 'Post Removed'
    user_id = request.session['user_id']
    ap = alumni_posts.objects.filter(alumni_id=user_id).order_by('-id')
    context = {'post_list': ap, 'msg':msg}
    return render(request, './myapp/alumni_posts_view.html', context)

def alumni_posts_view(request):
    user_id = request.session['user_id']
    ap = alumni_posts.objects.filter(alumni_id=user_id).order_by('-id')
    context = {'post_list':ap}
    return render(request, './myapp/alumni_posts_view.html', context)


def alumni_posts_all_view(request):
    user_id = request.session['user_id']
    ap = alumni_posts.objects.all().order_by('-id')
    ad = alumni_details.objects.all()
    context = {'post_list':ap,'al_list':ad}
    return render(request, './myapp/alumni_posts_all_view1.html', context)







def alumni_profile_view(request):
    try:
        id = request.GET.get('id')
        ul = alumni_details.objects.get(id=id)
        post_list = alumni_posts.objects.filter(alumni_id=ul.user_id)
        j_list = alumni_job.objects.filter(user_id=ul.user_id)
        bd = branch_details.objects.get(id=ul.branch_id)
        al = alumni_details.objects.all()
        context = {'post_list': post_list, 'j_list': j_list, 'ul': ul, 'bd': bd, 'al_list': al}
        return render(request, './myapp/alumni_profile_view.html', context)
    except:
        id = request.GET.get('id')
        ul = alumni_details.objects.get(id=id)
        post_list = alumni_posts.objects.filter(alumni_id=ul.user_id)
        j_list = alumni_job.objects.filter(user_id=ul.user_id)
        #bd = branch_details.objects.get(id=ul.branch_id)
        al = alumni_details.objects.all()
        context = {'post_list': post_list, 'j_list': j_list, 'ul': ul, 'al_list': al}
        return render(request, './myapp/alumni_profile_view.html', context)



def alumni_profile_pic_update(request):
    if request.method == 'POST':
        user_id = request.session['user_id']
        pic = request.FILES['new_pic']
        fs = FileSystemStorage()
        pic_path = fs.save(pic.name, pic)
        pd = alumni_details.objects.get(user_id=user_id)
        pd.pic = pic_path
        pd.save()

        # user_id = request.session['user_id']
        ud = alumni_details.objects.get(user_id=int(user_id))
        context = {'uname': request.session['user_name'], 'ud': ud}
        return render(request, './myapp/alumni_details_edit.html', context)

    else:
        return render(request, './myapp/alumni_profile_pic_update.html')






def no_result(request):
    return render(request, './myapp/no_result.html')



