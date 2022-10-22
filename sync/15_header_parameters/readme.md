# Header Parameters


## 테스트

### Declare Header parameters

기본적으로 Header매개변수 이름 문자를 밑줄(_)에서 하이픈(-)으로 변환하여 헤더를 추출하고 문서화함

- GET http://localhost:8000/items/

response
```json
{
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
```

### Automatic conversion

HTTP 헤더는 대소문자를 구분하지 않으므로 표준 Python 스타일("snake_case"라고도 함)로 선언할 수 있음

다른 이유로 밑줄(_)을 하이픈(-)으로 자동 변환을 비활성화해야 하는 경우 Header 매개변수 `convert_underscores=False` 설정 해야함

- GET http://localhost:8000/items2/

request header
strange_header: "tester"

response
```json
{
  "strange_header": "tester"
}
```

### Duplicate headers

중복 헤더의 모든 값을 Python으로 list 받을 수 있음

request header
x-token: ["abc", "def"]

response
```json
{
  "X-Token values": [
    "abc,def"
  ]
}
```


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/header-params/
