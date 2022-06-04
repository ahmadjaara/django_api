from django.urls import path
from app.api.viewset import ObjectsdetailApiView ,ObjectsListApiView

urlpatterns =[
    path("api/v1/things-list",ObjectsListApiView.as_view(),name="objects_list"),
    path("api/v1/<int:pk>",ObjectsdetailApiView.as_view(),name="objects_list")
]   