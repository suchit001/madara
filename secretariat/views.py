from django.shortcuts import render, redirect

# Create your views here.
from project.models import project_details, sec_details
from student.models import Std_details
from users.models import CustomUser


def secretariat_dashboard(request):
    return render(request,'secretariat_dashboard/sec_dashboard.html')

def secretariat_profile(request, ):
    sec = sec_details.objects.filter(sec_id__in=CustomUser.objects.filter(username=request.user.username))
    # sec = sec_details.objects.all()
    print(sec)
    sec = sec[0]
    context = {
        'sec': sec
    }
    return render(request, 'secretariat_dashboard/sec_profile.html', context)

def secretariat_director_review(request):
    project = project_details.objects.all()
    context = {
        'project':project,
    }
    return render(request,'secretariat_dashboard/sec_director_review.html',context)

def secretariat_irb_review(request):
    project = project_details.objects.all()
    context = {
        'project':project,
    }
    return render(request,'secretariat_dashboard/sec_irb_review.html',context)

def secretariat_final_review(request):
    project = project_details.objects.all()
    context = {
        'project':project,
    }
    return render(request,'secretariat_dashboard/sec_final_review.html',context)






def upstatdr(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 3
    std.save()
    return redirect('secretariat:secretariat_director_review')

def upstatirbr(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 3
    std.save()
    return redirect('secretariat:secretariat_director_review')

def upstatfin(request,pk):
    std = Std_details.objects.get(pk=pk)
    std.st_project_status = 10
    std.save()
    return redirect('secretariat:secretariat_director_review')