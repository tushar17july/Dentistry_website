from django.shortcuts import render,HttpResponse
from datetime import datetime
from dentistry.models import Query
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def index(request):
    jon1={
    "variable1":"Hello",
    "variable2":"world"
    }
    return render(request,'index.html',jon1)

def pricing(request):
    return render(request,'pricing.html')

def services(request):
    return render(request,'product.html')

def contact(requests):
    if requests.method=="POST":
        # firstName=requests.POST.get('getrow')
        lastName=requests.POST.get('lastName')
        email=requests.POST.get('email')
        phone=requests.POST.get('phone')
        Feedback=requests.POST.get('Feedback')
        firstName=requests.POST['firstName']
        
        query=Query(F_name=firstName,L_name=lastName,email=email,Phone=phone,Query=Feedback,Date=datetime.today())
        query.save()
        return render(requests,'Contact_us.html')
    else:
        return render(requests,'Contact_us.html')