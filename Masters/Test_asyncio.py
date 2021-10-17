'''
    ###비동기식 코드 (asyncio) Test###
    동기식 함수와 비동기식 함수 비교
    사용자 조회 1명당 1초 소요된다고 가정
    $동기식 코드는 3명, 2명, 1명의 데이터를 조회한다고 할 때 3명의 데이터 처리가 끝나야 다음 2명의 데이터를 조회하는 식의 순차적 방식
    $비동기식 코드는 비동기적으로 수행되어 3명의 데이터가 조회되는 도중에도 다른 사용자의 데이터 처리 비동기적으로 진행
    비동기식 함수의 처리 과정이 동기식 함수의 처리 과정보다 훨씬 빠르고 효율적임을 확인.
'''

import time
import asyncio

#동기식 사용자 조회 함수 작성

def find_user_as_sync(n):
    for i in range(1, n + 1):
        print(f"{n}명 중 {i} 번 째 사용자 조회 중. . .")
        time.sleep(1)
    print(f"총 {n}명 user 동기식  조회 complete !!")

def process_sync():
    start = time.time()
    find_user_as_sync(3)
    find_user_as_sync(2)
    find_user_as_sync(1)
    end = time.time()
    print(f">>> 동기 처리 총 소요 시간 : {end - start}")

if __name__ == '__main__':
    process_sync()


#비동기식 사용자 조회 함수 작성

async def find_user_as_async(n):
    for i in range(1, n + 1):
        print(f"{n}명 중 {i} 번 째 사용자 조회 중. . .")
        await asyncio.sleep(1)
    print(f"총 {n}명 user 비동기식  조회 complete !!")

async def process_async():
    start = time.time()
    await asyncio.wait([
        find_user_as_async(3),
        find_user_as_async(2),
        find_user_as_async(1)
    ])
    end = time.time()
    print(f">>> 동기 처리 총 소요 시간 : {end - start}")

if __name__ == '__main__':
    asyncio.run(process_async())