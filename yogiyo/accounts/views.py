from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "회원가입 환영합니다.")
            next_url = request.GET.get('next', '/') # next가 존재하면 next로 보내고 없으면 빈 곳으로 보낸다.
            return redirect(next_url) # 회원가입 완료 후 어디로 다시 보낼지 정한다
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })
