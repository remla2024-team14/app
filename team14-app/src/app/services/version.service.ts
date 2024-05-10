import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class VersionService {

  constructor(private httpClient: HttpClient) { }

  getVersion() {
    return this.httpClient.get("http://127.0.0.1:5000/lib-version");
  }
}
