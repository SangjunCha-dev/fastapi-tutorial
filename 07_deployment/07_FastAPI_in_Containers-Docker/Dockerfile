# 공식 Python 이미지
FROM python:3.9

# 도커이미지의 현재 작업 디렉토리를 /code로 설정
WORKDIR /code

# requirements 파일을 도커이미지의 /code 디렉토리로 복사
COPY ./requirements.txt /code/requirements.txt

# 패키지 종속성 설치
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# ./app 디렉토리를 도커이미지의 /code 디렉토리로 복사
COPY ./app /code/app

# uvicorn 서버 실행 명령어
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
