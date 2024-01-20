from flask import Flask, redirect, url_for, render_template, request
from skript import header,url_info,vun_xss
import json
import requests



app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    url = None
    ipaddress = None
    header_res = {"": ""}
    port_res = {"": ""}
    directors = {"none":"none"}

    if request.method == 'POST':
        url = request.form.get('url')

        header_info = header.Header(url) 
        # dirs_enum = enumration.Enum(url)
        urldata = url_info.Urlinfo(url)
        
        ipaddress = urldata.get_ip_address()
        header_res = header_info.req_send()
        port_res = urldata.port_scanner()
        # directors = dirs_enum.dir_enum()
        print(header_res)


        if header_res is None or header_info == '':
            header_res = 'No Result'

    return render_template("index.html",
                           header_info=header_res,
                           t_url=url,
                           ip_address=ipaddress,
                           port_res=port_res,
                           )

results = ["blue" , "waiting for command " , "" , ""]
@app.route("/p", methods=['GET', 'POST'])
def process_data():
    global results

    if request.method == 'POST':
        data = json.loads(request.data)
        #print(request.data.decode())
        content = data['content']
        path = data['path']
        meth = data['method']
        head = data['headers']

        func = vun_xss.Scan_res(path,content,head,meth)

        results[0] = func.req_send()[0]
        results[1] = func.req_send()[1]
        results[2] = func.req_send()[2]
        results[3] = func.req_send()[3]

   
        
    return "RELOADING"


    
@app.route("/vuln", methods=['GET', 'POST'])
def show_data():
    global results

    
    if request.method == "POST":
        print("wowww")

    return render_template(
            "vuln.html",
            card_color=results[0],
            card_text=results[1],
            link_address = results[2],
            payload = results[3]
            )


    



if __name__ == "__main__":
    app.run(debug=True)

