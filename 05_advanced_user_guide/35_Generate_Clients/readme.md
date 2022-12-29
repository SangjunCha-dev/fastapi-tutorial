# Generate Clients

클라이언트 생성


## OpenAPI Client Generators

- 일반적인 툴 [OpenAPI Generator](https://openapi-generator.tech/)
- 프론트엔드 구축시 [openapi-typescript-codegen](https://github.com/ferdikoomen/openapi-typescript-codegen)


## 라이브러리 설치

## Generate a TypeScript Client

### npm setup

1. 다운로드 경로
    - https://nodejs.org/ko/download/
2. 설치 확인
    ```
    $ npm -v
    8.19.3

    $ node -v
    v18.13.0
    ```
3. 라이브러리 설치

```
npm install typescript --save-dev
npm install openapi-typescript-codegen --save-dev
```

4. client 생성 스크립트 실행

1. package.json 파일 작성
    ```
    {
    "name": "frontend-app",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
        "generate-client": "openapi --input http://localhost:8000/openapi.json --output ./src/client --client axios"
    },
    "author": "",
    "license": "",
    "devDependencies": {
        "openapi-typescript-codegen": "^0.23.0",
        "typescript": "^4.9.4"
    }
    }
    ```

2. client 생성 스크립트 실행
    ```
    npm run generate-client
    ```


## 참조 Docs

- https://fastapi.tiangolo.com/advanced/generate-clients/
