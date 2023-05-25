from django.shortcuts import render, get_object_or_404, redirect
from .forms import RegisterForm
from django.contrib.auth import get_user_model




def mypagedeail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk = pk)
    context = {
        'user':user
    }
    return render(request, 'detail.html', context)

def update(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('/')
    return render(request, 'update.html')


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
         user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form': user_form})




