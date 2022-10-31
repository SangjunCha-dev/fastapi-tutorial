# Body - Updates

Body - 업데이트


## Partial updates with PATCH

pydantic model 부분업데이트

```python
item.dict(exclude_unset=True)
```


## Using Pydantic's update parameter

기존 모델의 복사본을 만들고 업데이트할 데이터가 포함된 매개변수 전달

```python
stored_item_model.copy(update=update_data)
```


## 요약

1. (선택 사항) `PUT` 메소드 대신 `PATCH` 메소드 사용
2. 저장된 데이터 검색
3. 해당 데이터를 pydantic 모델에 넣음
4. dict를 사용하여 입력 모델의 기본값 없이 데이터 생성(exclude_unset)
    - 모델에서 지정한 기본값 대신 사용자가 실제로 설정한 값만 업데이트할 수 있음
5. 저장된 모델의 복사본을 생성하고, 부분 업데이트로 속성을 업데이트(update)
6. 복사한 모델을 DB에 저장할 수 있는 형식응로 변환(jsonable_encoder)
7. 데이터를 DB에 저장
8. 업데이트된 모델을 반환


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/body-updates/
