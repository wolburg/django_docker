from rest_framework.routers import DefaultRouter
from .views import (
    UsuarioViewSet,
    CourseViewSet,
    LessonViewSet,
    InscripcionViewSet,
)

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')
router.register(r'cursos', CourseViewSet, basename='cursos')
router.register(r'lecciones', LessonViewSet, basename='lecciones')
router.register(r'inscripciones', InscripcionViewSet, basename='inscripciones')

urlpatterns = router.urls
