from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
#from .forms import UserForm
from web.forms import ColorForm
from django.views.generic import FormView

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
#from django.core.context_processors import csrf
from .forms import DJ_user_clientCreationForm


AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'web/login.html')
    else:
        #albums = Album.objects.filter(user=request.user)
        #song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
                Q(album_title__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()
            song_results = song_results.filter(
                Q(song_title__icontains=query)
            ).distinct()
            return render(request, 'web/index.html', {
                #'albums': albums,
                #'songs': song_results,
            })
        else:
            return render(request, 'web/index.html', {})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'web/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
#                albums = Album.objects.filter(user=request.user)
                return render(request, 'web/index.html', {})
            else:
                return render(request, 'web/login.html', {'error_message': 'Su cuenta esta deshabilitada'})
        else:
            return render(request, 'web/login.html', {'error_message': 'Invalid login'})
    return render(request, 'web/login.html')

def mi_perfil_usuario(request):
    if not request.user.is_authenticated():
            return render(request, 'web/login.html')
    else:
       # albums = Album.objects.filter(user=request.user)
       #song_results = Song.objects.all()
#        query = request.GET.get("q")
#        if query:
#           albums = albums.filter(
#                Q(album_title__icontains=query) |
#                Q(artist__icontains=query)
#            ).distinct()
#                song_results = song_results.filter(
#                Q(song_title__icontains=query)
#            ).distinct()
#            return render(request, 'web/index.html', {
#                #'albums': albums,
#                #'songs': song_results,
#            })
#        else:
        #form = UserForm(request.POST or None)
        #context = {
        #    "form": form,
        #}
        user_results = User.objects.all()
        return render(request, 'web/index.html', {user_results})

class ColorFormView(FormView):
    template_name = "web/color_form.html"
    form_class = ColorForm

    def form_valid(self, form):
        color = form.cleaned_data.get("color")
        return HttpResponse("Your color: {0}".format(color))



#def register(request):
#    form = UserForm(request.POST or None)
#    if form.is_valid():
#        user = form.save(commit=False)
#        username = form.cleaned_data['username']
#        password = form.cleaned_data['password']
#        user.set_password(password)
#        user.save()
#        user = authenticate(username=username, password=password)
#        if user is not None:
#            if user.is_active:
#                login(request, user)
#                #albums = Album.objects.filter(user=request.user)
#                return render(request, 'web/index.html', {})
#    context = {
#        "form": form,
#    }
#    return render(request, 'web/register.html', context)

def home(request):
    return render(request, "home.html")


def login(request):
    c = {}
    c.update(csrf(request))    
    return render(request, 'login.html', c)


    
def auth_view(request):
    username = request.POST.get('DJ_user', '')
    password = request.POST.get('DJ_password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
    
    
def loggedin(request):
    return render(request, 'loggedin.html', 
                  {'user': request.user })



def invalid_login(request):
    return render(request, 'invalid_login.html')



def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')



def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    else:
        form = CustomUserCreationForm()
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render(request, 'register.html', args)



def register_success(request):
    return render(request, 'register_success.html')