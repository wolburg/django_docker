from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario, Course, Lesson, Inscripcion


# ========= Usuario =========
class UsuarioSerializer(serializers.ModelSerializer):
    id_usuario = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Usuario
        fields = ['id_usuario', 'correo', 'nombre', 'contrasena', 'created_at', 'updated_at']
        extra_kwargs = {
            'contrasena': {'write_only': True}
        }

    def create(self, validated_data):
        pwd = validated_data.get('contrasena')
        if pwd:
            validated_data['contrasena'] = make_password(pwd)
        return super().create(validated_data)


# ========= Curso =========
class CourseSerializer(serializers.ModelSerializer):
    id_curso = serializers.IntegerField(source='id', read_only=True)
    instructor_id = serializers.PrimaryKeyRelatedField(
        source='instructor', queryset=Usuario.objects.all(), write_only=True
    )
    instructor = UsuarioSerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            'id_curso', 'title', 'description',
            'instructor_id', 'instructor',
            'avatar', 'created_at', 'updated_at'
        ]


# ========= Lección =========
class LessonSerializer(serializers.ModelSerializer):
    id_leccion = serializers.IntegerField(source='id', read_only=True)
    curso_id = serializers.PrimaryKeyRelatedField(
        source='curso', queryset=Course.objects.all(), write_only=True
    )
    curso = CourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = [
            'id_leccion', 'nombre_leccion',
            'curso_id', 'curso',
            'created_at', 'updated_at'
        ]


# ========= Inscripción =========
class InscripcionSerializer(serializers.ModelSerializer):
    id_inscripcion = serializers.IntegerField(source='id', read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        source='usuario', queryset=Usuario.objects.all(), write_only=True
    )
    curso_id = serializers.PrimaryKeyRelatedField(
        source='curso', queryset=Course.objects.all(), write_only=True
    )
    usuario = UsuarioSerializer(read_only=True)
    curso = CourseSerializer(read_only=True)

    class Meta:
        model = Inscripcion
        fields = [
            'id_inscripcion',
            'usuario_id', 'usuario',
            'curso_id', 'curso',
            'fecha_inscripcion', 'rol'
        ]
