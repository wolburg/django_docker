from django.contrib import admin
from .models import Usuario, Course, Lesson, Inscripcion

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "correo", "nombre", "created_at")
    search_fields = ("correo", "nombre")
    list_filter = ("created_at",)
    ordering = ("id",)
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 25

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "instructor", "created_at")
    search_fields = ("title", "description")
    list_filter = ("created_at",)
    autocomplete_fields = ("instructor",)
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 25

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre_leccion", "curso", "created_at")
    search_fields = ("nombre_leccion",)
    list_filter = ("curso", "created_at")
    autocomplete_fields = ("curso",)
    ordering = ("curso", "id")
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 25

@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "curso", "rol", "fecha_inscripcion")
    search_fields = ("usuario__nombre", "usuario__correo", "curso__title")
    list_filter = ("rol", "fecha_inscripcion")
    autocomplete_fields = ("usuario", "curso")
    ordering = ("-fecha_inscripcion",)
    list_per_page = 25
