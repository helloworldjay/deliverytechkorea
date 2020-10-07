from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', login_required(TemplateView.as_view(template_name='root.html')), name='root'), # login이 되어있을때만 진입 가능
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
    path('__debug__/', include(debug_toolbar.urls)),
]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    