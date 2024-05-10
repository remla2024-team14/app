import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {UserInputComponent} from "./components/user-input/user-input.component";
import {VersionDisplayComponent} from "./components/version-display/version-display.component";
import {HttpClientModule} from "@angular/common/http";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, UserInputComponent, VersionDisplayComponent, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'team14-app';
}
