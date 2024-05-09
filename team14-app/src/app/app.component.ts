import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {UserInputComponent} from "./user-input/user-input.component";
import {VersionDisplayComponent} from "./version-display/version-display.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, UserInputComponent, VersionDisplayComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'team14-app';
}
