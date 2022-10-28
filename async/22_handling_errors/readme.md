# Handling Errors

오류 처리


## 테스트

### The resulting response

- GET http://localhost:8000/items/foo

response
```json
{
  "item": "The Foo Wrestlers"
}
```

- GET http://localhost:8000/items/bar

response
```json
{
  "detail": "Item not found"
}
```

### Install custom exception handlers

- GET http://localhost:8000/unicorns/yolo

response
```json
{
  "message": "Oops! yolo did something. There goes a rainrow..."
}
```

### Override request validation exceptions

- GET http://localhost:8000/items2/foo

response
```text
1 validation error for Request
path -> item_id
  value is not a valid integer (type=type_error.integer)
```

### Use the RequestValidationError body

- POST http://localhost:8000/items/

request
```json
{
  "title": "towel",
  "size": "XL"
}
```

response
```json
{
  "detail": [
    {
      "loc": [
        "body",
        "size"
      ],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ],
  "body": {
    "title": "string",
    "size": "XL"
  }
}
```


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/handling-errors/
