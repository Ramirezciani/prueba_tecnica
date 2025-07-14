import { Component } from '@angular/core';
import { RouterModule, Router } from '@angular/router';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [RouterModule],
  templateUrl: './sidebar.html',
  styleUrls: ['./sidebar.css']
})
export class Sidebar {
  constructor(private router: Router) { }

  logout() {
    localStorage.removeItem('access_token'); // Elimina el token
    this.router.navigate(['/login']);         // Navega a login
  }
}
