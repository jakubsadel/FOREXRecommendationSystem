import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, tap } from 'rxjs/operators';

@Component({
  selector: 'app-entry',
  templateUrl: './entry.component.html',
  styleUrls: ['./entry.component.scss']
})
export class EntryComponent {

  title = 'FRS';
  imgsrc = '';
  pandas = '';
  resavg = '';
  str1 = '';
  todayDate = '';
  constructor(private _http: HttpClient) {
    this.c1.todayDate = "xddd"
  }

  c1:Stock = new Stock();


  loadData(): void
  {
   this.getImage();
   this.getDate();
    }


  getImage()
  {
  this.imgsrc = '/getimg';
  }

  getDate()
  { console.log('xd');
    this._http.get("/getdejt").subscribe(res => this.todayDate = res.toString());
    console.log(this.todayDate);
  }

  click2(){
    this.getAllBooks().subscribe(b => this.c1 = b)
  }

  getAllBooks()
  {
    return this._http
      .get<Stock>('/getcust') 
  }

}


export class Stock{
  todayDate!: string;
  previousDate!: string;
}