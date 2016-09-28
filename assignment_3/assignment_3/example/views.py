from django.shortcuts import render
from django.utils.html import escape
import datetime

from .forms import SubmissionForm
from .models import submissions


# Create your views here.
def index(request):
    form = SubmissionForm()
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd['submission'])
            print(len(cd['submission']))
            suggestList = submissions.objects.filter(topic=escape(cd['submission']))
            if not suggestList.exists():
                suggested = submissions(
                    date=datetime.datetime.now(),
                    topic=escape(cd['submission']))
                suggested.save()
    lis = []
    suggestList = submissions.objects.all()
    for s in suggestList:
        lis += [s.topic]
    context = {
        'page_name':"Example",
        "submissions":lis,
        'form':form
        }
    return render(request,'example.html',context)
