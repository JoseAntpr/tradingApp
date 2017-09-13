import { Injectable, Inject } from '@angular/core';
import {Http, Response} from '@angular/http';
import { Observable } from 'rxjs/Observable';
import "rxjs/add/operator/map";


import { environment } from '../../environments/environment'
import { Coin } from '../class/coin'

@Injectable()
export class CoinService {

  constructor(
    private _http: Http
  ) { }

  getAll(): Observable<Coin[]> {

    return this._http
      .get(`${ environment.urlBackend}/coins`)
      .map(res => res.json())
  }

}
