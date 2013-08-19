from django.conf.urls import patterns, include, url


urlpatterns = patterns('movies.views',

    url(r'^moviez/$', 'movies_view', name="moviez"),
    url(r'^moviez/info/(?P<movie_id>\d+)/$', 'movies_info_view', name="moviez_info"),

)
