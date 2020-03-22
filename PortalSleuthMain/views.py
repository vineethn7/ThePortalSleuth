from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CategoryModel
from .forms import ReviewForm
from .models import ReviewModel
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from rake_nltk import Rake, Metric

def home(request):
    return render(request,'PortalSleuthMain/home.html')

def about(request):
    return render(request,'PortalSleuthMain/about.html')

@login_required
def review(request):

    r=Rake(ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO)
    reviews=ReviewModel.objects.filter(websiteName='Amazon')

    revs=reviews
    lst=[]
    for k in revs:
        lst.append(str(k.review))

    out=[]
    for i in lst:
        temp=i

        r.extract_keywords_from_text(temp)
        t=r.get_ranked_phrases()
        out.append(t)

    overall_rating=0
    c=0
    for o in out:
        for i in range(0,len(o)):
            c=c+1
            if "bad" in o[i] or "dont like" in o[i] or "very bad" in o[i] :
                overall_rating=overall_rating-1

            else:
                overall_rating=overall_rating+1
    overall_rating=round(5*overall_rating/c,2)


    # overall_rating/=len(max(out,key=len))

    return render(request,'PortalSleuthMain/review.html',{'reviews':reviews,'out':overall_rating})

# class ReviewListView(ListView):
#     model = ReviewModel
#     template_name = 'PortalSleuthMain/review.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'reviews'
#     ordering=['-created_at']


class ReviewDetailView(DetailView):
    model = ReviewModel

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model=ReviewModel
    fields=['review']

    def form_valid(self,form):
        form.instance.user=self.request.user
        form.instance.websiteName="Amazon"
        return super().form_valid(form)
#
#
#
class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ReviewModel
    fields = ['review']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.websiteName="Amazon"
        return super().form_valid(form)

    def test_func(self):
        review = self.get_object()
        if self.request.user == review.user:
            return True
        return False


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ReviewModel
    success_url = '/review'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

# @login_required
# def post(request):
#     if request.method=="POST":
#         reviews=ReviewModel.objects.filter(websiteName="Amazon")
#         form = ReviewForm(request.POST)
#
#         return render(request, 'PortalSleuthMain/postreview.html', {'form': form,'reviews':reviews})
