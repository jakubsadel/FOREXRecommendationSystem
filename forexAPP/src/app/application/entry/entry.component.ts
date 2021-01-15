import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Stock} from 'src/app/application/model/stock';
import { TAPredictions} from 'src/app/application/model/tapredictions';
import { LSTMPredictions} from 'src/app/application/model/lstmpredictions';


@Component({
  selector: 'app-entry',
  templateUrl: './entry.component.html',
  styleUrls: ['./entry.component.scss']
})
export class EntryComponent {

  title = 'FOREX Recommendation System ';
  stockimg = '';
  lstmimg = '';
  condition = 0;

  constructor(private _http: HttpClient) {
    this.s1.todayDate = '____-__-__';
    this.s1.previousDate =  '____-__-__';
    this.s1.stockID = '____';
    this.t1.candleName = '';
    this.t1.trendVal = '';
    this.t1.spotDate = '';
    this.t1.trend = '';
    this.t1.taRecommendation = 'czekaj';
    this.l1.rmse = '';
    this.l1.day_1 = '';
    this.l1.day_2 = '';
    this.l1.day_3 = '';
    this.l1.day_4 = '';
    this.l1.day_5 = '';

  }

  s1: Stock = new Stock();
  t1: TAPredictions = new TAPredictions();
  l1: LSTMPredictions = new LSTMPredictions();


  getStockImage(): void
  {
  this.stockimg = '/getstockplot';
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

  getPatternInfo()
  {
    return this._http
      .get<TAPredictions>('/getpatternsdata') ;
  }

  getLSTMInfo()
  {
    return this._http
      .get<LSTMPredictions>('/getlstmdata') ;
  }

  loadPredictedInfo(): void
  {
    this.condition = 1;
    this.getPatternInfo().subscribe(t => this.t1 = t);
    this.getLSTMInfo().subscribe(l => this.l1 = l);
    this.getLSTMImage();
  }

}







