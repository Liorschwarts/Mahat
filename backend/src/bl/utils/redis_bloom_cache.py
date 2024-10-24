import redis
from functools import wraps
import pickle
import os
import logging

logger = logging.getLogger("uvicorn")

# Connect to Redis
redis_client = redis.Redis(
        host=os.getenv('REDIS_HOST', 'localhost'), 
        port=os.getenv('REDIS_PORT', 6379), 
        db=0
    )

def redis_bloom_cache(bloom_key, cache_key_prefix, expire_time=3600):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Generate a unique key for the function call
            call_key = pickle.dumps((func.__name__, args, kwargs))
            cache_key = f"{cache_key_prefix}:{call_key}"

            # Check if the key might exist in the Bloom filter
            if redis_client.execute_command('BF.EXISTS', bloom_key, call_key):
                logger.info("Bloom filter hit!")
                
                # If it might exist, try to get it from Redis cache
                cached_result = redis_client.get(cache_key)
                if cached_result:
                    logger.info("Cache hit!")
                    return pickle.loads(cached_result)
                else:
                    logger.info("Bloom filter false positive")
            else:
                logger.info("Bloom filter miss!")

            # If not in cache or Bloom filter, call the function
            result = await func(*args, **kwargs)

            # Store the result in Redis cache
            redis_client.setex(cache_key, expire_time, pickle.dumps(result))

            # Add the key to the Bloom filter
            redis_client.execute_command('BF.ADD', bloom_key, call_key)

            return result
        return wrapper
    return decorator

# Example usage
if __name__ == "__main__":
    @redis_bloom_cache('function_calls', 'cache_prefix', expire_time=3600)
    def example_function(a, b):
        print("Executing expensive operation")
        return a + b
        
    print(example_function(1, 2))  # First call, will execute the function
    print(example_function(1, 2))  # Second call, should be a cache hit
    print(example_function(3, 4))  # New parameters, will execute the function