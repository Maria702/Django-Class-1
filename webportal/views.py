

from django.http import HttpResponse


def index(request):
    return HttpResponse(
        "<center>  <h1 style='color: blue'>Hello</h1> </center>"
        "<center>  <h2> Welcome to the home Page </h2> </center>"
        "<center> <h3> This is Mariya </h3></center>" 
        "<center>Go to <a href='/about/'>About</a> </center>"
        ) 



def about(request):
    return HttpResponse( 
        """ 
        <center><h1 style='color: blue' >Welcome to About Page</h1> 
        <h3 > My self Mariya<br>
        I am a student of Saylani Mass IT Programming<br>
        And This is my first web<br>
        Thank You sir Nasir.. Thanks alot...</h3>
        </center> 

        <center>Go to <a href='/'>Home</a> </center>
        """ 
        ) 


    