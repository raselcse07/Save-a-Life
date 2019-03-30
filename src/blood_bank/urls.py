from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path
from donor.views import (
                        PersonCreateView,
                        load_ps,
                        home_page,
                        search_result
                    )


urlpatterns = [
    path('', home_page,name="home"),
    path('admin/', admin.site.urls),
    path('register/', PersonCreateView.as_view(),name="register"),
    path('search/', search_result,name="search-result"),
    path('ajax/load-dist/', load_ps, name='ajax_load_ps'),
    path('eligibility/', TemplateView.as_view(template_name="eligibility.html"),name="eligibility"),
    path('contact/', TemplateView.as_view(template_name="contact.html"),name="contact"),

]

if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
