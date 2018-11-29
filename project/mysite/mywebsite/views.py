from django.shortcuts import render
from django.http import HttpResponse
from mywebsite.item import Item
from mywebsite.cart import Cart
import sqlite3
import json

# Create your views here.
def Home(request):
	response = HttpResponse()
	html_out = ""
	f = open("home_html.txt")
	for line in f:
		html_out += line
	response.write(html_out)
	return response	

def LogIn(request):
	response = HttpResponse()
	html_out = ""
	f = open("login_html.txt")
	for line in f:
		html_out += line
	response.write(html_out)
	return response

def CartPage(request):	
	response = HttpResponse()
	html_out = ""
	f = open("cart_html.txt")
	for line in f:
		html_out += line
	response.write(html_out)
	return response

def SignUp(request):
	response = HttpResponse()	
	html_out = ""
	f = open("signup_html.txt")
	for line in f:
		html_out += line
	response.write(html_out)
	return response
	
def BatBoard(request):
	response = HttpResponse()	
	html_out = ""
	f = open("bat_board_html.txt")
	for line in f:
		html_out += line
	response.write(html_out)
	return response

def VolJacket(request):
	response = HttpResponse()	
	html_out = ""
	f = open("vol_jacket_html.txt")
	for line in f:
		html_out += line
	response.write(html_out)
	return response

def BurtMittens(request):
	response = HttpResponse()	
	html_out = ""
	f = open("burt_mittens_html.txt")
	for line in f:
		html_out += line
	response.write(html_out)
	return response

def LineSkis(request):
	response = HttpResponse()	
	html_out = ""
	f = open("line_skis_html.txt")
	for line in f:
		html_out += line
	response.write(html_out)
	return response

def VonGoggles(request):
	response = HttpResponse()	
	html_out = ""
	f = open("von_goggles_html.txt")
	for line in f:
		html_out += line
	response.write(html_out)
	return response

def _686Jacket(request):
	response = HttpResponse()	
	html_out = ""
	f = open("686_jacket_html.txt")
	for line in f:
		html_out += line
	response.write(html_out)
	return response

def add_to_cart(request):
	conn = sqlite3.connect('db.sqlite3')
	c = conn.cursor()
	if request.method == 'GET':
		data = request.body.decode('utf-8')
		#c.execute("insert into cart (itemName, quantity) values (\"Burton Mittens\", 2)")
		conn.commit()
	c.close()
	conn.close()
	
	cart = Cart()
	cc = open("current_cart.txt")
	for line in cc:
		cart.add(line[:-1])	
	response = HttpResponse()
	html_out = ""
	f = open("cart_html.txt")
	for line in f:
		if line != "</body>\n" and line != "</html>":
			html_out += line
	for item_ in cart.items:
		html_out += "\t<div class=\"cartItems\">\n\t\t<p style=\"position:absolute; left:50px;\">1 "
		html_out += item_
		html_out += "</p>\n\t\t<p style=\"text-align:center \">remove</p>"
	html_out += "</body>\n</html>"
	response.write(html_out)	
	return response



