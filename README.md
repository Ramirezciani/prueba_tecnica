📋 Gestor de Tareas Colaborativo
📝 Descripción General
Aplicación web colaborativa para la gestión de tareas dentro de proyectos. Permite a los usuarios:

Crear, asignar, actualizar y eliminar tareas

Gestionar proyectos y equipos

Colaborar en tiempo real

Visualizar tareas en formato Kanban

Recibir notificaciones en vivo

🛠️ Tecnologías Utilizadas
Componente	Tecnologías
Backend	FastAPI (Python 3.11), SQLAlchemy, AsyncPG, JWT
Frontend	Angular, Node.js
Base de Datos	PostgreSQL 15
Contenedores	Docker, Docker Compose

✨ Funcionalidades Principales
✅ Gestión de Usuarios — Registro, login y autenticación JWT

✅ CRUD de Proyectos — Crear, leer, actualizar y eliminar proyectos

✅ CRUD de Tareas — Asignación de tareas y filtros

✅ Colaboración en Tiempo Real — Actualizaciones en vivo

✅ Interfaz Kanban — Visualización intuitiva de tareas

✅ Notificaciones — Alertas automáticas por cambios

🚀 Levantamiento del Entorno
Prerrequisitos
Docker

Docker Compose (v2 o superior)

Pasos para iniciar:
bash
Copiar
Editar
# 1. Clonar el repositorio
git clone https://github.com/Ramirezciani/prueba_tecnica.git

# 2. (Opcional) Crear archivo .env
echo "DATABASE_URL=postgresql+asyncpg://admin:admin@db:5432/taskdb" > .env

# 3. Levantar los servicios
docker-compose up --build
🔑 Usuario por Defecto
Email	Contraseña
admin@example.cl	admin

Este usuario se crea automáticamente al iniciar los servicios.

🌐 Servicios Disponibles
Servicio	URL
Frontend (Angular)	http://localhost:4200
Backend (FastAPI)	http://localhost:8000
Documentación API (Swagger)	http://localhost:8000/docs
PostgreSQL	localhost:5432

⚙️ Detalles Técnicos
Backend
FastAPI expone la API en /

Conexión PostgreSQL via SQLAlchemy + AsyncPG

Autenticación con JWT

Código fuente: backend/app/

Imagen basada en python:3.11-slim

Servidor: Uvicorn

Frontend
Angular CLI + Node.js

Servido con Nginx en contenedor separado

Docker multietapa: Build + Producción

Puerto web: 4200

Base de Datos
Imagen oficial PostgreSQL 15

Datos persistidos en volumen pgdata

Inicialización con script db/init.sql

Variables de entorno definidas en docker-compose.yml

✅ Validación de Despliegue
bash
Copiar
Editar
docker-compose ps
Los servicios deben estar en estado Up

Abrir en navegador:

http://localhost:4200 — Frontend Angular

http://localhost:8000 — API FastAPI

http://localhost:8000/docs — Documentación Swagger

Logs en tiempo real:

bash
Copiar
Editar
docker-compose logs -f
🔮 Próximas Funcionalidades
🎯 Interfaz Kanban con Drag & Drop

📬 Notificaciones por Email

🔗 Integración con Slack / Trello

🚀 Optimización de consultas

🧪 Pruebas unitarias y de integración

🤝 Contribuciones
Proyecto realizado como prueba técnica Fullstack.
¡Se agradecen mejoras, sugerencias o reportes de bugs!

🙌 Agradecimientos
Gracias por revisar este proyecto. ¡Listo para continuar desarrollando juntos!
