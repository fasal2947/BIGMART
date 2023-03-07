from django.urls import path
from websiteapp import views
urlpatterns = [
    path('Homepage/', views.Homepage, name="Homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('blogpage/', views.blogpage, name="blogpage"),
    path('discategory/<itemCatg>', views.discategory, name="discategory"),
    path('prodcsingle/<int:dataid>', views.prodcsingle, name="prodcsingle"),
    path('savecontactadmin/', views.savecontactadmin, name="savecontactadmin"),
    path('loginregister/', views.loginregister, name="loginregister"),
    path('saveregister/', views.saveregister, name="saveregister")

]