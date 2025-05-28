from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, "helloapp/index.html")

@csrf_exempt
def greet_post(request):
    if request.method == "POST":
        name = request.POST["name"]
        return render(request, "helloapp/greet.html", {
            "name": name.capitalize()
        })
    return render(request, "helloapp/index.html")
