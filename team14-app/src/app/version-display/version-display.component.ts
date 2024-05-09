import {Component, inject, OnInit} from '@angular/core';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import {CommonModule} from "@angular/common";

@Component({
  selector: 'app-version-display',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './version-display.component.html',
})
export class VersionDisplayComponent implements OnInit {
  httpClient = inject(HttpClient);
  version: String | undefined;

  ngOnInit(): void {
    this.fetchVersion();
  }

  fetchVersion(){
    this.httpClient.get("http://127.0.0.1:5000/lib-version").subscribe((data:any) => {
      console.log(data);
      this.version = data;
    })
  }

}
