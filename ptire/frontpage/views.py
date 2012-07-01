# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response


def home(request):
	'''
	Home page 
	'''
		

	#Printing HTML to user
	return render_to_response('base.html',{'title':'matte'})


def carstatus(request):
	'''
	function to get car status
	'''
	if request.GET:
		location=request.GET['location']
	#Printing HTML to user
	request.session["cars"]=location
	'''
	Exempel formatted html to send back to client
	'''
	html = "<car1><tr VALIGN=TOP><td width='130'><img src='/media/img/volvo.jpg' /></td><td width='200'><strong>Volvo v70</strong><br><p>Info of car</p><strong>Price: 1 200:-</strong></td><td><input type='button' value='Book' class='btn btn-primary' onclick='chooseCar();'></td></tr><car1>"
	
	return HttpResponse(html)	
