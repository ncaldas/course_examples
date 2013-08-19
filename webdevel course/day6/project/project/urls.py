from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^project/', include('project.foo.urls')),

    url(r'^hello/(?P<name>\w+)/(?P<year>\d{4})/', 'hello.views.hello_view'),
    url(r'^sum/(?P<x>-?\d+)/(?P<y>-?\d+)', 'hello.views.sum_view'),
    url(r'^grade/(?P<x>-?\d+)/', 'hello.views.grade_view'),
    url(r'^sort/(?P<l>\d+(,-?\d+)*)/', 'hello.views.sort_view'),
    url(r'^now/', 'hello.views.now_view'),
    url(r'^code/$', 'hello.views.code_view'),
    url(r'^hosts/$', 'hello.views.hosts_view'),
    url(r'^temperature/(?P<n>-?\d+)/', 'hello.views.temperature_view'), #it is important here to make sure the group "n" is defined so that the browser url will be able to take on the variable n which is defined in the function
    url(r'^percentage/(?P<x>\d+)/(?P<y>\d+)', 'hello.views.current_percentage'),
#    url(r'^dna/(?P<d>[ATCG]{4}*)/', 'hello.views.dna_view'),
    #the [] the elements inside however many times (or 0) ; ALSO the url is set up like this the dna/(this part is teh grouping which is the list of ACTG/
    url(r'^date/(?P<y>((19)|(20)\d{2}))/(?P<m>(0[1-9]|1[0-2]))/(?P<d>(0[1-9]|[1-2][0-9]|3[0-1]))', 'hello.views.date_view'),
    url(r'^average/(?P<username>\w+)/', 'hello.views.averagegrades_view'),
    url(r'^login/$', 'hello.views.login_view'),
    url(r'^html/$', 'hello.views.html_view'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    )
