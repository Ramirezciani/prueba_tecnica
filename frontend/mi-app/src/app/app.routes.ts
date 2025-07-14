import { Routes } from '@angular/router';
import { LoginComponent } from './auth/login/login';
import { DashboardComponent } from './dashboard/dashboard';
import { Admin } from './admin/admin';

export const routes: Routes = [
    { path: '', component: LoginComponent },            // Login en la raíz
    { path: 'dashboard', component: DashboardComponent }, // Dashboard para /dashboard
    { path: 'configuracion', component: Admin },
    // Puedes agregar más rutas aquí
];
