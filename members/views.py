from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    """Try login user.

    Returns:
        If user authenticate go back to home page. If not try again.
    """
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.success(
                request, ("Your login/password is incorrect. Try again.")
            )
            return redirect("login")
    else:
        return render(request, "authenticate/login.html", {})


def logout_user(request):
    """Try logout user.

    Returns:
        Go back to home page.
    """
    logout(request)
    messages.success(request, ("you were logged out."))
    return redirect("home")
