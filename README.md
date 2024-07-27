Fragen:
----------
- Im Dokument steht Transaktionskosten sind gleich 0.005% (5Basispunkte). <br>
  Aber 0.005% = 0.00005 != 0.0005 = 5 Basispunkte -> NACHFRAGEN

- Wie sehen die Daten aus, welche in die bot-Funktion kommen? Sind sie EUR/BTC (steht im Dokument, ist aber eine winzige Zahl) oder doch BTC/EUR? 
- Gibt es eine Begrenzung bzgl. Laufzeit? Frage wegen API-Call

- Nach meinem Verständnis handeln wir von CLOSE zu CLOSE. Wann genau wird die bot-Funktion ausgeführt? Kurz vor oder kurz nach dem Close der Stundenkerze? <br>
  Z.B. um 10:01 oder um 09:59? Können uns evtl. kurzfristige Informationsvorteile verschaffen. Bzw. ist relevant für die Backtest-Analyse.

- Ziel ist eine gute Sharpe-Ratio: wird die berechnet in EURO? D.h. wenn man die ganze zeit in EURO bleibt (nicht erlaubt) hätte man eine Varianz von 0? <br>
  Wenn ja, dann sollten wir uns auf wenige qualitativ hochwertige Signale konzentrieren -> Qualität über Quantität. Müssen keineen hohen Gewinn erzielen, aber niedrige Vola. 

Datenanbieter/ APIS:
-----------------------
Binance:
  - library python-binance
  - um Kurse abzurufen werden keine Keys benötigt
  - Beispiel in Retrieve_BitcoinData.ipynb
  - KLINE_INTERVAL_3MINUTE verfügbar

Geckocoin:
  - https://www.coingecko.com/en/api/pricing
  - Demo account ist kostenlos ("Attribution required" -> was bedeutet das? )
  - Coin Historical Data (5 Minutely) für den letzten Tag stehen zur Verfügung
