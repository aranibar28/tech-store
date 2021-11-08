from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from core.views import CatalogView, ProductView, KartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CatalogView.as_view()),
    path('catalog/product/<pk>', ProductView.as_view()),
    path('addToCart/', KartView.as_view()),
    path('cart', KartView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
