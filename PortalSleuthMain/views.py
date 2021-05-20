from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import CategoryModel
from .forms import ReviewForm,EmojiReviewForm
from .models import ReviewModel,EmojiReviewModel
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
import cv2
from rake_nltk import Rake, Metric
from django.http import StreamingHttpResponse
from PortalSleuthMain.camera import VideoCamera
emoji_dist={0:"PortalSleuthMain/angry.png",1:"PortalSleuthMain/disgusted.png",2:"PortalSleuthMain/fearful.png",3:"PortalSleuthMain/happy.png",4:"PortalSleuthMain/neutral.png",5:"PortalSleuthMain/sad.png",6:"PortalSleuthMain/surpriced.png"}

f=[0,0]
def gen(camera):
    # model=FrameModel
    while True:
        f1 = camera.get_frame()
        frame=f1[0]
        f[1]=f1[1]
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    # print(maxindex)
def livefeed(request):
    cam = VideoCamera()
    return StreamingHttpResponse(gen(cam),content_type="multipart/x-mixed-replace;boundary=frame")


@login_required
def getVideo(request):

    return render(request,'PortalSleuthMain/livefeed.html')

@login_required
def selectFrame(request):
    if request.method=='POST':
        emotion=request.POST['emotionIndex']
        user=request.user
        websiteName="Amazon"
        ins=EmojiReviewModel(emotion=emotion,user=user,websiteName=websiteName)
        ins.save()
        return redirect("submittedEmoji")
    return render(request,'PortalSleuthMain/lastFrame.html',{'emoji':str(f[1])})

@login_required
def submittedEmoji(request):
    m=EmojiReviewModel.objects.last()
    return render(request,"PortalSleuthMain/submittedEmoji.html",{'m':m})

def home(request):
    return render(request,'PortalSleuthMain/home.html')

def contact(request):
    return render(request,'PortalSleuthMain/contact.html')

@login_required
def category(request):
    shoppingSites=CategoryModel.objects.filter(categoryName="Shopping")
    cabSites=CategoryModel.objects.filter(categoryName="Cab Services")
    onlineClass=CategoryModel.objects.filter(categoryName="Online Classes")
    return render(request,'PortalSleuthMain/category.html',{'shoppingSites':shoppingSites,'cabSites':cabSites,'onlineClass':onlineClass})


@login_required
def chooseReview(request):
    return render(request,'PortalSleuthMain/chooseReview.html')


@login_required
def review(request):

    r=Rake(ranking_metric=Metric.DEGREE_TO_FREQUENCY_RATIO)
    reviews=ReviewModel.objects.filter(websiteName='Amazon')
    emojiReviews=EmojiReviewModel.objects.filter(websiteName='Amazon')
    emotionVal=[]
    for e in emojiReviews:
        if e.emotion=="0":
            emotionVal.append("Angry")
        elif e.emotion=="1":
            emotionVal.append("Disgusted")
        elif e.emotion=="2":
            emotionVal.append("Fearful")
        elif e.emotion=="3":
            emotionVal.append("Happy")
        elif e.emotion=="4":
            emotionVal.append("Neutral")
        elif e.emotion=="5":
            emotionVal.append("Sad")
        elif e.emotion=="6":
            emotionVal.append("Surprised")
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
    for i in emotionVal:
        temp=i
        r.extract_keywords_from_text(temp)
        t=r.get_ranked_phrases()
        out.append(t)
    overall_rating=0
    c=0
    for o in out:
        for i in range(0,len(o)):
            c=c+1
            if "Angry" in o[i] or "Fearful" in o[i] or "Sad" in o[i] or "Disgusted" in o[i] or "hate" in o[i] or "not good" in o[i] or "not satisfied" in o[i] or "bad" in o[i] or "dont like" in o[i] or "very bad" in o[i] :
                overall_rating=overall_rating-1
            else:
                overall_rating=overall_rating+1
    overall_rating=round(5*overall_rating/c,2)

    return render(request,'PortalSleuthMain/review.html',{'reviews':reviews,'emojiReviews':emojiReviews,'emotionVal':emotionVal,'out':overall_rating})

# class EmojiReviewCreateView():
#     model=EmojiReviewModel


class EmojiReviewAddedView(DetailView):
    model=EmojiReviewModel
    model=EmojiReviewModel.objects.last()
    success_url="submittedEmoji/"+str(model.pk)

class ReviewDetailView(DetailView):
    model = ReviewModel
# class EmojiReviewDetailView(DetailView):
#     model = EmojiReviewModel
# class EmojiReviewCreateView(LoginRequiredMixin, CreateView):
#     model=EmojiReviewModel
#     # fields=['emotion']
#
#     def form_valid(self,form):
#         form.instance.user=self.request.user
#         form.instance.websiteName="Amazon"
#         # model.objects.update_or_create()
#         return super().form_valid(form)

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model=ReviewModel
    fields=['review']

    def form_valid(self,form):
        form.instance.user=self.request.user
        form.instance.websiteName="Amazon"
        return super().form_valid(form)

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
