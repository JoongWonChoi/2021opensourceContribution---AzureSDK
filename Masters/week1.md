Week1 - Python팀 issue 선정 및 issue 살펴보기
=======
선정 이슈
---------
+ ㅣAzure Storage Queueㅣ receive_messages infinite loop #17301 <https://github.com/Azure/azure-sdk-for-python/issues/17301>

## about issue
+ AZURE STORAGE의 큐인 **receive message** 함수가 무한 루프에 빠지는 상황에 대한 issue.
+ AZURE STORAGE의 큐인 **def receive message**는 받을 메시지의 최대 수를 제한 하는 방법이 없다.
+ 만약 지속적으로 새 메시지를 얻는 큐에 대하여 사용된다면, 추가 메시지에 대하여 query를 시도 할 것이므로 무한 루프에 갇힐 것이다.
+ 만약 서버리스환경에서 동작하면, 실행에 시간제한이 있는 경우 기능이 죽으면 잠재적 데이터 손실로 이어질 것이다.

## Azure Queue Storage란?
+ HTTP 또는 HTTPS를 사용하여 인증된 호출을 통해 전 세계 어디에서나 액세스할 수 있는 다수의 메시지를 저장하기 위한 서비스.
+ Queue에는 메시지 집합이 포함.
+ 모든 messages는 큐에 있어야 하고, 이름은 모두 소문자여야함.

## 기존 code review
+ azure-sdk-for-python/sdk/storage/azure-storage-queue/azure/storage/queue/_queue_client.py 
<https://github.com/Azure/azure-sdk-for-python/blob/1ca37b47d156ed76922835e7097ee55396bf2fc5/sdk/storage/azure-storage-queue/azure/storage/queue/_queue_client.py#L546>

+ **receive_message** 함수의 내용

::  큐로부터 메시지를 검색하면, 큐의 앞에서부터 한 메세지씩 지운다.   
::  반응은 메시지 내용과 **pop_receipt value**를 포함하는데, 이는 메시지를 삭제할 때 요구된다.   
::  메시지는 큐로부터 자동적으로 삭제되지는 않는다. 하지만 메시지가 검색되면, **visibility_timeout** 파라미터로 저징된 시간 간격동안 다른 사용자들한테 보이지 않는다.    
::  만약 key-암호화 키 혹은 resolver field가 로컬 서비스 객체에 설정되면, 메시지는 반환 되기 전에 해독(?)된다.   
- **visibility_timeout(int)** 키워드
    
1. 만약 지정되지 않으면 default는 0이다.   
2. 새로운 시간 제한 값을 설정하라 - 몇 초로 / 서버 시간에 맞춰서?   
3. 그 값은 0 이상이어야 하고, 7일보다 커서는 안된다.   
4. **visibility_timeout(int)** 은 만료 시간 이후에 값으로 설정될 수 없다.   
5. **visibility_timeout(int)** 은 time-to-live 값보다 작아야 한다.  

## issue에 대한 resolve

+ Added kwarg to limit number of messages received in Queues #18783 <https://github.com/Azure/azure-sdk-for-python/pull/18783>
+ 큐에 들어오는 메시지들의 수를 제한하기 위하여 keyword arguments를 추가하였다.
+ keyword arguments 즉 kwargs는 함수의 매개변수로써 인자 값을 **key = value** 값으로 받고자 할 때 사용된다.
+ 전달된 값은 dictionary 형태, 즉 {'key' : 'value'}와 같은 형태로 저장된다.

