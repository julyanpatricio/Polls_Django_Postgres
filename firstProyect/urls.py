"""firstProyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

    ----------

La lista de rutas 'URLPATTNS` rutea las URLS a las views. Para más información por favor vea:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Ejemplos:
Vistas de función
    1. Agregue una importación: from my_app import views
    2. Agregue una URL a URLPATTNS: path('', views.home, name='home')
Vistas basadas en clase
    1. Agregue una importación:from other_app.views import Home
    2. Agregue una URL a URLPATTNS: path('', Home.as_view(), name='home')
Incluyendo otro urlconf
    1. Importar la función Incluir (): dfrom django.urls import include, path
    2. Agregue una URL a URLPATTNS: path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import path, include


'''La función include() permite hacer referencia a otros URLconfs. Cada vez que Django encuentra include() corta cualquier parte de la URL que coincide hasta ese punto y envía la cadena restante a la URLconf incluida para seguir el proceso.'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
]
