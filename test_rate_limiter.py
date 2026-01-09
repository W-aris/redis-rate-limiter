import time
import redis
from rate_limiter import RateLimiter

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

rate_limiter = RateLimiter(redis_client)

ip = "1.1.1.1"
route = "/payment"
max_requests = 3
window_seconds = 10

print("=== Fixed Window Rate Limiter Test ===", flush=True)

timestamps = [0, 3, 8, 9, 11]
previous = 0

for t in timestamps:
    time.sleep(t - previous)
    previous = t

    allowed = rate_limiter.allow_request(ip, route, max_requests, window_seconds)
    print(f"Time {t}s → {'ALLOWED' if allowed else 'BLOCKED'}", flush=True)
