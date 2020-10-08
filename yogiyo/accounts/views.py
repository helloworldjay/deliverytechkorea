from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, logout_then_login
from .forms import SignupForm, ProfileForm
from django.contrib import messages


# Create your views here.

login = LoginView.as_view(template_name="accounts/login_form.html") # 로그인 form에서 로그인하는 내장함수

def logout(request):
    messages.success(request, "로그아웃 되었습니다.") # 로그아웃 메세지 전송
    return logout_then_login(request) # 로그아웃시 자동으로 로그인 화면으로 전환

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입 환영합니다.")
            next_url = request.GET.get('next', '/') # next가 존재하면 next로 보내고 없으면 빈 곳으로 보낸다.
            return redirect(next_url) # 회원가입 완료 후 어디로 다시 보낼지 정한다
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })

# 항상 로그인 상황이어야되므로 장식자를 붙여준다, import 필요
@login_required
def profile_edit(request):
    if request.method=='POST':
        form = ProfileForm(request.POST, request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "프로필을 수정/저장했습니다.")
            return redirect("profile_edit")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile_edit_form.html", {
        "form" : form,
    })