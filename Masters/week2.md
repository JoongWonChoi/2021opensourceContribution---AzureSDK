Week2 - Python팀 1차 keyword 선정 & 스터디 시작
=====
선정 keyword
----
+ Key Vault

What is Key Vault?
-----
+ Key Vault란 '비밀'이란 것을 안전하게 저장하고 접근하기 위한 클라우드 서비스
+ 이 때 '비밀'이란 접근을 강하게 제어하고자 하는 모든 것들을 지칭한다.
+ API keys, passwords, certification(증명서), cryptographic keys(암호화 키) 등 모두 '비밀'에 포함된다.
+ Кey Vault 서비스는 vault 와 HSM(Hardware security module) 두가지 형태 컨테이너로 제공된다.

Why Key Vault?
-----
+ 암호화된 데이터와 암호화 키는 물리적으로 안전하게 분리된 장소에 보관되어야 한다고 권장된다.
+ 데이터는 암호화(encrypted)되어 DB에 저장된다.
+ 그렇다면 암호화를 진행한 key는 어디에, 어떻게 저장되어야할까?
+ 이 때 Key Vault 서비스를 통하여 이러한 보안 issue들을 storage service에 저장한다.

Azure Key Vault 사용
-----
+ Secret Keys
  + Azure를 사용하여 가상머신(VM)과 디스크(disks)를 생성하면, 다양한 정보 생성
  + 이 디스크들에는 보통 운영체제 정보와 다양한 어플리케이션 정보를 동시에 보관됨.
  + 이 정보들은 다른 사용자가 함부로 접근하고 사용하지 못하도록 암호화(encrypt)되어야 함.
  + 이 때 이 정보들을 암호화 하고 해독할 수 있는(encryption & decryption) key가 필요한데, 이를 저장하고 사용할 수 있게 해주는 storage가 key vault이다.
  
+ Web Application Secrets
  + Web 어플리케이션이 DB에 연결할 때, 설정에 연결 정보를 저장해야 한다.
  + 이 때, key vault를 사용하여 이 Application Secrets 를 보관 및 사용할 수 있다.
  + key vault를 사용하면 각 어플리케이션 제작 시 암호 내용을 저장해야하는 코드 작성의 노력을 줄일 수 있다.

+ Certificates
  + Web을 HTTPS로 client에게 배포할 때, 암호화된 복잡한 객체 파일(?)이 발생
  + 이러한 certificates를 위한 비밀 보안 storage가 필요할 때 keyvault 사용 가능

Azure Key Vault의 장점 및 특징
-----
+ 민감한 보안 정보들에 대해 관리되는 서비스
  + 어플리케이션 build시 혹은 platform 제작 시에 발생하는 민감한 보안 정보들 관리 가능
	+ key, secrets, certificates 들에 대한 보안 storage 서비스

+ 애플리케이션 비밀 중앙 집중화(centralization)
	+ 중앙 집중식 스토리지 방식으로 배포 제어 가능
	+ 한 스토리지에 저장하는 방식으로 여러 군데 흩어지지 않고 쉽게 제어 가능
	+ 각 애플리케이션마다 보안 정보를 저장하지 않아도 됨
	+ 각 어플리케이션마다의 보아 정보 저장에 대한 수고 덜어줌
	+ 어플리케이션이 DB에 접근할 때 keyvaylt에 저장된 연결 문자열 사용 가능
	+ 어플리케이션은 URI를 사용하여 필요한 정보에 안전하게 액세스할 수 있다. 이러한 URI를 사용하면 어플리케이션이 특정 버전의 비밀을 검색할 수 있다.

+ 안전하게 비밀 및 키 저장
 	+ keyvault에 엑세스 하려면 호출자(사용자 또는 어플리케이션)가 액세스할 수 있도록 인증 및 권한 부여 필요
	+ 인증은 호출자의 ID확인, Azure Active Directory를 통해 수해됨. 
	+ 권한 부여는 수행할 수 있는 작업 결정, Azure RBAC(Azure 역할 기반 액세스 제어) 또는 Key vault 액세스 정책을 통해 수행

+ 액세스 사용 및 모니터링
	+ 언제, 누가, 어디서 나의 keyvault에 접근하는지에 대한 모니터링과 로깅이 잘 되어있음
+ Azure 서비스들과의 통합
	+ VMs, Logic Apps, Data Factory, WebApps..와 같은 다른 Azure 서비스들과 고도로 통합되어있다.

![]()
