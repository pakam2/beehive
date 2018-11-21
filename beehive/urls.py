"""beehive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hives.views import MainView, AddNewHiveView, HiveList,  DeleteHiveView, AddDataDisplayHives, \
     AddDataHiveOneView, AddDataHiveTwoView, AddDataHiveThreeView, AddDataHiveFourView, \
     HistoricDataListView, ShowDataAllHives, ShowDataHiverOne, ShowDataHiverTwo, ShowDataHiverThree, ShowDataHiverFour, LoginView, SignUp, LogOutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', LoginView.as_view(), name="login"),
    url(r'^logout/', LogOutView.as_view(), name="logout"),
    url(r'^signup/', SignUp.as_view(), name="signup"),
    url(r'^main/$', MainView.as_view(), name="main"),
    url(r'^addNewHive/$', AddNewHiveView.as_view(), name="add-hive"),
    url(r'^listOfHives/$', HiveList.as_view(), name='hive-list'),
    url(r'^deleteHive/(?P<pk>(\d)+)$', DeleteHiveView.as_view(), name="delete-hive"),
    url(r'^displayHives/$', AddDataDisplayHives.as_view(), name="display-hives"),
    url(r'^historicData/$', HistoricDataListView.as_view(), name="show-hive-list"),
    #How data
    url(r'^historicData/(?P<num>(\d)+)/$', ShowDataAllHives.as_view(), name="show-data"),
    url(r'^historicData/(?P<num>(\d)+)/hiver1/$', ShowDataHiverOne.as_view(), name="show-data"),
    url(r'^historicData/(?P<num>(\d)+)/hiver2/$', ShowDataHiverTwo.as_view(), name="show-data"),
    url(r'^historicData/(?P<num>(\d)+)/hiver3/$', ShowDataHiverThree.as_view(), name="show-data"),
    url(r'^historicData/(?P<num>(\d)+)/hiver4/$', ShowDataHiverFour.as_view(), name="show-data"),
    #Add data
    url(r'^addHivesData/(?P<num>(\d)+)/hiver1/$', AddDataHiveOneView.as_view(), name="hive-data-one-add"),
    url(r'^addHivesData/(?P<num>(\d)+)/hiver2/$', AddDataHiveTwoView.as_view(), name="hive-data-two-add"),
    url(r'^addHivesData/(?P<num>(\d)+)/hiver3/$', AddDataHiveThreeView.as_view(), name="hive-data-three-add"),
    url(r'^addHivesData/(?P<num>(\d)+)/hiver4/$', AddDataHiveFourView.as_view(), name="hive-data-four-add"),

]
