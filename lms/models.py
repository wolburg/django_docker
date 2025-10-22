from django.db import models


class Usuario(models.Model):
    # id (AutoField por defecto)
    correo = models.EmailField(unique=True, max_length=150)
    contrasena = models.CharField(max_length=128)
    nombre = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} ({self.correo})"


class Course(models.Model):
    # id (AutoField por defecto)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructor = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="courses_taught"
    )
    avatar = models.ImageField(upload_to="course_avatars/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} (ID: {self.id})"


class Lesson(models.Model):
    # id (AutoField por defecto)
    nombre_leccion = models.CharField(max_length=200)
    curso = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="lessons"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_leccion} (Curso: {self.curso.title})"


class Inscripcion(models.Model):
    # id (AutoField por defecto)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    curso = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="inscripciones"
    )
    fecha_inscripcion = models.DateField(auto_now_add=True)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.usuario.nombre} → {self.curso.title} ({self.rol})"
