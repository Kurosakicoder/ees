from .models import Category
def menu_year_links(request):
    year_links = Category.objects.all()
    return dict(year_links=year_links)