# Body - Nested Models

Body - 내포된 모델


## 테스트

### Use the submodel as a type

- PUT /items4/1

request
```json
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
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
        "tax": 3.2,
        "tags": [
            "rock",
            "bar",
            "metal"
        ],
        "image": {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        }
    }
}
```

### Attributes with lists of submodels

- PUT /items6/1

request
```json
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": [
        "rock",
        "metal",
        "bar"
    ],
    "images": [
        {
            "url": "http://example.com/baz.jpg",
            "name": "The Foo live"
        },
        {
            "url": "http://example.com/dave.jpg",
            "name": "The Baz"
        }
    ]
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
        "tax": 3.2,
        "tags": [
            "metal",
            "rock",
            "bar"
        ],
        "images": [
            {
                "url": "http://example.com/baz.jpg",
                "name": "The Foo live"
            },
            {
                "url": "http://example.com/dave.jpg",
                "name": "The Baz"
            }
        ]
    }
}
```


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/body-nested-models/
