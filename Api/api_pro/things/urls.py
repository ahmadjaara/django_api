from django.urls import URLPattern, path
from things.api.viewset import ThingsListApiView ,ThingsdetailApiView

urlpatterns =[
    path("api/v1/things-list",ThingsListApiView.as_view(),name="things_list"),
    path("api/v1/<int:pk>",ThingsdetailApiView.as_view(),name="things_list")
]   