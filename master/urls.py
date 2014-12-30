from django.conf.urls import patterns, url


urlpatterns = patterns('master.views',
    # Examples:
    # url(r'^$', 'acadereg.views.home', name='home'),
     url(r'^home/$',"view_home", name="index"),
    
)
