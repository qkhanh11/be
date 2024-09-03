"""
URL configuration for be project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/NhomDonVi/',include('NhomDonVi.urls')),
    path('api/CapNhomDonVi/',include('CapNhomDonVi.urls')),
    path('api/DonVi/',include('DonVi.urls')),
    path('api/NhomDoiTuong/',include('NhomDoiTuong.urls')),
    path('api/CapBac_ChucVu/',include('CapBac_ChucVu.urls')),
    path('api/SiQuan/',include('SiQuan.urls')),
    path('api/TheRaVao/',include('TheRaVao.urls')),
    path('api/Khach/',include('Khach.urls')),
    path('api/HocVien/',include('HocVien.urls')),
    path('api/Truc/',include('Truc.urls')),
    path('api/ChienSi/',include('ChienSi.urls')),
    path('api/RaVaoSQ/',include('RaVaoSQ.urls')),
]
