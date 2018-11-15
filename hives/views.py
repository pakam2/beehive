from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse
from django.views import View
from django.http import HttpResponse
from hives.forms import AddHiveForm, HiveDataFormOne, HiveDataFormTwo, HiveDataFormThree, HiveDataFormFour, SignInForm, MySignUpForm
from hives.models import HiveModel, FirstHiveDataModel
from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
class SignUp(View):

    def get(self, request):
        #form = UserCreationForm()
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
            #User.objects.create_user(username="jeden", password="jeden")
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
        logout(request)
        return HttpResponse("Wylogowałeś się")


class MainView(LoginRequiredMixin, View):

    def get(self, request):
        print(request.user.id)
        print(request.user.username)
        return render(request, 'main.html')


class AddHiveView(LoginRequiredMixin, View):
    #View to add a new hive

    def get(self, request):
        form = AddHiveForm()
        return render(request, 'add_hive.html', {'form': form})

    def post(self, request):
        form = AddHiveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/main')
        else:
            return HttpResponse("Ul o tym numerze już istnieje")


class HiveListView( LoginRequiredMixin, View):

    #List of all hives

    def get(self, request):
        ctx = HiveModel.objects.all().filter(owner=request.user.id)
        return render(request, 'hive_list.html', {'ctx': ctx})


class HiveListDetailedView(LoginRequiredMixin, View):

    #Detailed view of a specific hive

    def get(self, request, num):

        hiveInformation = HiveModel.objects.all().filter(numberOfHive=num)
        return render(request, 'detailed.html', {'ul_id': num,
                                                 'ul_info': hiveInformation,})

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


class ShowListOfHives(LoginRequiredMixin, View):

    #displays a list of hives
    #In this view you can choose a hive and see the statistics
    def get(self, request):
        ctx = HiveModel.objects.all().filter(owner=request.user.id)
        return render(request, 'historic_data.html', {'ctx':ctx})


class ShowData(LoginRequiredMixin, View):

    def get(self, request, num):
        #Query gets all data from a chosen hive
        dataOfHive = FirstHiveDataModel.objects.all().filter(hive_id=num)
        return render(request, 'show_data.html', {'hive_id': num, 'dataOfHive': dataOfHive})
