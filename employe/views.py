from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import *
from django.views.generic import UpdateView

# Create your views here.

def Home(request):
    return render(request,'home.html')

def Resister_emp(request):
    err=''
    if request.method=='POST':
        f_n=request.POST.get('f_n')
        l_n=request.POST.get('l_n')
        ec=request.POST.get('ec')
        email=request.POST.get('email')
        p=request.POST.get('p')

        try:
            user=User.objects.create_user(first_name=f_n,last_name=l_n,username=email,password=p)
            Employe.objects.create(user=user,Ecode=ec)
            err='no'
            return redirect('/')
        except:
            err='yes'

    return render(request,'resister_emp.html',locals())

def Emp_list(request):
    e=Employe.objects.all()
    e1={'data':e}
    return render(request,'emp_list.html',e1)

def Emp_login(request): 
    if request.method=='POST':
        u=request.POST.get('email')
        p=request.POST.get('p')
        user=authenticate(User,username=u,password=p)
        try:
            if user  is not None:
                request.session['uid']=user.id
                login(request,user)
                err='no'
                return redirect('/emp_profile')
        except:
            err='yes'            
    return render(request,'emp_login.html',locals())

def Logout_view(request):
    logout(request)
    return redirect('/')

def Emp_Home(request):
    if not request.user.is_authenticated:
        return redirect('/employe_login')
    user=request.user
    e=Employe.objects.get(user=user)
    
    return render(request,'emp_home.html',locals())

def Emp_profile(request):    
    err=''
    user=request.user
    emp=Employe.objects.get(user=user)
    if request.method=='POST':
        f_n=request.POST.get('f_n')
        l_n=request.POST.get('l_n')
        ec=request.POST.get('ec')
        email=request.POST.get('email')
        dig=request.POST.get('dig')
        dept=request.POST.get('dpt')
        gender=request.POST.get('gen')
        con=request.POST.get('con')
        jd=request.POST.get('jdate')
        pic=request.FILES.get('pic')
        dob=request.POST.get('dob')


        emp.user.first_name=f_n
        emp.user.last_name=l_n
        emp.user.username=email
        emp.Ecode=ec
        emp.dig=dig
        emp.dept=dept
        emp.gender=gender
        emp.dob=dob
        emp.img=pic
        emp.join_data=jd
        emp.contact=con

        try:
            emp.save()
            emp.user.save()
            err='no'
            pro='yes'
            
            return redirect('/emp_home_dashboard')
        except:
            err='yes'
     
    return render(request,'emp_profile.html',locals())


def Emp_view(request):
    try:
        user=request.user
        e=Employe.objects.get(user=user)
        return render(request,'emp_profile_dt.html',locals())
    except:
        return redirect('/')
    

    
class Update_Emp(UpdateView):
    model=Employe
    template_name='emp_update.html'
    fields=['gender','dob','dept','contact','dig','join_data']
    success_url='/emp_home_dashboard'


def Emp_Education(request):    
    user=request.user
    emp=Employe.objects.get(user=user)
    if  request.method=='POST':
        add=request.POST.get('add')
        first_edu=request.POST.get('f_e_1')
        first_col=request.POST.get('f_e_name1')
        first_p_year=request.POST.get('f_p_1')

        sec_edu=request.POST.get('f_e_2')
        sec_col=request.POST.get('f_e_name2')
        sec_p_year=request.POST.get('f_p_2')

        thrd_edu=request.POST.get('f_e_3')
        thrd_col=request.POST.get('f_e_name3')
        thrd_p_year=request.POST.get('f_p_3')

        ed=Emp_Edu()
        ed.user=user
        
        ed.address=add

        ed.first_edu=first_edu
        ed.first_col=first_col
        ed.first_p_year=first_p_year

        ed.sec_edu=sec_edu
        ed.sec_col=sec_col
        ed.sec_p_year=sec_p_year

        ed.thrd_edu=thrd_edu
        ed.thrd_col=thrd_col
        ed.thrd_p_year=thrd_p_year

        try:
            ed.save()
            return redirect('/emp_home')

        except:
            return redirect('/emp_profile')
    return render(request,'emp_education.html')


def Emp_Education_detail(request):
    try:
        user=request.user
       
        e=Emp_Edu.objects.filter(user=user).first()
        return render(request,'emp_education_dt.html',locals())
    except:
        return redirect('/emp_home_dashboard')

    
class Edu_Update_Emp(UpdateView):
    model=Emp_Edu
    template_name='emp_edu_update.html'
    fields=['first_edu','first_p_year','first_col','sec_edu','sec_p_year','sec_col','thrd_edu','thrd_p_year','thrd_col']
    success_url='/emp_home_dashboard'


def Emp_exp(request):
    user=request.user
    emp=Employe.objects.get(user=user)
    if  request.method=='POST':
        jt1=request.POST.get('jt1')
        en1=request.POST.get('cn1')
        yoe1=request.POST.get('yoe1')

        jt2=request.POST.get('jt2')
        en2=request.POST.get('cn2')
        yoe2=request.POST.get('yoe2')

        jt3=request.POST.get('jt3')
        en3=request.POST.get('cn3')
        yoe3=request.POST.get('yoe3')
        
        ed=Emp_Exp()
        ed.user=user
        

        ed.job_title1=jt1
        ed.company1=en1
        ed.years1=yoe1

        ed.job_title2=jt2
        ed.company2=en2
        ed.years2=yoe2

        ed.job_title3=jt3
        ed.company3=en3
        ed.years3=yoe3       
        try:
            ed.save()
            return redirect('/emp_home')

        except:
            return redirect('/emp_home_dashboard')
    return render(request,'emp_exp.html')


def Emp_Exp_detail(request):
    try:
        user=request.user    
        e1=Emp_Exp.objects.filter(user=user).first()
        return render(request,'emp_exp_dt.html',locals())
    except:
        return render(request,'emp_home.html')
       
    
def Leave_request_form(request):
    user=request.user
    emp=Employe.objects.get(user=user)
    if request.method=='POST':
        ltype=request.POST.get('ltype')
        lstartdate=request.POST.get('lstartdate')
        lenddate=request.POST.get('lenddate')
        purpos=request.POST.get('purpos')

        e=Leave_user()
        e.user=user
        e.ltype=ltype
        e.lstartdate=lstartdate
        e.lenddate=lenddate
        e.purpos=purpos
        try:
            e.save()
            return redirect('/leave_r_dt')
        except:
            return redirect('/emp_home_dashboard')       
    return render(request,'leave_r_form.html')

def Leave_detail(request):
    try:
        user=request.user    
        e1=Leave_user.objects.filter(user=user)

        return render(request,'leave_detail.html',{'dt':e1})
    except:
        return render(request,'emp_home.html')

def dashboard(request):
    try:
        user=request.user  
        e=Employe.objects.get(user=user) 
        e1=Leave_user.objects.filter(user=user)
    except:
        return render(request,'emp_dashboard.html')

    return render(request,'dashboard.html',{'dt':e,'dt1':e1})


   
class Edu_Exp_Emp(UpdateView):
    model=Emp_Exp
    template_name='emp_exp_update.html'
    fields=['job_title1','company1','years1','job_title2','company2','years2','job_title3','company3','years3']
    success_url='/emp_home_dashboard'
