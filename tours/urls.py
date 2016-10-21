from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tours.views import delete_tour, add_tour, touroperator_tour, TourListView

urlpatterns = [
    url('^details$', TourListView.as_view(template_name='tour_list'), name='tour_list'),
    url('^add_tour$', add_tour, name='add_tour'),
    url('^touroperator_tour$', touroperator_tour, name='touroperator_tour'),
    url(r'^delete_tour/(?P<cur_id>\d+)/$', delete_tour, name='delete_tour'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
