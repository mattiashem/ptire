# Create your views here.

from django.http import HttpResponse,Http404
from django.template.loader import get_template
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

def pro(request,pro):
	'''
	Function to print pro page.
	Takes argumnet and if page is creted in templare dir shows page.
	If now page is created raise 404 error.
	'''
	try: 
		get_template(pro+"/index.html")
		'''
		template is located and printed to user
		'''
		
	
	except:
		'''
		No template raise 404
		'''
		raise Http404()


	render_to_response(pro+'/index.html',{'title':pro})		

	