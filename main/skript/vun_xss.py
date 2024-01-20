import requests


class Scan_res:
    def __init__(self, url , cont , head , method):
        self.url = url
        self.cont = cont
        self.head = head
        self.method= method

    def req_send(self):

        return_value = []
        scripts = '<iframe src=javascript:alert(1)>'

        url = self.url
        content = self.cont
        hearder = self.head
        method = self.method
        new_path = ''
        new_content = ''
            
        if "yehaxss" in url:
            new_content = content
            new_path = url.replace("yehaxss", scripts)
                #print(new_path)
        elif "yehaxss" in content:
            new_path = url
            new_content = content.replace("yehaxss", scripts)
                #print(new_content)
        else:
            print("couldn't find form")

        
        if method == "POST" or method == "post":
            try:
                req = requests.post(new_path , headers=hearder , data=new_content)
                if scripts in req.content.decode():
                    return_value.append('red')
                    return_value.append('XSS Has Detected')
                    return_value.append(url)
                    return_value.append(scripts)
                    return return_value
                else:
                    return_value.append('blue')
                    return_value.append('XSS Not Detected')
                    return_value.append(url)
                    return_value.append(scripts)
                    return return_value

            except requests.exceptions.RequestException as e:
                print(f"Error accured")
                print(e)
                return "error"
        if method == "GET" or method == "get":
            try:
                req = requests.get(new_path, headers=hearder , params=new_content) 
                if scripts in req.content.decode():
                    return_value.append('red')
                    return_value.append('XSS Has Detected')
                    return_value.append(url)
                    return_value.append(scripts)
                    return return_value
                else:
                    return_value.append('blue')
                    return_value.append('XSS Not Detected')
                    return_value.append(url)
                    return_value.append(scripts)
                    return return_value

            except requests.exceptions.RequestException as e:
                print(f"Error accured")
                print(e)
                return "error"

        
        