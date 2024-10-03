from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from main.models import Urlsshort

# @method_decorator(csrf_exempt, name='dispatch')
class SecondPageView(TemplateView):
    template_name = "main/test.html"
    
    def get(self, request, *args, **kwargs):
        context = {}
        link = kwargs["pk"]
        print("проверяю = ", link)
        interal = "https://www.w3schools.com/django/django_create_app.php"
        return redirect(interal)
    
    def post(self, request, *args, **kwargs):
        context = {}
        # print(request.POST['fileName'])
        return render(request, self.template_name, context)