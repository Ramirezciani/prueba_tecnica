# Etapa 1: Build de la aplicación Angular
FROM node:20 AS build

WORKDIR /app
COPY . .

# Instala dependencias
RUN npm install

# Compila la app (ajusta el nombre si tu app no se llama "app-frontend")
RUN npm run build --prod

# Etapa 2: Imagen liviana con Nginx para servir el frontend
FROM nginx:alpine

# Copia la app compilada al directorio público de Nginx
COPY --from=build /app/dist/* /usr/share/nginx/html/

# Expone el puerto 80 para acceder desde el navegador
EXPOSE 80
