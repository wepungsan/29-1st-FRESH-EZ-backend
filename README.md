# 29-1st-FRESH-EZ-backend

> 본 repository는 웹 개발 학습을 위해 프레시코드(https://www.freshcode.me/) 사이트를 클론코딩하였습니다.
> 짧은 기간동안 기능 구현에 보다 집중하기 위해 User, Product, Subscription 앱까지 기능 구현하였습니다.


## 개발 인원 및 기간

+ 개발기간: 2021.1.24. ~ 2022.02.11.
	+ Backend: 이도운, 이동훈 (repository: https://github.com/wecode-bootcamp-korea/29-1st-FRESH-EZ-backend)
	
	+ Backend
		+ Backend 공통: ERD, CSV Uploader
		+ 이도운 : 구독 옵션 View, 구독 상품 상세 View, 단일 상품 상세 View, 장바구니 View
		+ 이동훈 : 상품 리스트 View, 로그인 View, 회원가입 View


## Demo

> 영상


## ERD

![MRMRZARA](https://user-images.githubusercontent.com/86659102/153740817-a2566a25-818b-4fa9-84ff-281389bb07d5.png)


## 협업 도구

+ Github
+ [Trello 바로가기](https://trello.com/invite/accept-board)
+ Slack


## 사용 기술

+ Git
+ Django
+ Python
+ MySQL
+ AWS


## Library

+ JWT


## 구현 기능

### User
+ 회원가입: 정규표현식을 활용하여 email 및 비밀번호 유효성 체크, 이메일 중복 여부 체크, Bycrypt 활용하여 비밀번호 암호화 후 DB에 저장, 회원 별 알러지 정보 저장. (POST)

+ 로그인: Bcrypt 활용하여 비밀번호 복호화하여 체크 후 JWT 발급 (POST)

### Product
+ 제품 리스트 조회 (GET), 카테고리별 필터 기능 구현 (GET)

+ 단일 상품 상세 페이지 조회 기능 구현 (GET), 구독 상품 상세 페이지 조회 기능 구현 (GET)

+ Decorator 적용하여 token 통해서 유저 인증 후 알러지 유무에 맞게 제품 리스트가 보이도록 구현 (POST)

+ 장바구니에 제품 추가 기능 구현 (POST)

+ 장바구니 제품 리스트 조회 기능 구현 (POST)

+ 장바구니 제품 삭제 기능 구현 (POST)

### Subscription
+ Decorator 적용하여 token 통해서 유저 인증 후 구독 과정을 진행할 수 있도록 구현 (POST)


## Reference

+ 이 프로젝트는 프레시코드 사이트를 참조하여 학습 목적으로 만들었습니다.
+ 실무 수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제가 될 수 있습니다.
+ 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.

