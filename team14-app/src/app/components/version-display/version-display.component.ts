import { Component, OnInit } from '@angular/core';
import { VersionService } from '../../services/version.service';

@Component({
  selector: 'app-version-display',
  templateUrl: './version-display.component.html',
  standalone: true,
  providers: [VersionService]
})
export class VersionDisplayComponent implements OnInit {
  version: string | undefined;

  constructor(private versionService: VersionService) { }

  ngOnInit(): void {
    this.fetchVersion();
  }

  fetchVersion() {
    this.versionService.getVersion().subscribe((data: any) => {
      this.version = data;
    });
  }
}
