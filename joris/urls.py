from django.conf import settings
from django.conf.urls import url, include
from django.views.generic import RedirectView, TemplateView

from django.contrib import admin
from django.conf.urls.static import static


site_patterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('animationfinder.urls'))
]

debug_patterns = []
if settings.DEBUG:
    import debug_toolbar
    debug_patterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]

urlpatterns = debug_patterns + site_patterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




