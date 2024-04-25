from django.shortcuts import render,redirect
from django.views import View
from todoapp.forms import LoginForm,TodoForm,TodoEditForm
from todoapp.models import todoModel
from django.contrib.auth import authenticate,login,logout
from django.views.generic import UpdateView
from django.urls import reverse_lazy

# Create your views here.
class todoView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,'login.html',{'loginform':form})
    def post(self,request,*args,**kwargs):
        uname=request.POST.get('username')
        passw=request.POST.get("password")
        user=authenticate(request,username=uname,password=passw)
        if user:
            login(request,user)
            return redirect("home_view")
        else:
            return redirect('login_view')
        
class TodoCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TodoForm()
        return render(request,'todoenter.html',{'todo_form':form})
    def  post(self,request,*args,**kwargs):
        task=request.POST.get('task')
        description=request.POST.get('description')
        todoModel.objects.create(task=task,description=description,user=request.user)
        return redirect("home_view")

class TodoList(View):
     def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            data=todoModel.objects.filter(user=request.user)
            return render(request,'todolist.html',{'list':data})
        else:
            return redirect('login_view')
        
class Delete(View):
    def get(self,request,*args,**kwargs):
        x=kwargs.get('id')
        data=todoModel.objects.get(id=x)
        data.delete()
        return redirect('detail_todo')

class EditView(UpdateView):
    model=todoModel
    template_name='edit.html'
    pk_url_kwarg='id'
    context_object_name='form'
    form_class=TodoEditForm
    success_url=reverse_lazy('detail_todo')








