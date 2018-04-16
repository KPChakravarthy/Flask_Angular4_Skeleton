import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'app';
  url = 'http://127.0.0.1:5000/apidata';
  response: any;
  items: any;
  offers: any;

  constructor(public http: HttpClient) {
  }

  ngOnInit() {
    this.http.get(this.url).subscribe(
      data => {
        this.response = data;
        this.items = this.response.results[0].items;
        this.offers = this.items[0].offers;
        console.log(this.items);
        console.log(this.response);
      }
    );
  }

}
