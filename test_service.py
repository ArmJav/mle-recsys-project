import requests
import random as rd
import logging

# базовая настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("tests.log", encoding="utf-8"),  # логи в файл
        logging.StreamHandler()                              # вывод в консоль
    ]
)

logger = logging.getLogger(__name__)

recommendations_url = "http://127.0.0.1:8000"
features_store_url = "http://127.0.0.1:8010"


headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

user_list = [1000004, 1000005, 1000007, 1000009, 1000011, 1000013, 1000014,
       1000015, 1000019, 1000023, 1000025, 1000026, 1000028, 1000029,
       # 1000032, 1000037, 1000039, 1000047, 1000060, 1000062, 1000063,
       # 1000068, 1000072, 1000077, 1000079, 1000080, 1000083, 1000092,
       # 1000095, 1000101, 1000109, 1000110, 1000115, 1000122, 1000128,
       1000134, 1000135, 1000138, 1000139, 1000143, 1000144, 1000149]

ITER = 1
for user_id in user_list:

    params = {"user_id": user_id, 'k': 10}

    resp_offline = requests.post(recommendations_url + "/recommendations_offline", headers=headers, params=params)
    resp_online = requests.post(recommendations_url + "/recommendations_online", headers=headers, params=params)
    resp_blended = requests.post(recommendations_url + "/recommendations", headers=headers, params=params)

    recs_offline = resp_offline.json()["recs"]
    recs_online = resp_online.json()["recs"]
    recs_blended = resp_blended.json()["recs"]
    logger.info(f"=== Тест №{ITER} для пользователя с id: {user_id} ===")
    logger.info(f"Оффлайн рекомендации: {recs_offline}")
    logger.info(f"Онлайн рекомендации: {recs_online}")
    logger.info(f"Смешанные рекомендации: {recs_blended}")
    ITER +=1
