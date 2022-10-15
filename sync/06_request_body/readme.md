# 테스트

- `127.0.0.1:8000/docs` swagger 접속

## Request Body

- POST /items/

    request
    ```json
    {
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5
    }
    ```

    response
    ```json
    {
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5
    }
    ```

- POST /items/ 일부 값만 전송

    request
    ```json
    {
        "name": "Foo",
        "price": 45.2
    }
    ```

    response
    ```json
    {
        "name": "Foo",
        "description": null,
        "price": 45.2,
        "tax": null
    }
    ```

## Use the model

- POST /items2/

    request
    ```json
    {
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5
    }
    ```

    response
    ```json
    {
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5,
    "price_with_tax": 48.7
    }
    ```

## Request body + path parameters

- PUT /items3/1

request
```
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
```

response
```json
{
    "item_id": 1,
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
```

## Request body + path + query parameters

- PUT /items4/1?q=tester

request
```json
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
```

response

```json
{
  "item_id": 1,
  "name": "Foo",
  "description": "An optional description",
  "price": 45.2,
  "tax": 3.5,
  "q": "tester"
}
```


# 참고 Docs

- https://fastapi.tiangolo.com/tutorial/body/
