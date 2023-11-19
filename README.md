# django_project1

먼저 기본파이참 프로젝트 ch01 start를 생성하였습니다.
테스트 위해서 관리자 페이지 연결하여 사이트 확인하였습니다. 
![image](https://github.com/sowon61/django_project/assets/115778827/c478ae16-ac26-40ff-a0f1-18c1da480f35)

설문조사 애플리케이션을 설계하기 위하여 ch03 polls 파일 만들고 요구사항에 따른 URL설계하였습니다. 장고앱 생성해서 데이터베이스 만들어졌습니다.
![image](https://github.com/sowon61/django_project/assets/115778827/876ff831-06d0-4c55-bd66-0dd52ccd9413)
![image](https://github.com/sowon61/django_project/assets/115778827/5a2144df-352d-4c1b-b958-cdb040c9c338)

View를 연결하여 hello world 간단한 화면 출력을 해보았습니다.
![image](https://github.com/sowon61/django_project/assets/115778827/18f697d0-06eb-4084-8259-d6e5b2a78238)
![image](https://github.com/sowon61/django_project/assets/115778827/557c0cb6-45f3-40f9-8d18-ae85ae5d94d8)

관리자 페이지에서 Question 3개 이상, 각 Question 마다 Choice 3개 이상 등록하여 기능 동작을 확인할 수 있도록 설정해야하므로 질문 3개를 추가하였습니다
![image](https://github.com/sowon61/django_project/assets/115778827/20ff28fe-8031-409e-b59a-8a5a580238d2)

![image](https://github.com/sowon61/django_project/assets/115778827/54d78729-5dc9-47f1-b469-acf6bc737ba7)
![image](https://github.com/sowon61/django_project/assets/115778827/52e92a95-13f3-49e6-8c1a-2f7452908e3e)
![image](https://github.com/sowon61/django_project/assets/115778827/82747b4d-394a-445c-8b11-d7fa3bb0e29d)

Question 과 Choice테이블을 한 화면에서 처리할 수 있도록 변경하였고 UI 화면에 필터 사이드바, 검색박스를 추가하였습니다.
![image](https://github.com/sowon61/django_project/assets/115778827/1639d78f-6494-4e20-bf57-ac8e7b36d601)

admin 사이트를 변경하였습니다.
![image](https://github.com/sowon61/django_project/assets/115778827/6d432080-f6ef-40dd-a09b-dbab7308f1a3)
![image](https://github.com/sowon61/django_project/assets/115778827/ceb28a97-c27a-428e-b24d-2352f1985259)

“list_filter" 를 사용해 UI 화면 우측에 필터 사이드 바를 추가하였습니다.
