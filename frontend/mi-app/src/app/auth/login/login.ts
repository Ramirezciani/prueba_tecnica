import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, Validators, FormGroup } from '@angular/forms';

import { MatCardModule } from '@angular/material/card';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';

import { AuthService } from '../auth'; // Ajusta ruta si es necesario
import { Toast } from '../../shared/toast'; // Ajusta ruta al servicio toast
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    MatCardModule,
    MatInputModule,
    MatFormFieldModule,
    MatButtonModule
  ],
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class LoginComponent {

  form: FormGroup;

  constructor(
    private fb: FormBuilder,
    private authService: AuthService,
    public toastService: Toast,
    private router: Router
  ) {
    this.form = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.form.invalid) return;

    const credentials = {
      email: this.form.get('email')?.value ?? '',
      password: this.form.get('password')?.value ?? ''
    };

    this.authService.login(credentials).subscribe({
      next: (res) => {
        const token = res.access_token; // Asegúrate de que el backend envíe el token en este campo
        if (token) {
          localStorage.setItem('access_token', token);
        }
        this.toastService.show('Bienvenido', { classname: 'bg-success text-white', delay: 2000 });

        setTimeout(() => {
          this.router.navigate(['/dashboard']);
        }, 1500); // Espera para que el toast se vea antes de redirigir
      },
      error: (err) => {
        const msg = err?.error?.detail ?? 'Error en login';
        this.toastService.show(msg, { classname: 'bg-danger text-white', delay: 3000 });
      }
    });
  }
}
