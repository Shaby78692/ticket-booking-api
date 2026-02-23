import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration
URL = 'https://your-api-endpoint.com/api/booking'
NUM_USERS = 100

# User simulation function

def simulate_user(user_id):
    response = requests.post(URL, json={'user_id': user_id})
    return response.status_code, response.json()

# Load testing function

def load_test():
    with ThreadPoolExecutor(max_workers=NUM_USERS) as executor:
        futures = {executor.submit(simulate_user, user_id): user_id for user_id in range(1, NUM_USERS + 1)}
        for future in as_completed(futures):
            user_id = futures[future]
            try:
                status_code, result = future.result()
                print(f'User {user_id}: Status Code: {status_code}, Response: {result}')
            except Exception as e:
                print(f'User {user_id} generated an exception: {e}')

if __name__ == '__main__':
    start_time = time.time()
    load_test()
    end_time = time.time()
    print(f'Total time for load test: {end_time - start_time:.2f} seconds')
