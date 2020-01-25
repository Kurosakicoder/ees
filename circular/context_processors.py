from .models import Category
def menu_circular_links(request):
    circular_links = Category.objects.all()
    return dict(circular_links=circular_links)