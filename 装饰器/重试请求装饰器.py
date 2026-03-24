import time
import functools
import requests
from requests.exceptions import RequestException, ConnectionError, Timeout


def retry_request(max_retries=3, delay=1, exceptions=(RequestException,)):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 记录当前重试次数
            retry_count = 0
            while retry_count <= max_retries:
                try:
                    # 执行请求函数
                    return func(*args, **kwargs)
                except exceptions as e:
                    retry_count += 1
                    # 达到最大重试次数，抛出异常
                    if retry_count > max_retries:
                        raise RuntimeError(f"请求失败，已重试{max_retries}次，最终异常：{str(e)}") from e
                    # 未达到最大重试次数，等待后重试
                    print(f"请求失败：{str(e)}，将在{delay}秒后重试（第{retry_count}/{max_retries}次重试）")
                    time.sleep(delay)

        return wrapper

    return decorator

@retry_request(max_retries=2, delay=2, exceptions=(ConnectionError, Timeout, RequestException))
def get_url_content(url):
    """发送GET请求获取URL内容"""
    response = requests.get(url, timeout=3)
    response.raise_for_status()  # 触发HTTP状态码异常（如404、500等）
    return response.text

# 测试：请求一个不存在的URL（触发重试）
try:
    content = get_url_content("http://www.example-nonexistent-domain.com")
    print(content)
except RuntimeError as e:
    print(e)