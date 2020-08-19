from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from django.views.generic import ListView
from django.contrib import messages

# Create your views here.
class bookList(ListView):
	model = Book
	template_name = 'shop/list.html'

cart = {}
def insertCart(request, id):
	book = Book.objects.get(id=id)

	if id in cart.keys():
		cart[id] = {
			'id': id,
			'title': book.title,
			'image': str(book.image),
			'price': book.price,
			'quantity': int(cart[id]['quantity']) + 1
		}
		request.session['shopCart'] = cart
		messages.info(request, 'you have add more item in your cart')
	else:
		cart[id] = {
			'id': id,
			'title': book.title,
			'image': str(book.image),
			'price': book.price,
			'quantity': 1
		}
		request.session['shopCart'] = cart
		messages.success(request, 'you have add 1 item in your cart')
	return redirect('shop:bookList')

def viewCart(request):
	cart = request.session.get('shopCart')
	total = 0
	for item in cart.values():
		total += int(item['price']) * int(item['quantity'])
	return render(request, 'shop/viewCart.html', {'cart':cart, 'total':total})

def deleteCart(request, id):
	cart = request.session.get('shopCart')
	cart.pop(str(id), None)

	request.session['shopCart'] = cart
	messages.warning(request, 'you have delete 1 item in your cart')
	return redirect('shop:viewCart')

def updateCart(request):
	id = request.POST['id']
	number = request.POST['number']

	cart = request.session.get('shopCart')
	cart[id]['quantity'] = int(number)
	request.session['shopCart'] = cart
	return redirect('shop:viewCart')