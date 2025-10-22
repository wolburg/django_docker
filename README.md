# 🐳 Proyecto Django con Docker

Este proyecto contiene una aplicación **Django** configurada para ejecutarse dentro de **Docker**, utilizando **PostgreSQL** como base de datos.

---

## 🚀 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- [Git](https://git-scm.com/downloads)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## ⚙️ Clonar el repositorio

Clona el proyecto desde GitHub:

```bash
git clone https://github.com/wolburg/django_docker.git

Levanta el docker con docker compose up --build
Aplica las migraciones docker compose exec web python manage.py migrate
Crea un superusuarios docker compose exec web python manage.py createsuperuser
Y entra a Aplicación principal: http://localhost:8500/
