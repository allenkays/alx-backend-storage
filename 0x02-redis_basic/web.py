import requests
import redis
import time

# Create a Redis client
redis_client = redis.Redis()

def cache_decorator(fn):
    """
    Decorator to cache the result of a function with an expiration time of 10 seconds.
    """

    def wrapper(url):
        # Check if the result is already cached
        cached_result = redis_client.get(url)
        if cached_result:
            return cached_result.decode("utf-8")

        # Invoke the original function
        result = fn(url)

        # Cache the result with an expiration time of 10 seconds
        redis_client.setex(url, 10, result)

        return result

    return wrapper

@cache_decorator
def get_page(url: str) -> str:
    """
    Get the HTML content of a given URL.

    Args:
        url: The URL to retrieve.

    Returns:
        The HTML content of the URL.
    """
    response = requests.get(url)
    return response.text

# Example usage
# url = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://www.example.com"
# content = get_page(url)
# print(content)
