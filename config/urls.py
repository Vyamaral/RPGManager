from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from fichas import views

urlpatterns = [
    # =====================
    # ADMIN
    # =====================
    path('admin/', admin.site.urls),

    # =====================
    # APP PRINCIPAL (CRUD)
    # =====================
    path('', include('fichas.urls')),

    # =====================
    # LOGIN MANUAL (CORRIGIDO)
    # =====================
    path('login/', views.login_view, name='login'),

    # =====================
    # LOGOUT
    # =====================
    path('logout/', views.logout_view, name='logout'),

    # =====================
    # CADASTRO
    # =====================
    path('cadastro/', views.cadastro, name='cadastro'),
]

# =====================
# MEDIA (DESENVOLVIMENTO)
# =====================
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )