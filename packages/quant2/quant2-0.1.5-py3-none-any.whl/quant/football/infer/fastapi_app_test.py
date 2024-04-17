import requests

# 发送 POST 请求
url = "http://localhost:8000/predictor"
data = {
    "model": "model1",
    "name": "example item",
    "description": "example description",
    "price": 99.99,
}
response = requests.post(url, json=data)

# 检查响应状态码
if response.status_code == 200:
    print("Request successful")
    print("Response body:", response.json())
else:
    print("Request failed")
    print("Response status code:", response.status_code)
