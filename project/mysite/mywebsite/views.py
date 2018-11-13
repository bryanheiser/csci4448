from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
	response = HttpResponse()
	html_out = ""
	f = open("home_html.txt")
	for line in f:
		html_out += line
	#html_out = '<div style="width: 100vw; height: 100px; background:MidnightBlue"><header style="padding: 20px; text-align: center; font-size: 40px;' 
	#html_out += 'color: white; font-family: "Helvetica", sans-serif;">Capita</header><h3 style="position: absolute; top: 15px; right: 150px"><a style="color:white; text-decoration:none" href="login/">Log In</a></h3>'	
	#html_out += '<h3 style="position: absolute; top: 15px; right: 50px"><a style="color:white; text-decoration:none" href="cart/">Your Cart</a></h3>'
	#html_out += '<h3 style="position: absolute; top: 15px; right: 230px"><a style="color:white; text-decoration:none" href="signup/">Sign Up</a></h3></div>'
	#html_out += '<body style="background: LightBlue; margin: 0;">'
	#html_out += '<h1 style="padding: 20px; text-align: center; font-family: "Helvetica", sans-serif;">'
	#html_out += 'Check Out Our Newest Winter Gear!</h1>'
	response.write(html_out)
	return response	

def LogIn(request):
	response = HttpResponse()
	html_out = '<div style="width: 100vw; height: 100px; background:MidnightBlue">'		
	html_out += '<header style="padding: 20px; text-align: center; font-size: 40px;' 
	html_out += 'color: white; font-family: "Helvetica", sans-serif;">Capita</header>'
	html_out += '<h3 style="position: absolute; top: 15px; left: 40px"><a style="color:white; text-decoration:none" href="">Home</a></h3></div>'
	html_out += '<body style="background: LightBlue; margin: 0;">'
	html_out += '<h3 style="padding: 35px;"></h3>'
	html_out += '<form style="text-align: center;"><h3 style="text-align: center; font-family: "Helvetica", sans-serif;">'
	html_out += 'Email:</h3>'
	html_out += '<input type="text" name="email">'
	html_out += '<h3 style="text-align: center; font-family: "Helvetica", sans-serif;">'
	html_out += 'Password:</h3>'
	html_out += '<input type="text" name="password"></form>'
	html_out += '<div style="text-align: center"><button type="button">Log In</button></div>'
	response.write(html_out)
	return response

def Cart(response):	
	response = HttpResponse()
	html_out = '<div style="width: 100vw; height: 100px; background:MidnightBlue">'		
	html_out += '<header style="padding: 20px; text-align: center; font-size: 40px;' 
	html_out += 'color: white; font-family: "Helvetica", sans-serif;">Capita</header>'
	html_out += '<h3 style="position: absolute; top: 15px; left: 40px"><a style="color:white; text-decoration:none" href="">Home</a></h3></div>'
	html_out += '<body style="background: LightBlue; margin: 0;">'
	html_out += '<h1 style="padding: 10px; text-align: left; font-family: "Helvetica", sans-serif;">'
	html_out += 'Your Cart</h1>'
	html_out += '<p style="padding: 10px; font-size: 30px">Items</p></body>'
	response.write(html_out)
	return response

def SignUp(response):
	response = HttpResponse()	
	html_out = '<div style="width: 100vw; height: 100px; background:MidnightBlue">'		
	html_out += '<header style="padding: 20px; text-align: center; font-size: 40px;' 
	html_out += 'color: white; font-family: "Helvetica", sans-serif;">Capita</header>'
	html_out += '<h3 style="position: absolute; top: 15px; left: 40px"><a style="color:white; text-decoration:none" href="">Home</a></h3></div>'
	html_out += '<body style="background: LightBlue; margin: 0;">'
	html_out += '<h1 style="padding: 10px; text-align: center; font-family: "Helvetica", sans-serif;">'
	html_out += 'Sign Up</h1>'
	html_out += '<form style="text-align: center;"><h3 style="text-align: center; font-family: "Helvetica", sans-serif;">'
	html_out += 'Email:</h3>'
	html_out += '<input type="text" name="email">'
	html_out += '<h3 style="text-align: center; font-family: "Helvetica", sans-serif;">'
	html_out += 'Password:</h3>'
	html_out += '<input type="text" name="password">'
	html_out += '<h3 style="text-align: center; font-family: "Helvetica", sans-serif;">'
	html_out += 'Re-Enter Password:</h3>'
	html_out += '<input type="text" name="password1"></form>'
	html_out += '<div style="text-align: center"><button type="button">Sign Up</button></div>'
	response.write(html_out)
	return response
