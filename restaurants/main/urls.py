from django.urls import path
from .views import register, export_view, import_view

urlpatterns = [
    path('register', register, name="register"),
    path('export', export_view, name="export"),
    path('import', import_view, name="import")
]
