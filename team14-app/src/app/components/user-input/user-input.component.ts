import {Component} from '@angular/core';
import { UrlService } from '../../services/url.service';
import {FormsModule} from '@angular/forms';
import {NgForOf} from '@angular/common';
import { environment } from '../../../../../environment';

@Component({
  selector: 'app-user-input',
  templateUrl: './user-input.component.html',
  standalone: true,
  imports: [
    FormsModule,
    NgForOf
  ],
  providers: [UrlService]
})
export class UserInputComponent {
  inputUrl: string = '';
  selectedModel: string = 'model1';
  models: string[] = ['model1', 'model2'];
  target: string | undefined = environment.modelServiceURL;
  constructor(private urlService: UrlService) { }

  predict() {
    this.urlService.predict(this.selectedModel, this.inputUrl, this.target).subscribe();
  }
}
