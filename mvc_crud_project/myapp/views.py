from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    return render(request, 'myapp/index.html')

def register(request):
    return render(request, 'myapp/studentform.html')

def studentform_data(request):
    if request.method == 'POST':
        btn = request.POST.get('btn')

        if btn=="Submit":
            sname=request.POST.get('sname')
            slocation=request.POST.get('slocation')
            semail=request.POST.get('semail')
            sage=request.POST.get('sage')
             
            #condition for salary 
            try:
                sage = int(sage)
            except(ValueError, TypeError):
                return render(request,'myapp/studentform.html',{
                    'msg': '❌ Age must be a number!',
                    'msg_type': 'error'
                })
            
            if sage <= 0:
                return render(request,'myapp/studentform.html',{
                    'msg':'❌ Age must be a positive number!',
                    'msg_type':'error'
                })
            
            #check for duplicate email
            if Student.objects.filter(semail=semail).exists():
                return render(request,'myapp/studentform.html',{
                    'msg': '❌ This email is already exist!',
                    'msg_type': 'error'
                })

            Student.objects.create(
                sname=sname,
                slocation=slocation,
                semail=semail,
                sage=sage
            )

            return render(request,'myapp/studentform.html',{
                'msg': '✅ Student added successfully!',
                'msg_type': 'success'
            })

        if btn=="Display":
            data = Student.objects.all()
            dic = {'data':data}
            return render(request, 'myapp/studentform.html', dic)
        
    else:
        return render(request,'myapp/studentform.html',{
            'msg': '⚠️ Something went wrong!',
            'msg_type': 'error'
            })
    
def studentdata_delete(request):
    sid = request.GET.get('sid')
    try:
        Student.objects.filter(sid=sid).delete()
    except Student.DoesNotExist:
        return render(request,'myapp/studentform.html',{'delete_msg': '⚠️ Something went wrong!', 'delete_msg_type': 'error'})
    return render(request,'myapp/studentform.html',{'delete_msg': '✅ Record Deleted Successfully...', 'delete_msg_type': 'success'})

def student_data(request):
    sid = request.GET.get('sid')
    try:
        record=Student.objects.get(sid=sid)
        param={'data':record}
    except Student.DoesNotExist:
        return render(request,'myapp/studentform.html',{'delete_msg': '⚠️ Something went wrong!', 'delete_msg_type': 'error'})
    return render(request,'myapp/studentdata_edit.html',param)

def studentdata_edit(request):
    if request.method == 'POST':
        btn = request.POST.get('btn')
        if btn == 'Update':
            sid=request.POST.get('sid')
            sname=request.POST.get('sname')
            slocation=request.POST.get('slocation')
            semail=request.POST.get('semail')
            sage=request.POST.get('sage')
            try:
                record=Student.objects.get(sid=sid)
                if sname != "":
                    record.sname=sname
                if slocation != "":
                    record.slocation=slocation
                if semail != "":
                    record.semail=semail
                if sage != "":
                    record.sage=sage
                record.save()
                return render(request,'myapp/studentform.html',{'delete_msg':'✅ Record Updated Successfully...','delete_msg_type':'success'})
            except Student.DoesNotExist:
                return render(request,'myapp/studentdata_edit.html',{'msg':'⚠️ Something went wrong!','msg_type':'error'})