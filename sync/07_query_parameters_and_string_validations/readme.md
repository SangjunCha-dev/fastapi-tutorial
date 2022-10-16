# Query Parameters and String Validations

쿼리 매개변수 및 문자열 유효성 검사


## 테스트

- GET http://localhost:8000/items/

response
```
{
  "items": [
    {
      "item_id": "Foo"
    },
    {
      "item_id": "Bar"
    }
  ]
}
```

### Query parameter list / multiple values

- GET http://localhost:8000/items10/?q=foo&q=bar

response
```
{
  "q": [
    "foo",
    "bar"
  ]
}
```

### Query parameter list / multiple values with defaults

- GET http://localhost:8000/items11/

response
```
{
  "q": [
    "foo",
    "bar"
  ]
}
```

### Alias parameters

- GET http://localhost:8000/items15/?item-query=foobaritems

response
```
{
  "items": [
    {
      "item_id": "Foo"
    },
    {
      "item_id": "Bar"
    }
  ],
  "q": "foobaritems"
}
```


## 요약

### 일반 유효성 검사 및 메타데이터

- alias
- title
- description
- deprecated

### 문자열에 대한 유효성 검사

- min_length
- max_length
- regex


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
