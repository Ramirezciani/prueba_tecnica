import { Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login';
import { DashboardComponent } from './dashboard/dashboard';
import { Admin } from './admin/admin';
import { Projects } from './projects/projects'; // Importamos el componente de proyectos

export const routes: Routes = [
    { path: '', component: LoginComponent },            // Login en la raíz
    { path: 'dashboard', component: DashboardComponent }, // Dashboard para /dashboard
    { path: 'configuracion', component: Admin },
    { path: 'proyectos', component: Projects }, // Ruta para /proyectos
    // Puedes agregar más rutas aquí
];
