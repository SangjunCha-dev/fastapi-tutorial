# Events: startup - shutdown

이벤트: 시작 - 종료

애플리케이션이 시작되기 전 또는 종료될 때 실행해야 하는 이벤트 핸들러(함수)를 정의할 수 있음


## startup event

애플리케이션이 시작되기 전에 실행되어야 하는 함수를 추가하려면 `@app.on_event("startup")` 이벤트로 선언

모든 startup 이벤트 핸들러가 완료될 때까지 애플리케이션은 요청 수신을 시작하지 않는다.


## shutdown event

애플리케이션이 종료될 때 실행되어야 하는 함수를 `@app.on_event("shutdown")` 이벤트로 선언


## 참조 Docs

- https://fastapi.tiangolo.com/advanced/events/
