import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Sidebar } from '../shared/sidebar/sidebar';

interface Project {
  id: number;
  name: string;
  description: string;
}

interface Task {
  id: number;
  name: string;
  projectId: number;
  title: string;
  description: string;
  status: string;
  due_date: string;
  assigned_to: number | null;
}

interface User {
  id: number;
  email: string;
  role: string;
}

@Component({
  selector: 'app-projects',
  standalone: true,
  imports: [
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule,
    Sidebar
  ],
  templateUrl: './projects.html',
  styleUrl: './projects.css'
})
export class Projects implements OnInit {
  projects: Project[] = [];
  tasks: Task[] = [];
  users: User[] = [];
  projectForm!: FormGroup;
  taskForm!: FormGroup;
  editingProject: Project | null = null;
  editingTask: Task | null = null;

  readonly projectApiUrl = 'http://localhost:8000/projects';
  readonly taskApiUrl = 'http://localhost:8000/tasks';
  readonly usersApiUrl = 'http://localhost:8000/users';

  constructor(private http: HttpClient, private fb: FormBuilder) { }

  ngOnInit(): void {
    this.initForms();
    this.loadProjects();
    this.loadTasks();
    this.loadUsers();
  }

  private initForms(): void {
    this.projectForm = this.fb.group({
      name: ['', Validators.required],
      description: ['', Validators.required]
    });

    this.taskForm = this.fb.group({
      name: ['', Validators.required],
      projectId: [null, Validators.required],
      title: ['', Validators.required],
      description: ['', Validators.required],
      status: ['', Validators.required],
      due_date: ['', Validators.required],
      assigned_to: [null, Validators.required]
    });
  }

  private loadUsers(): void {
    this.http.get<User[]>(this.usersApiUrl).subscribe({
      next: (users) => (this.users = users),
      error: (err) => console.error('Error al cargar usuarios:', err)
    });
  }

  // CRUD para Proyectos
  loadProjects(): void {
    this.http.get<Project[]>(this.projectApiUrl).subscribe({
      next: (projects) => (this.projects = projects),
      error: (err) => console.error('Error al cargar proyectos:', err)
    });
  }

  saveProject(): void {
    if (this.projectForm.invalid) return;

    const projectData = this.projectForm.value;

    if (this.editingProject) {
      this.http.put(`${this.projectApiUrl}/${this.editingProject.id}`, projectData).subscribe({
        next: () => {
          this.loadProjects();
          this.cancelProjectEdit();
        },
        error: (err) => console.error('Error al actualizar proyecto:', err)
      });
    } else {
      this.http.post<Project>(this.projectApiUrl, projectData).subscribe({
        next: () => {
          this.loadProjects();
          this.projectForm.reset();
        },
        error: (err) => console.error('Error al crear proyecto:', err)
      });
    }
  }

  editProject(project: Project): void {
    this.editingProject = project;
    this.projectForm.patchValue(project);
  }

  cancelProjectEdit(): void {
    this.editingProject = null;
    this.projectForm.reset();
  }

  deleteProject(project: Project): void {
    this.http.delete(`${this.projectApiUrl}/${project.id}`).subscribe({
      next: () => this.loadProjects(),
      error: (err) => console.error('Error al eliminar proyecto:', err)
    });
  }

  // CRUD para Tareas
  loadTasks(): void {
    this.http.get<Task[]>(this.taskApiUrl).subscribe({
      next: (tasks) => (this.tasks = tasks),
      error: (err) => console.error('Error al cargar tareas:', err)
    });
  }

  saveTask(): void {
    if (this.taskForm.invalid) {
      console.error('Formulario inválido:', this.taskForm.value);
      return;
    }

    const taskData = this.taskForm.value;
    console.log('Datos enviados:', taskData);

    if (this.editingTask) {
      this.http.put(`${this.taskApiUrl}/${this.editingTask.id}`, taskData).subscribe({
        next: () => {
          this.loadTasks();
          this.cancelTaskEdit();
        },
        error: (err) => console.error('Error al actualizar tarea:', err)
      });
    } else {
      this.http.post<Task>(this.taskApiUrl, taskData).subscribe({
        next: () => {
          this.loadTasks();
          this.taskForm.reset();
        },
        error: (err) => console.error('Error al crear tarea:', err)
      });
    }
  }

  editTask(task: Task): void {
    this.editingTask = task;
    this.taskForm.patchValue(task);
  }

  cancelTaskEdit(): void {
    this.editingTask = null;
    this.taskForm.reset();
  }

  deleteTask(task: Task): void {
    this.http.delete(`${this.taskApiUrl}/${task.id}`).subscribe({
      next: () => this.loadTasks(),
      error: (err) => console.error('Error al eliminar tarea:', err)
    });
  }
}
