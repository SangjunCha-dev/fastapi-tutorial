# Sub-dependencies

하위 종속성


## Using the same dependency multiple times

- 여러 종속성에 공통된 하나의 종속성이 있는 경우 FastAPI는 해당 하위 종속성을 요청당 한번만 호출함
- 반환된 값을 "캐시"에 저장하고 동일한 요청에 대해 종속성을 여러번 호출하는 대신 해당 특정 요청에서 필요로 하는 모든 "종속성"에 전달함
- "캐시된" 값을 사용하는 대신 동일한 요청의 모든 단계(여러 번)에서 종속성을 호출하는 캐시 비활성화 `Depends(..., use_cache=False)` 매개변수를 설정 할 수 있음


## 요약

- 종속성 주입은 간단하게 코드의 양을 줄일수 있음
- 보안 기능 구현에서 종속성이 유용하게 사용됨


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/dependencies/sub-dependencies/
