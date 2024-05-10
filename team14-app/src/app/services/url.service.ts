import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UrlService {

  constructor(private httpClient: HttpClient) { }

  predict(modelName: string, inputUrl: string) {
    const payload = {
      model_name: modelName,
      input_url: inputUrl
    };

    return this.httpClient.post<any>('0.0.0.0:5000/predict', payload);
  }
}
