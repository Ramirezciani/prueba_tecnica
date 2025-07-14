// src/app/shared/toast-container/toast-container.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Toast } from '../toast';

@Component({
  selector: 'app-toast-container',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './toast-container.html',
})
export class ToastContainerComponent {
  constructor(public toastService: Toast) { }
}