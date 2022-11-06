# Dependencies with yield

yield 종속성


## A database dependency with yield

- `yield`구문은 반드시 함수내에서 1번만 사용해야함


## A dependency with yield and try

- try 구문에서 exception 발생시 finally 구문의 close 동작하게됨


## Dependencies with yield and HTTPException

- HTTPException 코드에서는 `yield` 동작하지 않음
- 종속성의 종료 코드는 응답이 전송된 후 `yield` 실행되므로 예외 처리기가 이미 실행된 것
- 종료 코드에서 종속성으로 인해 발생하는 예외는 잡을 수 없음
- 그러므로 응답이 전송된 이후 백그라운드 작업을 실행하는 용도로 사용


## What are "Context Managers"

Context Manager는 with 파일을 읽는데 사용할 수 있음

```python
with open("./somefile.txt") as f:
    contents = f.read()
    print(contents)
```

- open(...)은 Context Manager 개체를 생성하고 블록이 완료되면 `with` 예외가 있더라도 file을 객체를 닫음
- yield 종속성을 생성하면 FastAPI가 내부적으로 Context Manager로 변환하고 다른 도구와 결합함


## Using context managers in dependencies with yield

- python으로 context manager를 만들 수 있음
- context manager를 만드는 다른 방법
    - `@contextlib.contextmanager`
    - `@contextlib.asynccontextmanager`


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/
