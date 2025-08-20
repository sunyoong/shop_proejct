# shop_proejct

## Django 실행 방법 & URL 접속 

1. 가상환경 생성 및 설정(선택사항/윈도우 기준)
```
  pip -m venv .venv
  venv/Scripts/activate  (활성화)
```
  
2. 필요 패키지 설치
```
pip install -r requirements.txt
 ```

3. db migrate (프로젝트 루트 경로(shop_proejct/) 에서 실행)
  ```
  python manage.py migrate
  ```

4. django 실행 (프로젝트 루트 경로(shop_proejct/) 에서 실행)
```
 python manage.py runserver
```

5. url 접속
```
  127.0.0.1:8000
```


## Docker 실행 방법 & URL 접속 

1. docker 이미지 빌드
   ```
   docker compose up -d --build
   ```
   
2. docker 컨테이너 생성 및 실행
   ```
    docker compose up -d (백그라운드에서 실행)
   ```
   - 기타 명령어

     * docker 컨테이너 중단 및 삭제
       ```
       docker compose down
       ```
     * docker 컨테이너만 중단
       ```
       docker compose stop
       ```
     * 중단된 docker 컨테이너 다시 실행
       ```
       docker compose start
       ```
     * 실행중인 docker 목록보기
       ```
       docker ps
       ```
    
3. DB mirate
   ```
   docker exec -it shop_project-web-1 python manage.py migrate
   ```
   
5. URL 접속
   ```
   127.0.0.1:8000
   ```
