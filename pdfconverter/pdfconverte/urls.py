"""
URL configuration for pdfconverte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from converter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('signin/', views.signin,name='signin'),
    path('auth/', include('social_django.urls', namespace='social')), 
    path('forgot-password/', views.forgot_password, name='forgot_password'), 
    path('Contact_Us/',views.contact_us, name='contact_us'),
    path('add_page/',views.add_page_number,name='add_page_number'),
    path('merge/',views.merge,name='merge'),
    path('remove/',views.remove,name='remove'),
    path('rotate/',views.rotate,name='rotate'),
    path('word_to_pdf/',views.word_to_pdf,name='word_to_pdf'),
    path('pdf_to_word/',views.pdf_to_word,name='pdf_to_word'),
    path('excel_to_pdf/',views.excel_to_pdf,name='excel_to_pdf'),
    path('pdf_to_excel/',views.pdf_to_excel,name='pdf_to_excel'),
    path('ppt_to_pdf/',views.ppt_to_pdf,name='ppt_to_pdf'),
    path('pdf_to_ppt/',views.pdf_to_ppt,name='pdf_to_ppt'),
    path('jpg_to_pdf/',views.jpg_to_pdf,name='jpg_to_pdf'),
    path('pdf_to_png/',views.pdf_to_png,name='pdf_to_png'),


]

