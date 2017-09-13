import { Component, OnInit, EventEmitter, Output } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { Router } from '@angular/router'

import { Trade } from '../../class/trade';
import { Coin } from '../../class/coin';
import { CoinService } from '../../services/coin.service';
import { TradeService } from '../../services/trade.service';

@Component({
  selector: 'app-new-trade',
  templateUrl: './new-trade.component.html',
  styles: []
})
export class NewTradeComponent implements OnInit {

  coinList:Coin[];
  rate:number;
  submitted = false;
  trade:Trade = {};
  none =undefined;


  constructor(
    private _coinService: CoinService,
    private _tradeService: TradeService,
    private _router:Router
  ) { }

  ngOnInit() {
   
     this._coinService
         .getAll()
         .subscribe(data => this.coinList = data);
    
    
  }

  onChange(): void{
    if (this.trade.sell_currency && this.trade.buy_currency && (this.trade.buy_currency != this.trade.sell_currency)){
      this._tradeService
          .getRate(this.trade.sell_currency.toString(), this.trade.buy_currency.toString())
          .subscribe(data => this.trade.rate = data['rate'])
    }
  }

  calculateBuyAmount():void {
    if(this.trade.sell_amount){
      this.trade.buy_amount = parseFloat((this.trade.sell_amount * this.trade.rate).toFixed(2));
    }
  }

  onSubmit():void{ 
    let trade: Trade;
    trade = Object.assign({}, this.trade) as Trade;

    this._tradeService
        .createTrade(trade)
        .subscribe(x => this._router.navigate(['/']));
      

  }

}
