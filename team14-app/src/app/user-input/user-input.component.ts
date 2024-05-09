import { Component } from '@angular/core';
import {FormsModule} from "@angular/forms";

@Component({
  selector: 'app-user-input',
  standalone: true,
  imports: [
    FormsModule
  ],
  templateUrl: './user-input.component.html',
})
export class UserInputComponent {

  userInput: string = '';
  prediction: string = '';
  onEnter() {

  }
}
