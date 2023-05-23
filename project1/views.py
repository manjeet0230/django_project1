from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect

def html_page(request):
    return render(request,"index.html")

# def index_page(request):
#     return render(request,"indexpage.html")

# def index_page(request):
#     result=0
#     try:
#         if request.mathod=="POST":
#         #  n1=int(request.GET['num1'])
#         #  n2=int(request.GET['num2'])
#             n1=int(request.POST.get('num1'))
#             n2=int(request.POST.get('num2'))
#             result=(n1+n2);
#             print(result)
#     except:
#         pass
#     return render(request,"indexpage.html",{'output':result})


# This mathod is for get and post mathod in django.
def index_page(request):
    result = 0
    data={}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            result = n1 + n2
            print(result)
            data={
                "n1":n1,
                "n2":n2,
                "output":result
            }

            url="/htmlpage/?output={}".format(result)

            return HttpResponseRedirect('url')


    except (TypeError, ValueError):
        pass
    return render(request, "indexpage.html", {'output': result})
print('my name is manjeet singh rana')