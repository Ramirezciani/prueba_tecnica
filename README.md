
📋 GESTOR DE TAREAS COLABORATIVO
================================

📝 DESCRIPCIÓN GENERAL
----------------------
Aplicación web colaborativa para la gestión de tareas dentro de proyectos. Permite a los usuarios:
- Crear, asignar, actualizar y eliminar tareas
- Gestionar proyectos y equipos
- Colaborar en tiempo real
- Visualizar tareas en formato Kanban
- Recibir notificaciones en vivo

🛠️ TECNOLOGÍAS UTILIZADAS
--------------------------
| Componente   | Tecnologías                                  |
|--------------|-----------------------------------------------|
| Backend     | FastAPI (Python 3.11), SQLAlchemy, AsyncPG, JWT |
| Frontend    | Angular, Node.js                             |
| Base de Datos | PostgreSQL 15                             |
| Contenedores | Docker, Docker Compose                     |

✨ FUNCIONALIDADES PRINCIPALES
------------------------------
- ✅ Gestión de Usuarios — Registro, login y autenticación JWT
- ✅ CRUD de Proyectos — Crear, leer, actualizar y eliminar proyectos
- ✅ CRUD de Tareas — Asignación de tareas y filtros
- ✅ Colaboración en Tiempo Real — Actualizaciones en vivo
- ✅ Interfaz Kanban — Visualización intuitiva de tareas
- ✅ Notificaciones — Alertas automáticas por cambios

🚀 LEVANTAMIENTO DEL ENTORNO
----------------------------
PRERREQUISITOS:
- Docker (https://docs.docker.com/get-docker/)
- Docker Compose (v2 o superior)

PASOS:
1. Clonar el repositorio:
   git clone https://github.com/Ramirezciani/prueba_tecnica.git
   
2. Avanzar al proyecto 
   cd prueba_tecnica

3. Crear archivo .env:
   DATABASE_URL=postgresql+asyncpg://admin:admin@db:5432/taskdb

4. Levantar los servicios:
   docker-compose up --build

🔑 USUARIO POR DEFECTO
----------------------
| Email             | Contraseña |
|-------------------|-------------|
| admin@example.cl | admin       |

🌐 SERVICIOS DISPONIBLES
------------------------
- Frontend (Angular): http://localhost:4200
- Backend (FastAPI): http://localhost:8000
- Documentación API (Swagger): http://localhost:8000/docs
- PostgreSQL: localhost:5432

⚙️ DETALLES TÉCNICOS
--------------------
BACKEND:
- API disponible en /
- SQLAlchemy + AsyncPG para base de datos
- JWT para autenticación
- Código fuente en backend/app/
- Imagen Python 3.11-slim + Uvicorn

FRONTEND:
- Angular + Node.js
- Servido con Nginx (contenedor separado)
- Docker multietapa: build + producción
- Puerto web: 4200

BASE DE DATOS:
- PostgreSQL 15 (contenedor oficial)
- Volumen persistente: pgdata
- Inicialización desde db/init.sql
- Configuración en docker-compose.yml

✅ VALIDACIÓN DE DESPLIEGUE
---------------------------
docker-compose ps   # Los servicios deben estar UP

Acceder en navegador:
- http://localhost:4200 — Frontend
- http://localhost:8000 — API
- http://localhost:8000/docs — Documentación

Ver logs en tiempo real:
docker-compose logs -f

🔮 PRÓXIMAS FUNCIONALIDADES
---------------------------
- 🎯 Interfaz Kanban con drag & drop
- 📬 Notificaciones por email
- 🔗 Integración con Slack / Trello
- 🚀 Optimización de consultas
- 🧪 Pruebas unitarias e integración

🤝 CONTRIBUCIONES
-----------------
Proyecto creado como prueba técnica Fullstack.
Se aceptan sugerencias y mejoras.

🙌 AGRADECIMIENTOS
-------------------
Gracias por revisar este proyecto. ¡Listo para seguir avanzando!
