import asyncio
import aiohttp
import time
from datetime import datetime

BOT_API_URL = "https://api.telegram.org/bot<YOUR_TOKEN>/getMe" #Смотреть README.md
CONCURRENT_USERS = 10 
REQUESTS_PER_USER = 5 

async def send_request(session, user_id):
    """Имитация запроса пользователя"""
    try:
        start = time.time()
        async with session.get(BOT_API_URL) as response:
            status = response.status
            duration = time.time() - start
            return {'status': status, 'time': duration, 'user': user_id}
    except Exception as e:
        return {'status': 0, 'time': 0, 'error': str(e)}

async def load_test():
    print(f"🚀 Начало нагрузочного тестирования...")
    print(f"👥 Пользователей: {CONCURRENT_USERS}, Запросов на юзера: {REQUESTS_PER_USER}")
    
    start_time = time.time()
    results = []
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for user in range(CONCURRENT_USERS):
            for req in range(REQUESTS_PER_USER):
                tasks.append(send_request(session, user))
        
        results = await asyncio.gather(*tasks)
    
    total_time = time.time() - start_time
    
    success = sum(1 for r in results if r.get('status') == 200)
    avg_time = sum(r.get('time', 0) for r in results) / len(results) if results else 0
    rps = len(results) / total_time if total_time > 0 else 0
    
    print("\n📊 Результаты:")
    print(f"✅ Успешных запросов: {success}/{len(results)}")
    print(f"⏱ Среднее время ответа: {avg_time:.3f} сек")
    print(f"⚡ RPS (Requests Per Second): {rps:.2f}")
    print(f"🕒 Общее время: {total_time:.2f} сек")

if __name__ == '__main__':
    asyncio.run(load_test())