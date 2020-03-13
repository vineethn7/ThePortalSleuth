from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CategoryModel
from .forms import ReviewForm
# Create your views here.
def home(request):
    return render(request,'PortalSleuthMain/home.html')

def about(request):
    return render(request,'PortalSleuthMain/about.html')

@login_required
def review(request):
    # if applybtn in request.POST:
    #     currentUser=request.user
    #     w=request.POST['websitename']
    #
    #     return render(request,'PortalSleuthMain/postreview',{'w':w})
    # else:
    websites= CategoryModel.objects.all()
    return render(request,'PortalSleuthMain/review.html',{'websites':websites})

@login_required
def post(request):


    form = ReviewForm()
    return render(request, 'PortalSleuthMain/postreview.html', {'form': form})
