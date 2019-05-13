from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm                # Eliminated once we got forms.py and .forms import as below
from django.contrib import messages         # for flash message
from django.shortcuts import redirect       # to redirect the user to different page after creating account
from .forms import UserRegisterForm
from django.contrib.auth.decorators  import login_required

from .forms import UserUpdateForm, ProfileUpdateForm            # imported models so that we can pass them to view below - profile update purpose
# Create your views here.

def register(request):
    if request.method == 'POST':
        print("Request method identified:",request.method)
        form = UserRegisterForm(request.POST)
        #form.save()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Send a flash message
            messages.success(request, f'Hey {username}, your account has been created!')
            return redirect('login')   # parameter is name from the url patterns for a page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

# @login_required(login_url='login')
@login_required
def profile(request):

    if request.method == "POST":
        # For Update view - And the arguments over here are the references to the objects of user and profile which will come in handy to present original data which user may want to update
        u_form = UserUpdateForm(request.POST, instance=request.user)                                  # Instance of the UserUpdateForm() class
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)         # Instance of the ProfileUpdateForm() class
        # requst.post is needed here, request.Files is needed to handle multipart arguments
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Hey {request.user.username}, your account has been updated!')
            return redirect('profile')   # this is the new request without any context so even on reload no new post request will be made to update the records
    else:
        u_form = UserUpdateForm(instance=request.user)                                  # Instance of the UserUpdateForm() class
        p_form = ProfileUpdateForm(instance=request.user.profile)                        # Instance of the ProfileUpdateForm() class

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)