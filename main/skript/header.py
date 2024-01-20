import requests


class Header:
    def __init__(self, url):
        self.url = url

    def req_send(self):
        url = self.url

        missed_header = []
        check_header = [
            "Content-Security-Policy",
            "Strict-Transpot-Security",
            "X-Frame-Options",
            "X-XSS-Protection",
            "X-Content-Type-Options",
            "Referrerr-Policy",
            "Content-Security-Policy-Report-Only"
        ]
        try:
            respone = requests.get(url)
            for head in check_header:
                if head.lower() in respone.headers:
                    pass
                else:
                    missed_header.append(head)
            print(missed_header)
            return missed_header
        except requests.exceptions.RequestException as e:
            print(f"Error accured")
            print(e)
            return None
