/// <reference types="@angular/localize" />

import { bootstrapApplication } from '@angular/platform-browser';
import { provideRouter } from '@angular/router';
import { provideHttpClient, HttpClientModule } from '@angular/common/http'; // Importa HttpClientModule
import { appConfig } from './app/app.config';
import { App } from './app/app';
import { routes } from './app/app.routes'; // Importa las rutas

bootstrapApplication(App, {
  providers: [
    provideRouter(routes), // Asegúrate de incluir las rutas aquí
    provideHttpClient(),   // Proporciona HttpClient
    ...appConfig.providers
  ]
}).catch((err) => console.error(err));
