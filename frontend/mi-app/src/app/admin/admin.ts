import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule, FormBuilder, Validators, FormGroup } from '@angular/forms';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { Sidebar } from '../shared/sidebar/sidebar';

interface User {
  id: number;
  name: string;
  email: string;
  role: string;
}

@Component({
  selector: 'app-admin',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule,
    Sidebar
  ],
  templateUrl: './admin.html',
  styleUrls: ['./admin.css']
})
export class Admin implements OnInit {
  users: User[] = [];
  form!: FormGroup;
  editingUser: User | null = null;

  readonly roles = ['Administrador', 'Líder de Proyecto', 'Colaborador'];
  readonly apiUrl = 'http://localhost:8000/users';

  constructor(
    private fb: FormBuilder,
    private http: HttpClient
  ) { }

  ngOnInit(): void {
    this.initForm();
    this.loadUsers();
  }

  private initForm(): void {
    this.form = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      role: ['', Validators.required],  // El select devuelve el valor string directo
      password: ['', Validators.required]
    });
  }

  loadUsers(): void {
    this.http.get<User[]>(this.apiUrl).subscribe({
      next: (users) => this.users = users,
      error: (err) => console.error('Error al cargar usuarios:', err)
    });
  }

  saveUser(): void {
    if (this.form.invalid) return;

    const userData = this.form.value;

    if (this.editingUser) {
      this.http.put(`${this.apiUrl}/${this.editingUser.id}`, userData).subscribe({
        next: () => {
          this.loadUsers();
          this.cancelEdit();
        },
        error: (err) => console.error('Error al actualizar:', err)
      });
    } else {
      this.http.post<User>(this.apiUrl, userData).subscribe({
        next: () => {
          this.loadUsers();
          this.form.reset();
        },
        error: (err) => console.error('Error al crear:', err)
      });
    }
  }

  editUser(user: User): void {
    this.editingUser = user;

    this.form.patchValue({
      name: user.name,
      email: user.email,
      role: user.role,
      password: ''  // Nunca se precarga la contraseña
    });
  }

  cancelEdit(): void {
    this.editingUser = null;
    this.form.reset();
  }

  deleteUser(user: User): void {
    this.http.delete(`${this.apiUrl}/${user.id}`).subscribe({
      next: () => this.loadUsers(),
      error: (err) => console.error('Error al eliminar:', err)
    });
  }
}
