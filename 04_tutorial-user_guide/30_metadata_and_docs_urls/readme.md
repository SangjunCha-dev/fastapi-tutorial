# Metadata and Docs URLs

메타데이터 및 문서 URL


## Metadata for API

|Parameter|Type|Description|
|---|---|---|
|title | str | 제목 |
|description | str | 설명. 마크다운 사용가능 |
|version | str | 버전. 자체적으로 지정한 애플리케이션 버전 |
|terms_of_service | str | 서비스 약관 URL |
|contact | dict | 연락처 정보({"name": str, "url": str, "email": str}) |
|license_info | dict | 라이선스 정보({"name": str, "url": str}) |


## Metadata for tags

|Parameter|Type|Description|
|---|---|---|
|name | str | 태그 이름(필수) |
|description | str | 설명. 마크다운 사용가능 |
|externalDocs | dict | 설명 외부 문서({"description": str, "url": str}) |


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/metadata/
