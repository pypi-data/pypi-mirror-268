# Introduction

eod2pd is a simple library to query eodhd.com in a multithreaded environment

**ATTENTION - The lib doesn't support all of the function calls available from EOD,
at the moment just historical stockprices are supported.**

## Getting Started

This library is a simple wrapper over the function calls listed at eodhd.com in order to retrive the price datas for some tickers. As mentioned above, only a small set of functions is supported at the moment, my focus point was to have a multithreaded environment available when accessing the data for more then one asset.

The following functions are available:

- `get_exchanges()` - get a dataframe with all exchanges
- `get_exchanges_symbols()` - get a dataframe for each of the given exchanges and receive all symols
- `get_symbols_prices()` - get a dataframe with price data for each given symbol name
- `get_symbols_prices_bulk()` - get a dataframe for each day in the given date range and exchange
- `get_symbols_dividends()` - get a dataframe with dividend payments for each given symbol
- `get_symbols_splits()` - get a dataframe with stock splits for each given symbol

The key point of the lib is that the requests are sent out in parallel by a threading framework provided by basefunctions. With this framework it's possible to request different data simultaneously and don't have to care about retry in error case or timeout situations.

## API-KEY Handling

eodhd.com needs an API-Key to work with. For the moment I have decided that the API-Key itself is readed from an .env file in your current project directory. The .env file in it's simplest form looks like, replace the phrase `your eodhd.com api key` with the API key you receive from eodhd.com

```python
EOD2PD_API_KEY = <your eodhd.com api key>
```

## Example

```python
>>> import eod2pd
>>> eod2pd.get_exchanges()
                             name    code operatingmic  country currency countryiso2 countryiso3
0                      USA Stocks      US   XNAS, XNYS      USA      USD          US         USA
1                 London Exchange     LSE         XLON       UK      GBP          GB         GBR
2                Toronto Exchange      TO         XTSE   Canada      CAD          CA         CAN
3                    NEO Exchange     NEO         NEOE   Canada      CAD          CA         CAN
4            TSX Venture Exchange       V         XTSX   Canada      CAD          CA         CAN
..                            ...     ...          ...      ...      ...         ...         ...
72  Money Market Virtual Exchange   MONEY         None  Unknown  Unknown                        
73   Europe Fund Virtual Exchange  EUFUND         None  Unknown      EUR                        
74        Istanbul Stock Exchange      IS         XIST   Turkey      TRY          TR         TUR
75               Cryptocurrencies      CC         CRYP  Unknown  Unknown                        
76                          FOREX   FOREX         CDSL  Unknown  Unknown                        

[77 rows x 7 columns]


>>> eod2pd.get_symbols_prices(["BMW.XETRA", "BAS.XETRA", "TL0.XETRA"])
{'TL0.XETRA':                symbol     open     high      low    close  adjusted_close  volume
date                                                                             
2013-03-06  TL0.XETRA   27.200   27.200   27.200   27.200          1.8133      50
2013-03-08  TL0.XETRA   28.020   30.425   28.010   30.425          2.0283     282
2013-03-11  TL0.XETRA   29.950   29.950   29.900   29.950          1.9967     210
2013-03-12  TL0.XETRA   29.715   29.715   29.715   29.715          1.9810     100
2013-03-13  TL0.XETRA   30.060   30.060   29.400   29.400          1.9600      67
...               ...      ...      ...      ...      ...             ...     ...
2024-03-18  TL0.XETRA  153.460  160.360  152.540  159.140        159.1400  150581
2024-03-19  TL0.XETRA  160.540  161.900  154.460  158.220        158.2200   85696
2024-03-20  TL0.XETRA  159.020  160.680  157.500  158.440        158.4400   62072
2024-03-21  TL0.XETRA  162.960  163.480  159.780  160.380        160.3800   65229
2024-03-22  TL0.XETRA  159.840  159.840  152.980  156.760        156.7600  113692

[2792 rows x 7 columns], 'BAS.XETRA':                symbol      open      high       low     close  adjusted_close   volume
date                                                                                  
1994-02-01  BAS.XETRA  154.5124  155.6884  153.8990  154.5124          2.4273  1565840
1994-02-02  BAS.XETRA  154.4102  155.0748  154.1546  154.4102          2.4257  1044460
1994-02-03  BAS.XETRA  154.5636  156.6088  151.5980  154.5636          2.4281  2216020
1994-02-04  BAS.XETRA  151.3424  153.8990  149.6552  151.3424          2.3775  1569320
1994-02-07  BAS.XETRA  148.8882  150.3198  148.3770  148.8882          2.3390  2213040
...               ...       ...       ...       ...       ...             ...      ...
2024-03-18  BAS.XETRA   49.5900   49.5900   48.7850   49.0050         49.0050  1302269
2024-03-19  BAS.XETRA   48.9800   50.6000   48.8650   50.6000         50.6000  3781991
2024-03-20  BAS.XETRA   50.6500   52.0900   50.6100   51.8800         51.8800  4141824
2024-03-21  BAS.XETRA   52.4200   52.8900   52.3100   52.6500         52.6500  2998619
2024-03-22  BAS.XETRA   52.4200   52.9000   52.2000   52.7200         52.7200  2335875

[7625 rows x 7 columns], 'BMW.XETRA':                symbol      open      high       low     close  adjusted_close   volume
date                                                                                  
1994-02-01  BMW.XETRA  406.4767  410.5692  400.0884  406.4767          5.1169  2677750
1994-02-02  BMW.XETRA  404.1757  405.7123  401.8772  404.1757          5.0880  2083911
1994-02-03  BMW.XETRA  398.2944  402.3868  397.2726  398.2944          5.0139  1822376
1994-02-04  BMW.XETRA  386.5370  392.6705  383.4664  386.5370          4.8659  2529985
1994-02-07  BMW.XETRA  385.0030  394.7193  382.4472  385.0030          4.8466  1404435
...               ...       ...       ...       ...       ...             ...      ...
2024-03-18  BMW.XETRA  106.1000  107.2200  104.8600  105.9800        105.9800   760275
2024-03-19  BMW.XETRA  106.2000  107.4000  105.9800  107.1200        107.1200   864978
2024-03-20  BMW.XETRA  107.0800  107.3400  105.6800  106.3600        106.3600   704215
2024-03-21  BMW.XETRA  107.0000  107.1000  104.3800  104.8000        104.8000  1509736
2024-03-22  BMW.XETRA  103.9200  104.6200  102.8400  104.1200        104.1200  1303067

[7626 rows x 7 columns]} 
```

## Project Homepage

<https://dev.azure.com/neuraldevelopment/eod2pd>

# Contribute

If you find a defect or suggest a new function, please send an eMail to <neutro2@outlook.de>
