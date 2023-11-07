# BLOA(Django mini project)
Django, Python, HTML, CSS를 활용한 블로그 개발 프로젝트입니다.

## 프로젝트 목표 및 배경
  의견 공유를 자유롭게 할 수 있는 포럼 형식의 블로그를 작성하고 싶어
  
  제가 즐겨 하는 PC 게임인 로스트아크로 한정하여 '로스트아크 블로그(이하 BLOA)'라는 주제를 선정하였고
  
  블로그 글을 작성하고 관련된 댓글 및 태그를 만들어 관련 주제에 대한 팁 및 의견 등을 공유하고
  
  태그 기능을 이용해 어떤 게시글/댓글을 검색할 수 있게 블로그를 만들었습니다. 

## 기능 및 요구사항
  * 기능
    * CRUD, 로그인/회원가입, 댓글, 조회수, 이미지 첨부 기능 구현
    * 블로그 글 작성 및 게시
    * 댓글 : 각 블로그 포스팅에 댓글 작성하고 수정/삭제 기능 구현
    * 태그 : 각 게시글의 태그를 통해 어떤 분류인지 파악 및 검색 가능

  * 요구사항
    * 0단계 : Django Admin을 활용한 게시글 읽기 및 메인 페이지 구현
    * 1단계 : 블로그 CRUD 기능 구현
    * 2단계 : 로그인/회원가입 기능 구현
    * 3단계 : 블로그 기능 외 추가 기능 구현
    
## 개발 기술 및 환경
   
    [FE]
   
    HTML5 CSS3 JAVASCRIPT
   
    [BE]
   
    PYTHON DJANGO
   
    [ENV]
   
    VS STUDIO

## 개발 기간
  2023.10.26 ~ 2023.11.07
   
  | 날짜       | 활동                     | 날짜       | 활동                |
|------------|--------------------------|------------|---------------------|
| 2023-10-26 | 계획 수립 및 DB 설계  | 2023-11-02 | 프로젝트 개발            |
| 2023-10-27 | 계획 수립 및 DB 설계  | 2023-11-03 | 프로젝트 개발            |
| 2023-10-28 | 계획 수립 및 DB 설계  | 2023-11-04 | 코드 점검         |
| 2023-10-29 | 계획 수립 및 DB 설계  | 2023-11-05 | 코드 점검         |
| 2023-10-30 | 프로젝트 개발            | 2023-11-06 | Readme 파일 작성  |
| 2023-10-31 | 프로젝트 개발            | 2023-11-07 | Readme 파일 작성  |
| 2023-11-01 | 프로젝트 개발            |



## 디렉터리 구조 / url 구조
  디렉터리 파일 구조로는 아래와 같이 진행하였습니다.

  mysite/

  ├── accounts
  
  ├── blog
  
  ├── main
  
  ├── media
  
  ├── static
  
  ㅣ├── assets
  
  ㅣ├── css
  
  ㅣ├── html
  
  ├── templates
  
  ㅣ├── accounts
  
  ㅣ├── blog
  
  ㅣ├── main
  
  ├── tutorialdjango
  
  ├── db.sqlite3
  
  ├── manage.py

## ERD 모델링
  
  ![ERDmodeling](https://github.com/mintcookie-park/django_miniproject/assets/79849531/c2a9c3f0-a8d1-4367-ace4-ef818f119d8b)

  

## 메인 기능 / 추가 기능
  
  * 메인 기능

    * 게시글 작성, 수정, 삭제, 조회
    * 로그인/회원가입
     
  * 추가 기능

    * 댓글 기능
    * 이미지 추가
    * 조회수

## 프로젝트 기능 실행 결과

  ### 실행 시 처음 화면
  
  ![Home](https://github.com/mintcookie-park/django_miniproject/assets/79849531/387b0ebb-80e4-4339-abb9-335238eff714)

  ### 블로그의 설명 화면
  
  ![About](https://github.com/mintcookie-park/django_miniproject/assets/79849531/a5b8a4cf-ef7c-468f-bf5d-ad2737d9c6dc)

  ### 블로그 글 작성 및 댓글 작성 화면
  
  ![Blog](https://github.com/mintcookie-park/django_miniproject/assets/79849531/d35a8ff8-61b6-4d0a-9b9a-262d4c078d79)


  ### 프로필 설정 및 비밀번호 재설정 화면
  
  ![Profile](https://github.com/mintcookie-park/django_miniproject/assets/79849531/54db7cfa-c004-449f-ad6a-b44aa5a1c69b)



## 개발 인원
  
  박정훈
  
## 느낀점
  Django와 Python을 통해 블로그 개발을 편리하고 빠르게 개발할 수 있는 경험을 하였고

  DB 구조와 프로젝트 문서 작성을 통해 예전에 두서 없이 개발했던 경험을 퇴고하며

  수정사항이나 관련 메모를 기입하며 하는 습관을 기르게 된 중요한 경험을 하였습니다.
