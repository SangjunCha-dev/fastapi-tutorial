# Request Files

파일 요청


## 라이브러리 설치

```bash
pip install python-multipart
```


## Define File Parameters

File은 Form 클래스를 직접 상속 클래스


## File Parameters with UploadFile

- 최대 크기 제한까지 메모리에 파일을 저장
- 제한을 초과하면 디스크에 저장


## UploadFile attributes

- `filename`: `str` 업로드된 원본 파일 이름 ex) myimage.jpg
- `content_type`: `str` 콘텐츠 유형(MIME type/media type) ex) image/jpeg
- `file`: `SpooledTemporaryFile` 파일 객체

async 호출 메소드

- `write(data)`: data(`str` or `bytes`) 파일 작성 
- `read(size)`: 파일에서 bytes/characters 을 읽어서 `size`(`int`) 반환
- `seek(offset)`: 파일의 바이트 위치 `offset`(`int`)로 이동
    - `await myfile.seek(0)`: 파일의 시작부분으로 이동
    - `await myfile.read()`: 한 번 실행하고 내용을 다시 읽을때 사용
- `close()`: 파일 닫기


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/request-files/
