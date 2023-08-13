<!-- ABOUT THE PROJECT -->
# 데이터생성기

* 추후 [CRM (고객관리 솔루션) 프로젝트 개발](https://github.com/sangeun99/crm-page.git) 에 사용할 데이터를 생성한다

* 생성할 수 있는 데이터 : User, Store, Item, Order, Orderlist

## 기술스택

* 언어 : Python

* 라이브러리 : SQLAlchemy

* 주소 데이터 : [주소기반산업지원서비스](https://business.juso.go.kr/addrlink/attrbDBDwld/attrbDBDwldList.do)


## 사용법
[CRM](https://github.com/sangeun99/crm-page.git) 페이지에서 이용하기를 원한다면 다음 명령어를 순서대로 입력하여 얻을 수 있다.<br/>
(데이터 개수 임의 변경 가능)

```
python main.py user 100000 csv
python main.py store 150 csv
python main.py item 100 csv
python main.py order 1000000 csv
python main.py orderlist 2000000 csv
```


## 기능

* 재사용성이 높은 코드로 구성하기 위해 객체와 메소드를 최대한 이용함

* 추상클래스를 이용해 각 요소 Generator의 형식을 정의함

* 데이터 클래스를 생성한 이후에는 main.py의 selectModel 변수에 등록해주기만 하면, generateMultipleData 함수로 해당 데이터 생성 가능함

* 실제 주소와 비슷한 데이터 생성을 위해 [주소기반산업지원서비스](https://business.juso.go.kr/addrlink/attrbDBDwld/attrbDBDwldList.do)의 데이터를 이용함<br/>
src/addr/TN_SPRD_RDNM.txt 가 src/roadname.db로 구성되는 코드는 [makeAddrDb.py](https://github.com/sangeun99/data-generator/blob/main/makeAddrDb.py)에서 확인 가능함

* 명령줄에서 인자를 주어 데이터를 생성할 수 있도록 함<br/>
```python main.py user 10 csv```


## License

MIT 라이센스에 따라 배포. 자세한 내용은 `LICENSE`를 참조하세요.


## Contact
* 엄상은
* sangeun.e.9@gmail.com