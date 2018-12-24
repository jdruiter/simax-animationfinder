from django.conf.urls import url
from animationfinder import views

urlpatterns = [

    # http://localhost:8000/get-animations/{"sentence": "We saw her duck. She loves ducks."}
    url(r'^get-animations/(.*)', views.get_animations, name='get_animations'),

    # http://localhost:8000/
    url(r'^$', views.welcome, name='welcome'),

]
