# 테스트

## Defaults

- http://127.0.0.1:8000/items/?skip=0&limit=10

```
[
  {
    "item_name": "Foo"
  },
  {
    "item_name": "Bar"
  },
  {
    "item_name": "Baz"
  }
]
```

- http://127.0.0.1:8000/items/?skip=20

```
[]
```

## Query parameter type conversion

- http://127.0.0.1:8000/items/foo?short=1
- http://127.0.0.1:8000/items/foo?short=True
- http://127.0.0.1:8000/items/foo?short=true
- http://127.0.0.1:8000/items/foo?short=on
- http://127.0.0.1:8000/items/foo?short=yes

```
{"item_id":"foo"}
```

## Multiple path and query parameters

- http://127.0.0.1:8000/users/1/items/bag?q=tester&short=false

```
{
  "item_id": "bag",
  "owner_id": 1,
  "q": "tester",
  "description": "This is an amazing item that has a long description"
}
```

## Required query parameters

- http://127.0.0.1:8000/items2/foo-item?needy=sooooneedy

```
{
  "item_id": "foo-item",
  "needy": "sooooneedy",
  "skip": 0,
  "limit": null
}
```


# 참고 Docs

- https://fastapi.tiangolo.com/tutorial/query-params/
