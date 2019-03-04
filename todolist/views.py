from django.shortcuts import render,redirect#render渲染,redirect重定向

# Create your views here.

lis=[{'待办事项':'学习','已完成':False},{'待办事项':'吃饭','已完成':True},]


def home(request):
    global lis
    if request.method == "POST":
        if request.POST["待办事项"] == '':
            content = {"清单": lis,'警告':'请输入内容!'}
            return render(request,'todolist/home.html',content)
        else:
            lis.append({"待办事项":request.POST["待办事项"],'已完成':False})
            content={"清单":lis,'信息':'添加成功!'}
            return render(request,'todolist/home.html',content)
    elif request.method == "GET":
        content = {"清单": lis}
        return render(request, 'todolist/home.html', content)
def about(request):
    return render(request,'todolist/about.html')


def edit(request,forloop_counter):
    global lis
    if request.method == "POST":
        if request.POST["已修改事项"] == '':
            return render(request, 'todolist/edit.html', {'警告': '请输入内容!'})
        else:
            lis[int(forloop_counter) - 1]["待办事项"]=request.POST["已修改事项"]
            return redirect('todolist:主页')
    elif request.method == "GET":
        content = {"待修改事项": lis[int(forloop_counter)-1]["待办事项"]}
        return render(request,'todolist/edit.html',content)



def delete(request,forloop_counter):
    lis.pop(int(forloop_counter)-1)
    return redirect('todolist:主页')

def cross(request,forloop_counter):
    if request.POST['完成状态']=='已完成':
        lis[int(forloop_counter) - 1]['已完成']=True
    else:
        lis[int(forloop_counter) - 1]['已完成'] = False

    return redirect('todolist:主页')

