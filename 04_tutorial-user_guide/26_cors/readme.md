# CORS (Cross-Origin Resource Sharing)

CORS 또는 "Cross-Origin 리소스 공유" 브라우저에서 실행되는 프런트엔드에 백엔드와 통신하는 JavaScript 코드가 있고 백엔드가 프런트엔드와 다른 "출처(서버)"에 있는 상황


## Use CORSMiddleware

CORSMiddleware 사용하여 FastAPI 애플리케이션 구성

- Import CORSMiddleware
- 허용된 출처목록 생성
- FastAPI 애플리케이션에 "미들웨어"로 추가

백엔드가 지정가능한 허용 항목

- 자격 증명(인증 헤더, 쿠키 등)
- 특정 HTTP 메소드(POST, PUT) 또는 와일드카드가 있는 모든 메소드 "*"
- 특정 HTTP 헤더 또는 와일드카드가 있는 모든 헤더 "*"

지원하는 인수

- allow_origins: 요청을 허용해야 하는 출처 목록
- allow_origin_regex: 요청을 허용해야 하는 출처와 일치하는 정규식 문자열
- allow_methods: 요청에 허용되어야 하는 HTTP 메서드 목록
    - 기본값은 ['GET']
- allow_headers: 요청에 대해 지원되어야 하는 HTTP 요청 헤더 목록
    - 기본값은 []
    - Accept, Accept-Language, Content-Language, Content-Type 항상 허용
- allow_credentials: 요청에 대해 쿠키를 지원해야 함
    - 기본값 False
    - 자격 증명을 허용하려면 와일드카드가 아닌 명시적으로 출처를 지정해야 함
- expose_headers: 브라우저에서 액세스할 수 있어야 하는 모든 응답 헤더
    - 기본값 []
- max_age: 브라우저가 CORS 응답을 캐시하는 최대 시간을 초 단위로 설정
    - 기본값 600


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/cors/
