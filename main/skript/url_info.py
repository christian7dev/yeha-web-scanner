import socket
from urllib.parse import urlparse
import nmap
import whois


class Urlinfo:
    def __init__(self, urls):
        self.url = urls

    def get_ip_address(self):

        url = self.url
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        try:
            dm_info = whois.whois(domain)
            return dm_info
        except:
            return f"{url} is not registered"

    def port_scanner(self):
        nm = nmap.PortScanner()
        url = self.url
        ipad = urlparse(url).netloc
        ip_addr = socket.gethostbyname(ipad)
        nm.scan(ip_addr, arguments='-Pn -sV -n --min-parallelism 10 --max-parallelism 30')
        
        result_port = {}

        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    result_port[port] = {'name' : nm[host][proto][port]['name'] , 'state' : nm[host][proto][port]['state'] , 'version' : nm[host][proto][port]['version'] }
        return result_port
