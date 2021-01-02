from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from .forms import SignUpForm
from .models import Profile


# Create your views here.
#
# def signup(request):
#     return HttpResponse('he is risen')
#




def loginpage(request):
    context={
        'SignUpForm':SignUpForm,
             }

    return render(request, 'login.html',context)


def signuppage(request):
    return render(request, 'signup.html')



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})









def signup(request):
    if request.method == "POST":
        email = request.POST.get('email', False)
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phone=request.POST['phone']
        password = request.POST['password1']
        confirm_password = request.POST['password2']


        # if re.fullmatch(r'[A-Za-z0-9]{8,}', password):

        if password == confirm_password:

            if User.objects.filter(email=email).exists():

                messages.warning(request, 'Email exists!')
                return render(request, 'signup.html')


            else:
                user = User.objects.create_user(email=email, username=email,first_name=firstname,last_name=lastname, password=password
                                                )
                user.save()
                messages.success(request, 'Account created sucessfully!')
                user.refresh_from_db()
                user=Profile(phone=phone)
                user.save()
                user = authenticate(username=email, password=password)
                login(request, user)

                # send_mail(
                #     'Account creation',
                #     'Hello,welcome to the Maskani family. Your account creation was successful.Should you have any queries just send us an email or call our customer care numbers. here is a guide to get you started',
                #     'firstregapp@gmail.com',
                #     [email],
                #     fail_silently=True,
                #
                # )

                print("sign up sucessful")

                return redirect('/')
        # else:
        # return HttpResponse('invalid email')
        else:
            messages.info(request, 'Passwords do not match!')
            return render(request,'signup.html')
        # else:
        #     return HttpResponse('password must contain charachters,numbers and uppercase letters')

    else:
        return render(request,'signup.html')

def login_function (request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)

        user =auth.authenticate( email = email, password = password)

        if user is not None:
            login(request, user)
            return redirect('/')


        else:
            messages.warning(request, 'Incorrect username/password!')
            # return render(request, 'login.html')
            return render(request, 'login.html')



    else:

        return render(request,'login.html')




def logout_view(request):
    logout(request)
    return redirect('/')



def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():









        user = form.save()
        user.refresh_from_db()
        # user.profile.first_name = form.cleaned_data.get('first_name')
        # user.profile.last_name = form.cleaned_data.get('last_name')
        # user.profile.email = form.cleaned_data.get('email')
        user.profile.phone = form.cleaned_data.get('phone')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user = authenticate(username=username, password=password)
        login(request, user)
        print('signup successfull')
        return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
