from django.urls import path
from .views import *
urlpatterns = [
    path('',RegionView.as_view(),name="regions"),
    path('region/<int:pk>/vnzs/', VnzListView,name="vnzs"),
    path('vnz/<int:pk>/specialties',SpecListView, name="specialties"),
    path('specialty/<int:pk>/',SpecView, name="abits"),
    path('statistic/',get_statistic_for_region,name="stat"),
    path('spec/',get5Specilaties,name="top5spec"),
    path('students/',statistic_for_polygon,name="statistic"),
    path('doc/',doc,name="doc"),
    path('help/',help,name='help')


    # path('v/',vns),
    # path('delete/',Delete),
    # path('add/',addvnzs),
    # path('spec/',addspec,)

]