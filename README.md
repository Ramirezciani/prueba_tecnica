DOCUMENTACIÓN - Gestor de Tareas Colaborativo

--------------------------------------------------------------------------------

Descripción general:

Este proyecto es una aplicación web para la gestión colaborativa de tareas dentro de proyectos. Permite a los usuarios crear, asignar, actualizar y eliminar tareas, gestionar proyectos, y colaborar en tiempo real. Está compuesta por:

- **Backend**: API REST desarrollada con FastAPI (Python 3.11) y PostgreSQL.
- **Frontend**: Aplicación SPA con Angular, servida por Nginx.
- **Base de datos**: PostgreSQL 15.
- **Orquestación**: Docker y Docker Compose para contenerizar y levantar el sistema completo.

--------------------------------------------------------------------------------

Estructura del proyecto:

gestor-tareas/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── project.py
│   │   │   └── task.py
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── projects.py
│   │   │   └── tasks.py
│   │   └── ...
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   └── app-frontend/
│       ├── angular.json
│       ├── package.json
│       ├── Dockerfile
│       └── src/
│           ├── app/
│           │   ├── components/
│           │   ├── services/
│           │   └── ...
│           └── assets/
├── db/
│   └── init.sql
├── docker-compose.yml
├── .env
└── DOCUMENTACION.txt

--------------------------------------------------------------------------------

Tecnologías utilizadas:

- **Backend**: FastAPI, Python 3.11, SQLAlchemy, AsyncPG, JWT para autenticación.
- **Frontend**: Angular, Node.js, Nginx.
- **Base de datos**: PostgreSQL 15.
- **Contenedores**: Docker, Docker Compose.

--------------------------------------------------------------------------------

Características principales:

- **Gestión de usuarios**: Registro, inicio de sesión y autenticación mediante JWT.
- **Gestión de proyectos**: CRUD completo para proyectos.
- **Gestión de tareas**: CRUD completo para tareas, con asignación a usuarios y filtros.
- **Colaboración en tiempo real**: Actualización en vivo de tareas y proyectos.
- **Interfaz Kanban**: Visualización de tareas en formato Kanban.
- **Notificaciones**: Alertas en tiempo real para cambios en tareas y proyectos.

--------------------------------------------------------------------------------

Configuración y levantamiento del entorno:

Prerrequisitos:
- Docker instalado: https://docs.docker.com/get-docker/
- Docker Compose (v2 o superior)

Pasos para levantar el proyecto:

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/Ramirezciani/prueba_tecnica.git
    cd gestor-tareas
    ```

2. (Opcional) Crear archivo `.env` para variables de entorno, por ejemplo:
    ```env
    # .env
    DATABASE_URL=postgresql+asyncpg://admin:admin@db:5432/taskdb

    ```

3. Ejecutar Docker Compose para levantar todo:
    ```bash
    docker-compose up --build
    ```

--------------------------------------------------------------------------------

Servicios disponibles:

- **Frontend Angular**: [http://localhost:4200](http://localhost:4200)  
  Interfaz web cliente.

- **Backend FastAPI**: [http://localhost:8000](http://localhost:8000)  
  API REST para gestión y lógica.

- **Documentación Swagger**: [http://localhost:8000/docs](http://localhost:8000/docs)  
  Interfaz automática para probar la API.

- **PostgreSQL**: `localhost:5432` (cliente DB)  
  Base de datos relacional (uso interno).

--------------------------------------------------------------------------------

Detalles técnicos backend:

- FastAPI expone endpoint principal en `/`.
- Conexión a PostgreSQL configurada con SQLAlchemy y AsyncPG.
- Autenticación basada en JWT.
- Configuración de base de datos vía variable de entorno `DATABASE_URL`.
- Código fuente principal en `backend/app/`.
- Dockerfile usa `python:3.11-slim`, instala dependencias y corre `uvicorn`.

--------------------------------------------------------------------------------

Detalles técnicos frontend:

- Proyecto Angular creado con Angular CLI.
- Código construido en contenedor Node.js.
- Aplicación servida por Nginx en contenedor separado.
- Dockerfile multietapa: build y producción (Nginx).
- Puerto mapeado al 4200 para acceso web.

--------------------------------------------------------------------------------

Base de datos:

- PostgreSQL versión 15 en contenedor oficial.
- Datos persistidos en volumen Docker llamado `pgdata`.
- Script de inicialización SQL (`db/init.sql`) ejecutado al levantar el contenedor.
- Variables de acceso definidas en `docker-compose.yml`.

--------------------------------------------------------------------------------

Cómo validar que todo funciona:

1. Ejecutar:
    ```bash
    docker-compose ps
    ```
    Debe mostrar backend, frontend y db en estado `Up`.

2. Abrir navegador y acceder a:
    - [http://localhost:4200](http://localhost:4200) --> Interfaz Angular cargada.
    - [http://localhost:8000](http://localhost:8000) --> Mensaje JSON de bienvenida.
    - [http://localhost:8000/docs](http://localhost:8000/docs) --> Swagger UI.

3. Ver logs:
    ```bash
    docker-compose logs -f
    ```

--------------------------------------------------------------------------------

Próximos desarrollos:

- Mejorar la interfaz Kanban con drag-and-drop.
- Añadir notificaciones por correo electrónico.
- Implementar integración con servicios externos (e.g., Slack, Trello).
- Optimizar rendimiento de consultas en base de datos.
- Añadir pruebas unitarias y de integración.

--------------------------------------------------------------------------------

Contribuciones:

Proyecto creado para prueba técnica fullstack.  
Se aceptan mejoras, correcciones y sugerencias.

--------------------------------------------------------------------------------

Agradecimientos:

Gracias por revisar este proyecto. Quedo atento para continuar.

--------------------------------------------------------------------------------
