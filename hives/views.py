from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.views import View
from django.urls import reverse_lazy
from django.http import HttpResponse
from hives.forms import AddHiveForm, HiveDataFormOne, HiveDataFormTwo, HiveDataFormThree, HiveDataFormFour, SignInForm, MySignUpForm
from hives.models import HiveModel, FirstHiveDataModel
from django.db.models import Sum, Max, Count
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
class SignUp(View):

    def get(self, request):
        form = MySignUpForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('/')
        else:
            return HttpResponse("Rejestracja nie powiodła się")

class LoginView(View):

    def get(self, request):
        if request.user.is_authenticated():
            return redirect('/main')
        else:
            ctx = SignInForm()
            return render(request, 'login.html', {'ctx': ctx})

    def post(self, request):
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/main')
        else:
            return HttpResponse("Nie ma takiego użytkownika")

class LogOutView(View):

    def get(self, request):
        messages.info(request, "Wylogowałeś się")
        logout(request)
        return redirect('/')


class MainView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, 'main.html')


class AddNewHiveView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddHiveForm()
        newHiveNumber = HiveModel.objects.all().filter(owner=request.user.id).aggregate(Count('numberOfHive'))
        return render(request, 'add_new_hive.html', {'form': form, 'newHiveNumber': newHiveNumber['numberOfHive__count'] + 1})

    def post(self, request):
        form = AddHiveForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner_id  = request.user.id
            form.numberOfHive = HiveModel.objects.all().filter(owner=request.user.id).aggregate(Count('numberOfHive'))['numberOfHive__count'] + 1
            form.save()
            return redirect('/main')
        else:
            return HttpResponse("Ul o tym numerze już istnieje")
1

class HiveList(LoginRequiredMixin, View):

    def get(self, request):
        form = HiveModel.objects.all().filter(owner=request.user.id)
        return render(request, 'hive_list.html', {'form': form})


class DeleteHiveView(LoginRequiredMixin, DeleteView):

    
    model = HiveModel
    success_url = reverse_lazy('main')
    
 

class AddDataDisplayHives(LoginRequiredMixin, View):

    #Displays list of all hives to which we can add data
    def get(self, request):
        ctx = HiveModel.objects.all().filter(owner=request.user.id)
        return render(request, 'display_hives.html', {'ctx': ctx})

    def post(self, request):
        ctx = HiveModel.objects.all().filter(owner=request.user.id)
        return render(request, 'display_hives.html', {'ctx': ctx})


class AddDataHiveOneView(LoginRequiredMixin, View):

    #Addiing data to a specific hive
    def get(self, request, num):
        form = HiveDataFormOne()
        return render(request, 'add_data_hiver_one.html', {'form': form, 'hive_id': num})

    def post(self, request, num):
        form = HiveDataFormOne(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.hive_id = int(num)
            form.owner = request.user.id
            form.save()
            return render(request,'display_hives.html', {'ctx': HiveModel.objects.all().filter(owner=request.user.id), 'success': 'Data added'} )
        else:
            #For error handling
            return render_to_response('my_template.html', {'form': form})

class AddDataHiveTwoView(LoginRequiredMixin, View):
    
    #Addiing data to a specific hive
    def get(self, request, num):
        form = HiveDataFormTwo()
        # formTwo = HiveDataFormTwo()
        # formFour = HiveDataFormFour()
        # formThree = HiveDataFormThree()
        return render(request, 'add_data_hiver_two.html', {'form': form, 'hive_id': num})

    def post(self, request, num):
        form = HiveDataFormTwo(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.hive_id = int(num)
            form.owner = request.user.id
            form.save()
            return render(request,'display_hives.html', {'ctx': HiveModel.objects.all().filter(owner=request.user.id), 'success': 'Data added'} )
        else:
            #For error handling
            return render_to_response('my_template.html', {'form': form})


class AddDataHiveThreeView(LoginRequiredMixin, View):
    
    #Addiing data to a specific hive
    def get(self, request, num):
        form = HiveDataFormThree()
        return render(request, 'add_data_hiver_three.html', {'form': form, 'hive_id': num})

    def post(self, request, num):
        form = HiveDataFormThree(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.hive_id = int(num)
            form.owner = request.user.id
            form.save()
            return render(request,'display_hives.html', {'ctx': HiveModel.objects.all().filter(owner=request.user.id), 'success': 'Data added'} )
        else:
            #For error handling
            return render_to_response('my_template.html', {'form': form})

class AddDataHiveFourView(LoginRequiredMixin, View):
    
    #Addiing data to a specific hive
    def get(self, request, num):
        form = HiveDataFormFour()
        return render(request, 'add_data_hiver_four.html', {'form': form, 'hive_id': num})

    def post(self, request, num):
        form = HiveDataFormFour(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.hive_id = int(num)
            form.owner = request.user.id
            form.save()
            return render(request,'display_hives.html', {'ctx': HiveModel.objects.all().filter(owner=request.user.id), 'success': 'Data added'} )
        else:
            #For error handling
            return render_to_response('my_template.html', {'form': form})


class HistoricDataListView(LoginRequiredMixin, View):

    #displays a list of hives
    #In this view you can choose a hive and see the statistics
    def get(self, request):
        ctx = HiveModel.objects.all().filter(owner=request.user.id)
        return render(request, 'historic_data.html', {'ctx':ctx})


class ShowDataAllHives(LoginRequiredMixin, View):

    def get(self, request, num):
        #Query gets all data from a chosen hive
        dataOfHive = FirstHiveDataModel.objects.all().filter(hive_id=num)
        return render(request, 'show_data.html', {'hive_id': num, 'dataOfHive': dataOfHive})

class ShowDataHiverOne(LoginRequiredMixin, View):

    def get(self, request, num):
        hiverOneData = FirstHiveDataModel.objects.all().filter(hive_id=num, owner=request.user.id)
        print(hiverOneData)
        return render(request, 'historic_data_hiver_one.html', {'form':hiverOneData})

class ShowDataHiverTwo(LoginRequiredMixin, View):
    pass

class ShowDataHiverThree(LoginRequiredMixin, View):
    pass

class ShowDataHiverFour(LoginRequiredMixin, View):
    pass

