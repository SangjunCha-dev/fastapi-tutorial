# 서버 실행

```
uvicorn main:app --reload
```


# 테스트

## Any Type

- http://127.0.0.1:8000/items/foo

```
{"item_id":"foo"}
```

## Path parameters with types

- Data conversion
- http://127.0.0.1:8000/items2/3

```
{"item_id":3}
```

## Data validation

- http://127.0.0.1:8000/items2/foo
- http://127.0.0.1:8000/items2/4.2

```
{
    "detail": [
        {
            "loc": [
                "path",
                "item_id"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]
}
```

## Order matters

- http://127.0.0.1:8000/users/me

```
{"user_id":"the current user"}
```

- http://127.0.0.1:8000/users/tester

```
{"user_id":"tester"}
```

- http://127.0.0.1:8000/users

```
["Rick","Morty"]
```


# Predefined values

## create an enum class

- http://localhost:8000/docs
- swagger 접속후 `GET /models/{model_name}` 클릭
- model_name 선택 목록 중 하나를 선택하고 `Execute` 클릭


```
{
  "model_name": "alexnet",
  "message": "Deep Learning FTW!"
}
```

## Path convertor

- http://127.0.0.1:8000/files//home/johndoe/myfile.txt/

```
{"file_path":"/home/johndoe/myfile.txt/"}
```


# 참고 Docs

- https://fastapi.tiangolo.com/tutorial/path-params/