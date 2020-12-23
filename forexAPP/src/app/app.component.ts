import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map, tap } from 'rxjs/operators';
import {Observable} from 'rxjs';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'XD';
  imgsrc='';
  pandas='';
  imgsbsrc='';
  str1='';
  resavg='';
  constructor(private _http:HttpClient) {
    this.c1.name = "eli"
  }
 
  c1:Cust = new Cust();
  click1(){
    this.getBooks().subscribe(b => this.c1.name = b.toString())
  }
  click2(){
    this.getAllBooks().subscribe(b => this.c1 = b)
  }
 
  getavg(){
  	this._http.get("/getavg?val=" + this.str1).pipe(map(r=>r.toString()),tap(res => this.resavg= res))
  }


  getDF(){
    this._http.get("./getdata").pipe(map(r => r.toString()), tap(v => this.pandas = v));  
  }


  getAllBooks()
  {
    return this._http
      .get<Cust>("./getcust") // GET request  
  }
  getBooks()
  {
    return this._http
      .post("./apitest/","5") // POST request with argument
  }

  getsbimage()
  {
  	this.imgsbsrc = '/getsbdata';
  }

  getimage(){
  	this.imgsrc = '/getimg';
  }



}
 
export class Cust{
  name!: string;
  age!: number;
  city!: string;
}