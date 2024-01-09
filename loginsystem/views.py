from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from . import models
from django.urls import reverse


def Logout(request):
    logout(request)
    return redirect(reverse('home'))

def checkIfUserNameAvailable(name):
    return User.objects.filter(username=name).exists()

# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request,"home.html")
    
class UserRegister(View):
    def get(self, request, *args, **kwargs):
        return render(request,"user_register.html")
    
    def post(self, request, *args, **kwargs):
        post_data = request.POST

        # check if email is already registered
        username = post_data.get('username')
        email = post_data.get('email')
        password = post_data.get('pass')
        repass = post_data.get('repass')

        fname = post_data.get('fname')
        lname = post_data.get('lname')
        phone = post_data.get('phone')
        address = post_data.get('address')

        city = post_data.get("city")
        state = post_data.get("state")
        pincode = post_data.get("pincode")

        profile_pics = post_data.get('profileimage')
        if self.checkIfEmailDoesNotExist(email):
            # email is already registered abort registration
            return render(request,"user_register.html" ,{"error_message":"Email is already registered" , "data":{"fname":fname,"lname":lname,"phone":phone,"address":address,"email":email, "city":city,"state":state,"pincode":pincode} })
        elif checkIfUserNameAvailable(username):
            return render(request,"user_register.html" ,{"error_message":"username already taken" , "data":{"fname":fname,"lname":lname,"phone":phone,"address":address,"email":email, "city":city,"state":state,"pincode":pincode} })
        elif repass.strip() != password.strip():
            return render(request,"user_register.html" ,{"error_message":"Password and retyped did not matched." , "data":{"fname":fname,"lname":lname,"phone":phone,"address":address,"email":email,"city":city,"state":state,"pincode":pincode} })
        
        else:
            new_user = User.objects.create(
                first_name = fname,
                last_name = lname,
                username = username,
                email  = email,
                password = password
            )
            # new_user.is_staff = True
            new_user.save()

            # saving extra details in Patient model
            newP = models.Patient.objects.create(
                user = new_user,
                phone = phone,
                address = address,
                profile_picture = profile_pics,
                city = city,
                state = state,
                pincode = pincode
            )
            newP.save()

            # user = authenticate(request, username=email, password=password)
            # print(user)
            login(request, new_user)
            return redirect(reverse("user_dashboard"))
            # email is not registered proceed registration
        
    
    def checkIfEmailDoesNotExist(self, email):
        return User.objects.filter(email=email).exists()



         



class DoctorRegister(View):
    def get(self, request, *args, **kwargs):
        return render(request,"doctor_register.html")


    def post(self, request, *args, **kwargs):
        post_data = request.POST

        # check if email is already registered
        username = post_data.get('username')
        email = post_data.get('email')
        password = post_data.get('pass')
        repass = post_data.get('repass')

        fname = post_data.get('fname')
        lname = post_data.get('lname')
        phone = post_data.get('phone')
        address = post_data.get('address')

        city = post_data.get("city")
        state = post_data.get("state")
        pincode = post_data.get("pincode")

        profile_pics = post_data.get('profileimage')

        if self.checkIfEmailDoesNotExist(email):
            # email is already registered abort registration
            return render(request,"user_register.html" ,{"error_message":"Email is already registered" , "data":{"fname":fname,"lname":lname,"phone":phone,"address":address,"email":email, "city":city,"state":state,"pincode":pincode} })
        elif checkIfUserNameAvailable(username):
            return render(request,"user_register.html" ,{"error_message":"username already taken" , "data":{"fname":fname,"lname":lname,"phone":phone,"address":address,"email":email, "city":city,"state":state,"pincode":pincode} })
        elif repass.strip() != password.strip():
            return render(request,"user_register.html" ,{"error_message":"Password and retyped did not matched." , "data":{"fname":fname,"lname":lname,"phone":phone,"address":address,"email":email,"city":city,"state":state,"pincode":pincode} })
        
        else:
            new_user = User.objects.create(
                first_name = fname,
                last_name = lname,
                username = username,
                email  = email,
                password = password
            )
            new_user.is_staff = True
            new_user.save()

            # saving extra details in Patient model
            newD = models.Doctor.objects.create(
                user = new_user,
                phone = phone,
                address = address,
                profile_picture = profile_pics,
                city = city,
                state = state,
                pincode = pincode
            )
            newD.save()

            # user = authenticate(request, username=email, password=password)
            # print(user)
            login(request, new_user)
            return redirect(reverse("doctor_dashboard"))
            # email is not registered proceed registration
    
    def checkIfEmailDoesNotExist(self, email):
        return User.objects.filter(email=email).exists()
    

class Login(View):

    def get(self, request, *args, **kwargs):
        return render(request,"login.html")

    def post(self, request, *args, **kwargs):
        #doctor login >> staff status -true
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect("../../doctor/dashboard")
            else:
                #user is patients redirect to patient dashboard
                return redirect("../../user/dashboard")
        else:
            return render(request,"login.html", {'username': username,"error_message":"Invalid username or password"})
    

class DoctorDashboard(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    # redirect_field_name = "redirect_to"

    def get(self, request, *args, **kwargs):
        return render(request,"doctor_dashboard.html")

    
class UserDashboard(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    def get(self, request, *args, **kwargs):
        return render(request,"patient_dashboard.html")