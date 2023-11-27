from basic import  views as basic_views
from django.urls import  path

urlpatterns = [
    path("", basic_views.home, name="home"),
    path("about/", basic_views.about, name="about"),
    path("contact/", basic_views.contact, name="contact"),
    path("services/", basic_views.services, name="services"),
    path("team/", basic_views.team, name="team"),
    path("portfolio/", basic_views.portfolio, name="portfolio"),
    path("faq/", basic_views.faq, name="faq"),
    path("subscribe/", basic_views.subcribe, name="subscribe"),
    path("join-fan-network/", basic_views.join_network, name="join_network"),
    path("join-fan-network-second/", basic_views.join_network_sc, name="join_network_sc"),
    path("join-fan-network-third/", basic_views.join_network_th, name="join_network_th"),
    path("join-fan-network-ms/", basic_views.join_network_ms, name="join_network_ms"),
    path("update_network/", basic_views.update_network, name="update_network"),
    path('cities/', basic_views.autocomplete, name='autocomplete'),


]