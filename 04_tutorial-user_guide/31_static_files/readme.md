# Static Files


## Use StaticFiles

- StaticFiles() 경로에 인스턴스 mount


## What is "Mounting"

"Mounting" 특정 경로에 완전한 "독립" 응용 프로그램을 추가한 다음 모든 하위 경로를 처리하는 것을 의미


## Details

- `app.mount("/static", ...)`: "하위 응용 프로그램"이 마운트될 경로 지정
  - 시작하는 모든 경로가 "/static"으로 시작
- `app.mount(..., StaticFiles(directory="static"), ...)`: 정적 파일이 포함된 디렉토리의 이름 지정
- `app.mount(..., name="static")`: FastAPI 에서 내부적으로 사용할 이름 지정


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/static-files/
