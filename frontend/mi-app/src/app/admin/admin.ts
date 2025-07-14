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

const rolesMap: Record<number, string> = {
  1: "Administrador",
  2: "Líder de Proyecto",
  3: "Colaborador"
};

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

  readonly rolesMap = rolesMap;
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
      role: ['', Validators.required], // Aquí se selecciona el ID
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

    const formValue = this.form.value;
    const userData = {
      name: formValue.name,
      email: formValue.email,
      password: formValue.password,
      role: rolesMap[+formValue.role]  // Convertir ID a string de rol
    };

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

    const roleId = Object.entries(rolesMap).find(([id, name]) => name === user.role)?.[0] || '';

    this.form.patchValue({
      name: user.name,
      email: user.email,
      role: roleId,
      password: ''
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
