# Body - Multiple Parameters

Body 여러 매개변수


## 테스트

### Multiple body parameters - Body 다중 매개변수

- PUT /items2/1

request
```json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
```


response
```json
{
    "item_id": 1,
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
```

### Singular values in body

- PUT /items3/1

request
```json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
```

response
```json
{
  "item_id": 1,
  "item": {
    "name": "Foo",
    "description": "The pretender",
    "price": 42,
    "tax": 3.2
  },
  "user": {
    "username": "dave",
    "full_name": "Dave Grohl"
  },
  "importance": 5
}
```

### Embed a single body parameter

request

embed=True
```json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
```

embed=False
```json
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```

response
```json
{
    "item_id": 1,
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42,
        "tax": 3.2
    }
}
```


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/body-multiple-params/
