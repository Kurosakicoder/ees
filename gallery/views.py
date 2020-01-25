from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Gallery
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def allCategories(request, c_slug=None):
	c_page = None
	gallery_list = None
	if c_slug != None:
		c_page = get_object_or_404(Category,slug=c_slug)
		gallery_list = Gallery.objects.filter(category=c_page)
	else:
		gallery_list = Gallery.objects.all().filter()
	'''Pagination code'''
	paginator= Paginator(gallery_list, 6)
	try:
		page = int(request.GET.get('page','1'))
	except:
		page = 1
	try:
		gallery = paginator.page(page)
	except (EmptyPage,InvalidPage):
		gallery = paginator.page(paginator.num_pages)
	return render(request, 'gallery/category.html',{'category':c_page, 'gallery':gallery})

# def AchieveDetails(request,c_slug,achievements_slug):
# 	try:
# 		achievements = Achievements.objects.get(category__slug=c_slug,slug=achievements_slug)
# 	except Exception as e:
# 		raise e
# 	return render(request,'achievements/achievements.html', {'achievements':achievements})