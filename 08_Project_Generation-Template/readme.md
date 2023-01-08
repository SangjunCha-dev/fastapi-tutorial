# Project Generation - Template

프로젝트 생성 - 템플릿

프로젝트 템플릿을 사용하여 초기 설정, 보안, 데이터베이스 및 첫번째 API 엔드포인트등이 포함되어 프로젝트 시작 과정을 단축할 수 있음


## Full Stack FastAPI PostgreSQL

[GitHub](ttps://github.com/tiangolo/full-stack-fastapi-postgresql)

### Features

- 전체 Docker 통합(Docker 기반)
- Docker Swarm 모드 배포
- 로컬 개발을 위한 Docker Compose 통합 및 최적화
- Uvicorn 및 Gunicorn을 사용한 프로덕션 Python 웹서버
- Python FastAPI 백엔드
  - 빠른 성능: NodeJS 및 Go와 동등한 높은 성능 (Starlette 및 Pydantic)
  - 직관적: 좋은 편집기 지원. 디버깅 시간 단축
  - Easy: 쉼게 사용하고 배울 수 있도록 설계, 공식문서를 통한 학습시간 단축
  - Short: 코드 중복 최소화. 각 매개변수 선언의 여러 기능
  - 자동화: 문서 자동화
  - 표준화: API 대한 개방형 표준. [OpenAPI](https://github.com/OAI/OpenAPI-Specification), [JSON 스키마](https://json-schema.org/)
  - 다른 많은 기능: 유효성 자동검사, 직렬화, 대화형 문서, OAuth2 JWT 토큰인증
- 암호 해싱
- JWT 토큰 인증
- SQLAlchemy 모델
- 사용자를 위한 기본 시작 모델(필요에 따라 수정 및 제거)
- Alembic 마이그레이션
- CORS (Cross Origin 리소스 공유)
- Celery Worker: 백엔드에서 선택적으로 모델과 코드를 사용할 수 있음
- Docker와 통합된 Pytest 기반 REST 백엔드 테스트를 통해 데이터베이스와 독립적으로 전체 API 상호 작용 테스트할 수 있음. Docker에서 실행되므로 매번 처음부터 새로운 데이터베이스를 구축할 수 있음(따라서 ElasticSearch, MongoDB, CouchDB 또는 원하는 것을 사용하고 API가 작동하는지 테스트 진행)
- Atom Hydrogen 또는 Visual Studio Jupyter와 같은 확장을 사용하여 원격 또는 Docker에서 개발을 위해 Jupyter 커널과 Python을 쉽게 통합하여 사용할 수 있음
- Vue frontend
  - Vue CLI 생성
  - JWT 인증 처리
  - 로그인 뷰
  - 로그인 후 메인 대시보드 뷰
  - 사용자 생성 및 수정이 포함된 기본 대시보드
  - Vuex
  - Vue-router
  - 머테리얼 디자인 구성요소를 위한 Vuetify
  - 타입스크립트
  - Nginx 기반 Docker 서버(Vue-router 호환되는 구성)
  - Docker 빌드로 컴파일된 코드를 저장하거나 커밋할 필요가 없음
  - 프론트엔드 테스트는 빌드시 실행됨(비활성화 가능)
  - 가능한 모듈식으로 제작되어 사용할 수 있지만 Vue CLI로 재생성하거나 필요에 따라 추가하거나 원하는것을 재사용할 수 있음
  - PostgreSQL 데이터베이스용 PGAdmin, PHPMyAdmin 및 MySQL을 쉽게 사용하도록 수정할 수 있음
  - Flower: Celery job 모니터링
  - Traefik를 사용하여 프론트엔드와 백엔드 사이에 로드 밸런싱을 통해 동일한 도메인 아래에 경로로 구분되고 서로 다른 컨테이너에서 서비스를 제공할 수 있음
  - HTTPS 인증서 자동생성을 포함한 Traefik
  - 프론트엔트 및 백엔드 테스트를 포함한 GitLab CI (지속적인 통합)


## 참조 Docs

- https://fastapi.tiangolo.com/project-generation/
