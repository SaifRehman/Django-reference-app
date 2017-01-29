from django.shortcuts import render

# Create your views here.
def Home(request):
    context = locals()
    template = "home.html"
    return render(request, context, template)