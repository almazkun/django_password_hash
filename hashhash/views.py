from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


@csrf_exempt
def create_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username)
        user.set_password(password)
        user.save()

        from_db_user = User.objects.get(username=username)
        print("\nFrom post:", username, password)
        print("From DB:", from_db_user.username, from_db_user.password, "\n")

    return redirect("/")


@csrf_exempt
def create_user_form(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            from_db_user = User.objects.get(username=form.data.get("username"))
            print("\nFrom post:", form.data.get("username"), form.data.get("password1"))
            print("From DB:", from_db_user.username, from_db_user.password, "\n")

            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "home.html", {"form": form})
