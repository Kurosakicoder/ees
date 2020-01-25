from .models import Category
def menu_gallery_links(request):
    gallery_links = Category.objects.all()
    return dict(gallery_links=gallery_links)