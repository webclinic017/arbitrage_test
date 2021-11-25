<div align="center">

  <h3 align="center">Project-B</h3>

  <p align="center">
    <img src='asset/diagram.png?raw=1' width = '900' >
    <br />
    알고리즘 프로세스 다이어그램
  </p>
</div>

## Demo
[View Demo](https://ailab-sample.herokuapp.com/)

## Directory

| Path | Description
| :--- | :----------
| utils | 알고리즘 모듈화
| &ensp;&ensp;&boxvr;&nbsp; template  | 홈페이지
| &ensp;&ensp;&boxvr;&nbsp; data_crawler  | 데이터 크롤러
| &ensp;&ensp;&boxvr;&nbsp; Alpha_Function | 알파 알고리즘
| &ensp;&ensp;&boxvr;&nbsp; Risk_Function | 리스크 알고리즘
| &ensp;&ensp;&boxvr;&nbsp; TransactionCost_Function | 거래비용 알고리즘
| &ensp;&ensp;&boxvr;&nbsp; simulation | 거래실행 알고리즘
| &ensp;&ensp;&boxur;&nbsp; PnO_Function | 성과평가 및 최적화 알고리즘
| app.py | 웹페이지 실행
| asset | 결과.html, 웹페이지.png

## install

```.bash
pip install -r requirements.txt
```

## Main App

```.bash
#run
streamlit run app.py
```

<p align="center">
    <img src='asset/webpage.gif?raw=1' width = '900' >
</p>

<!-- AddNew_Algorithm -->
## Add New_Algorithm
* Algorithm result must be one list
  * klay = [today_klay.Time, today_klay.Close, 'klay', klay]
  * money = [today_klay.Time, today_klay.Close, 'money', money]
  * btc = [today_btc.Time, today_btc.Close, 'btc', btc]
- [x] Alpha_Function.py
    - Add New_Algorithm
- [x] template.py
    - Add option value in function of Template
- [x] simulation.py
    - Add library
    - Add below'# 비교할 알고리즘', '# 비교할 알고리즘' in function of bactest
