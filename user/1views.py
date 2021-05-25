# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from qna.forms import SignupForm
# def signup(request):
#     """signup
#     to register users
#     """
#     if request.method == "POST":
#         signupform = SignupForm(request.POST)
#         if signupform.is_valid():
#             user = signupform.save(commit=False)
#             user.email = signupform.cleaned_data['email']
#             user.save()

#         elif request.method == "GET":
#             signupform = SignupForm()
#         return render(request, "registration/signup.html", {
#         "signupform": signupform,
#         })
