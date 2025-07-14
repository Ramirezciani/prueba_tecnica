import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';  // <-- Importa esto

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [RouterModule],  // <-- agrégalo aquí
  templateUrl: './sidebar.html',
  styleUrls: ['./sidebar.css']
})
export class Sidebar { }