from django.shortcuts import render,redirect,HttpResponse#render渲染,redirect重定向
from .models import Todo
from django.contrib.auth.models import User
# Create your views here.



def home(request):
    if request.method == "POST":
        if request.POST["待办事项"] == '':
            content = {"清单": Todo.objects.filter(用户=request.user),'警告':'请输入内容!'}
            return render(request,'todolist/home.html',content)
        else:
            # request.user.username

            a_row = Todo(用户=request.user,thing=request.POST['待办事项'])
            a_row.save()
            content={"清单":Todo.objects.filter(用户=request.user),'信息':'添加成功!'}
            return render(request,'todolist/home.html',content)
    elif request.method == "GET":
        #content = {"清单": Todo.objects.all()}

        content = {"清单": Todo.objects.filter(用户=request.user)}
        print(content)
        return render(request, 'todolist/home.html', content)


def about(request):
    return render(request,'todolist/about.html')


def edit(request,每一件事_id):
    global lis
    if request.method == "POST":
        if request.POST["已修改事项"] == '':
            return render(request, 'todolist/edit.html', {'警告': '请输入内容!'})
        else:
            a = Todo.objects.get(id=每一件事_id)
            a.thing = request.POST["已修改事项"]
            a.save()
            return redirect('todolist:主页')
    elif request.method == "GET":
        a = Todo.objects.get(id=每一件事_id)
        content = {"待修改事项": a.thing}
        return render(request,'todolist/edit.html',content)



def delete(request,每一件事_id):
    a= Todo.objects.get(id=每一件事_id)
    a.delete()
    return redirect('todolist:主页')

def cross(request,每一件事_id):
    if request.POST['完成状态']=='已完成':
        a = Todo.objects.get(id=每一件事_id)
        a.done=True
    else:
        a = Todo.objects.get(id=每一件事_id)
        a.done = False
    a.save()
    return redirect('todolist:主页')

def timeing(request,每一件事_id):

    a= Todo.objects.get(id=每一件事_id)
    b= int(request.POST['计时状态'])
    if b>1051982140862:
        b=0
    print(a.work_time,'+',b)
    a.work_time += b
    wm = a.work_time

    s, w = divmod(wm, 1000)
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    a.格式化秒="%02d:%02d:%02d" % (h, m, s)
    a.save()
    # 1
    return redirect('todolist:主页')

