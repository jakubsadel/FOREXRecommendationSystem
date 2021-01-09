import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, tap } from 'rxjs/operators';

@Component({
  selector: 'app-entry',
  templateUrl: './entry.component.html',
  styleUrls: ['./entry.component.scss']
})
export class EntryComponent {

  title = 'FOREX Recommendation System ';
  stockimg = '';
  lstmimg = '';
  pandas = '';
  resavg = '';
  str1 = '';
  todayDate = '';
  constructor(private _http: HttpClient) {
    this.s1.todayDate = '____-__-__';
    this.s1.previousDate =  '____-__-__';
    this.s1.stockID = '____';
    this.s1.list = [];
  }

  s1: Stock = new Stock();




  getStockImage(): void
  {
  this.stockimg = '/getimg';
  }

  getLSTMImage(): void
  {
  this.lstmimg = '/getlstmplot';
  }


  loadStockData(): void
  {
    this.getStockInfo().subscribe(a => this.s1 = a);
    this.getStockImage();
  }

  getStockInfo()
  {
    return this._http
      .get<Stock>('/getstockdata') ;
  }


  loadPredictedInfo(): void
  {
    this.getLSTMImage();
  }

}


export class Stock{
  todayDate!: string;
  previousDate!: string;
  stockID!: string;
  list!: Array<number>
}




