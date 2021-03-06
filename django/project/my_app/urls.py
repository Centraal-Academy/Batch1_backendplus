from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^base/$', views.BaseView.as_view(), name="base"),
    url(r'^template/$', views.HomeTemplateView.as_view(), name="template"),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.PersonDetailView.as_view(), name="detail"),
    url(r'^list/$', login_required(views.PersonList.as_view()), name="list"),
    url(r'^create/$', views.PersonCreate.as_view(), name="create"),
    url(r'^update/(?P<pk>[0-9]+)/$', views.PersonUpdate.as_view(), name="update"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.PersonDelete.as_view(), name="delete"),
    url(r'^form/$', views.ContactFormView.as_view(), name="form"),
    url(r'^formset/$', views.EventPersonFormset, name="formset"),
    url(r'^search/$', views.Search, name="search"),
    url(r'^search/ajax/$', views.search_name, name="search_name"),
    url(r'^graphql/$', GraphQLView.as_view(graphiql=True)),
    
]
