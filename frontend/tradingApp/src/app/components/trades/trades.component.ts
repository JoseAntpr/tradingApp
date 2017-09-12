import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';

import { TradeService } from '../../services/trade.service';

@Component({
  selector: 'app-trades',
  templateUrl: './trades.component.html',
  styles: []
})
export class TradesComponent implements OnInit {

  trades = [];

  constructor(
    private router:Router,
    private _tradeService: TradeService) { }

  ngOnInit() {
    this._tradeService
        .getAll()
        .subscribe(data => this.trades=data);
  }

}
