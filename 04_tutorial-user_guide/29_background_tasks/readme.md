# Background Tasks


## 사용 예시

- 작업을 수행한 후 전송되는 이메일 알림
  - 응답을 즉시 반환하고 백그라운드에서 이메일을 보내는 것
- 처리된 데이터
  - 느린 프로세스를 거쳐야하는 파일은 우선 응답하고 백그라운드에서 데이터 처리


## Caveat

- 많은 백그라운드 계산을 수행하고 동일한 프로세스에서 실행할 필요가 없는 경우(메모리 및 변수 등을 공유할 필요가 없음)
- Celery backgorund task 사용 권장


## 참고 Docs

- https://fastapi.tiangolo.com/tutorial/background-tasks/
