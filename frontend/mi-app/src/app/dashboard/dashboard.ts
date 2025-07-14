import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common'; 
import { Sidebar } from '../shared/sidebar/sidebar';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [Sidebar, CommonModule],  
  templateUrl: './dashboard.html',
  styleUrls: ['./dashboard.css']
})
export class DashboardComponent implements OnInit {
  projects: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.fetchProjects();
  }

  fetchProjects(): void {
    this.http.get<any[]>('http://localhost:8000/members/kanban').subscribe({
      next: (data) => this.projects = data,
      error: (err) => console.error('Error fetching projects:', err)
    });
  }
}
