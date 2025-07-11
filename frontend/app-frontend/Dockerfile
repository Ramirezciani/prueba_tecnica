# Etapa 1: Build Angular app
FROM node:20 AS build
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build --prod

# Etapa 2: Nginx para servir la app
FROM nginx:alpine
COPY --from=build /app/dist/app-frontend /usr/share/nginx/html
EXPOSE 80
