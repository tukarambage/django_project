from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse("""<h1>Hey I am a Django Server.</h1>
                        <p> Hey this is from django server</p>
                        <hr>
                        <h3 style="color:red"> Hope you are loving it :) <h3>
                        """)
                    

def success_page(request):
    print("*"*10)
    return HttpResponse("<h1> Hey this is a success page</h1>")
