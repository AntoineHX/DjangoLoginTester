from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, Django!")

from django.views.generic import TemplateView
from django.shortcuts import render
# from django.template import loader
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        # print(kwargs)
        # print('Home get:', request.GET)
        if request.is_ajax():
            print('Ajax request')
            # return return HttpResponseRedirect(reverse_lazy('home'))
            return render(request, self.template_name)
        context = {
            'email': 'bip',
        }
        return self.render_to_response(context)
        # return HttpResponseRedirect(reverse_lazy('home'))
    
    # def post(self, request, *args, **kwargs):
    #     print('Home post:', request.POST)
    #     context = {
    #         'username': 'bip',
    #     }
    #     return self.render_to_response(context)

from django.views.generic import FormView
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,JsonResponse

from .forms import TestForm

class TestFormView(FormView):
    template_name = 'test_form.html'
    form_class = TestForm
    success_url = reverse_lazy('home')
    # success_message = ""

    def dispatch(self, request, *args, **kwargs):
        # print('Ajax:',request.POST)
        self.user=request.user
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(FormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status 
        code along with name of the user
        """
        # Mail update
        email = form.cleaned_data['email']
        update=User.objects.filter(username=self.user).update(email=email)
        assert update==1 #Un seul mail modifier

        response = HttpResponseRedirect(self.success_url)
        #response = JsonResponse({"email": email}, status=200)
        return response

    
    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """
        print('Form invalid :', form)
        errors = form.errors.as_json()
        return JsonResponse({"errors": errors}, status=400)