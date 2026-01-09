import redis

class RateLimiter:
    def __init__(self, redis_client):
        self.redis = redis_client

    def allow_request(self, ip_address, api_route, max_requests, window_seconds):
        key = f"rate_limit:{ip_address}:{api_route}"

        current_count = self.redis.incr(key)

        if current_count == 1:
            self.redis.expire(key, window_seconds)

        return current_count <= max_requests
