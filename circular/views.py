from django.shortcuts import render, get_object_or_404, redirect
from .models import Circular, Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.
# def circular(request):    
#     circular = Circular.objects.all()
#     template = 'circular/circular.html'
#     context = {
#         'circular': circular
#     }
#     return render(request, template, context)

def circular(request, c_slug=None):
	c_page = None
	circular_list = None
	if c_slug != None:
		c_page = get_object_or_404(Category,slug=c_slug)
		circular_list  = Circular.objects.filter(category=c_page)
	else:
		circular_list  = Circular.objects.all().filter()
	'''Pagination code'''
	paginator= Paginator(circular_list , 6)
	try:
		page = int(request.GET.get('page','1'))
	except:
		page = 1
	try:
		circular = paginator.page(page)
	except (EmptyPage,InvalidPage):
		circular = paginator.page(paginator.num_pages)
	return render(request, 'circular/circular.html',{'category':c_page, 'circular':circular})