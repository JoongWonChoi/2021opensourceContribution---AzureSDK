Week5. New issue 확인하기
====
target issue: [Update async samples to use asyncio.run instead of loop · Issue #21207 · Azure/azure-sdk-for-python (github.com)]
--
Javascript => 애초에 비동기 프로그래밍 방식

-파이썬은 동기 방식, 따라서 웹 서버와 같은 어플리케이션 실행 시 CPU연산대 비 DB나 API와 연동 과정에서의 생성되는 대기시간이 훨씬 길다.
따라서 한 행위가 끝나야 다음 행위로 넘어가는 동기식 말고
비동기화 하여 각각의 연산 및 실행 시간에 맞춰 실행되게끔 만들어주기?
여러 작업을 동시에 수행할 수 있도록 해주는 것?

-코루틴과 스레드?

-비동기를 원하는 함수 앞에 async 붙이기
async def main_async():..

-async로 선언되지 않은 동기 함수 내에서 비동기 함수를 호출하려면
asyncio 라이브러리의 이벤트 루프 사용해야함

-동기 처리에서는 첫 번째 함수의 실행이 끝나야 두 번째 함수가 실행되고, 마찬가지로 두 번째 함수가 끝나야 세 번째 함수가 실행됩니다.
asyncio.run()
