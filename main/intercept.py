from mitmproxy import (
    ctx,
    http
)
import requests
import json

class RequestCapturer:
    def request(self, flow: http.HTTPFlow) -> None:
        # Retrieve request header
        header = flow.request.data

        # print("=="*20)
        # print(flow.request.url)
        # print("=="*20)

        # Retrieve request body
        #body = flow.request.content.decode()

        url = 'http://127.0.0.1:5000/p' 

        if b'yehaxss' in header.path or b'yehaxss' in header.content:
            data = {
                "headers" : dict(header.headers),
                "content" : header.content.decode(),
                "path" : flow.request.url,
                "method" : flow.request.method
                
            }

            json_data = json.dumps(data)
            requests.post(url , data=json_data)
        # Display header and body
        # print('--- Request Header ---')
        # print(json_data)
        # for key, value in header.items():
        #     print(f'{key}: {value}')
        # print('--- Request Body ---')
        # print(body)

addons = [
    RequestCapturer()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-s', __file__])