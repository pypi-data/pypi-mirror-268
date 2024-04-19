from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse


class Handle(BaseHTTPRequestHandler):
    def __init__(self, client_address, request, server):
        super().__init__(client_address, request, server)
        self._get: dict = {}
        self._post: dict = {}
        self._cookie: dict = {}

    def do_GET(self):
        # 由于每次连接都会有GET favicon.ico，避免多余的GET处理
        if self.path == '/favicon.ico':
            from ....image import PNGIconHebill
            icon = PNGIconHebill()
            self.send_response(200)
            self.send_header('Content-type', 'image/x-icon')
            self.end_headers()
            self.wfile.write(icon.bites)
        else:
            '''
            Host: 127.0.0.1:8000
            Connection: keep-alive
            Cache-Control: max-age=0
            sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"
            sec-ch-ua-mobile: ?0
            sec-ch-ua-platform: "Windows"
            Upgrade-Insecure-Requests: 1
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
            Sec-Fetch-Site: cross-site
            Sec-Fetch-Mode: navigate
            Sec-Fetch-User: ?1
            Sec-Fetch-Dest: document
            Accept-Encoding: gzip, deflate, br, zstd
            Accept-Language: en-US,en;q=0.9
            Cookie: order=id%20desc; memSize=12031; ltd_end=-1; pro_end=-1; soft_remarks=%7B%22list%22%3A%5B%22%u5BA2%u670D%u4F18%u5148%u54CD%u5E94%22%2C%2215%u5929%u65E0%u7406%u7531%u9000%u6B3E%22%2C%2215+%u6B3E%u4ED8%u8D39%u63D2%u4EF6%22%2C%22500%u6761%u514D%u8D39%u77ED%u4FE1%uFF08%u5E74%u4ED8%uFF09%22%2C%221%u5F20SSL%u5546%u7528%u8BC1%u4E66%uFF08%u5E74%u4ED8%uFF09%22%2C%22%u4E13%u4EAB%u4E13%u4E1A%u7248%u670D%u52A1%u7FA4%uFF08%u5E74%u4ED8%uFF09%22%5D%2C%22ltd_list%22%3A%5B%22%u66F4%u6362%u6388%u6743IP%22%2C%225%u5206%u949F%u6781%u901F%u54CD%u5E94%22%2C%2215%u5929%u65E0%u7406%u7531%u9000%u6B3E%22%2C%2230+%u6B3E%u4ED8%u8D39%u63D2%u4EF6%22%2C%2220+%u4F01%u4E1A%u7248%u4E13%u4EAB%u529F%u80FD%22%2C%221000%u6761%u514D%u8D39%u77ED%u4FE1%uFF08%u5E74%u4ED8%uFF09%22%2C%222%u5F20SSL%u5546%u7528%u8BC1%u4E66%uFF08%u5E74%u4ED8%uFF09%22%2C%22%u4E13%u4EAB%u4F01%u4E1A%u670D%u52A1%u7FA4%uFF08%u5E74%u4ED8%uFF09%22%5D%2C%22kfqq%22%3A%223007255432%22%2C%22kf%22%3A%22http%3A//q.url.cn/CDfQPS%3F_type%3Dwpa%26qidian%3Dtrue%22%2C%22qun%22%3A%221%22%2C%22activity_list%22%3A%5B%22%3Cspan%20style%3D%5C%22color%3A%23D98704%3Bpadding-right%3A10px%5C%22%3E618%u7279%u60E0%u6D3B%u52A8%uFF0C6%u670815-18%u65E5%uFF0C%u6700%u9AD8%u51CF4700%u5143%3C/span%3E%3Ca%20style%3D%5C%22text-decoration%3Anone%3B%5C%22%20href%3D%5C%22https%3A//www.bt.cn/618%5C%22%20rel%3D%5C%22noreferrer%5C%22%20%20target%3D%5C%22_blank%5C%22%20class%3D%5C%22btlink%5C%22%3E%u70B9%u51FB%u7ACB%u5373%u67E5%u770B%3E%3E%3C/a%3E%22%5D%2C%22kf_list%22%3A%5B%7B%22qq%22%3A%223007255432%22%2C%22kf%22%3A%22http%3A//q.url.cn/CDfQPS%3F_type%3Dwpa%26qidian%3Dtrue%22%7D%2C%7B%22qq%22%3A%222927440070%22%2C%22kf%22%3A%22http%3A//wpa.qq.com/msgrd%3Fv%3D3%26uin%3D2927440070%26site%3Dqq%26menu%3Dyes%26from%3Dmessage%26isappinstalled%3D0%22%7D%5D%2C%22wx_list%22%3A%5B%7B%22ps%22%3A%22%u5728%u7EBF%u5BA2%u670D%22%2C%22kf%22%3A%22https%3A//www.bt.cn/new/wechat_customer%22%7D%5D%7D; force=0; serverType=nginx; site_type=-1; request_token=7X7sXHXMeMMFG8JbelY39eat5ZHilnr5R18FGrCxSnAN1Fh6; SetName=; rank=list; sites_path=D%3A/BtServer/wwwroot/; Path=D%3A; ChangePath=4; bt_user_info=undefined; p5=2; site_model=php; softType=0; p0=1; bt_config=%7B%22webserver%22%3A%22nginx%22%2C%22sites_path%22%3A%22D%3A/BtServer/wwwroot/%22%2C%22backup_path%22%3A%22D%3A/backup%22%2C%22status%22%3Atrue%2C%22mysql_root%22%3A%22admin%22%2C%22email%22%3A%22admin@qq.com%22%2C%22distribution%22%3A%22Windows%2010%20Pro%20%28build%2022631%29%20x64%20%28Py3.8.6%29%22%2C%22request_iptype%22%3A%22ipv4%22%2C%22request_type%22%3A%22python%22%2C%22php%22%3A%5B%7B%22setup%22%3Atrue%2C%22version%22%3A%2254%22%2C%22max%22%3A%2250%22%2C%22maxTime%22%3A0%2C%22pathinfo%22%3Atrue%2C%22status%22%3Atrue%7D%2C%7B%22setup%22%3Atrue%2C%22version%22%3A%2274%22%2C%22max%22%3A%2250%22%2C%22maxTime%22%3A0%2C%22pathinfo%22%3Atrue%2C%22status%22%3Atrue%7D%5D%2C%22mysql%22%3A%7B%22setup%22%3Afalse%2C%22status%22%3Afalse%2C%22version%22%3A%22%22%7D%2C%22sqlserver%22%3A%7B%22setup%22%3Afalse%2C%22status%22%3Afalse%2C%22version%22%3A%22%22%7D%2C%22ftp%22%3A%7B%22setup%22%3Afalse%2C%22status%22%3Afalse%2C%22version%22%3A%22%22%7D%2C%22panel%22%3A%7B%22502%22%3A%22%22%2C%22port%22%3A%228888%22%2C%22address%22%3A%2258.216.190.118%22%2C%22domain%22%3A%22%22%2C%22auto%22%3A%22%22%2C%22limitip%22%3A%22%22%2C%22templates%22%3A%5B%5D%2C%22template%22%3A%22default%22%2C%22admin_path%22%3A%22/hebill%22%7D%2C%22systemdate%22%3A%222024-03-05%2010%3A57%3A33%22%2C%22show_workorder%22%3Atrue%2C%22isSetup%22%3Atrue%2C%22lan%22%3A%7B%22H1%22%3A%22%u9996%u9875%22%2C%22H2%22%3A%22%u7F51%u7AD9%u7BA1%u7406%22%2C%22SEARCH%22%3A%22%u7F51%u7AD9%u641C%u7D22%22%2C%22PS%22%3A%22%u4F7F%u7528%u5B9D%u5854Windows%u9762%u677F%u521B%u5EFA%u7AD9%u70B9%u65F6%u4F1A%u81EA%u52A8%u521B%u5EFA%u6743%u9650%u914D%u7F6E%uFF0C%u7EDF%u4E00%u4F7F%u7528www%u7528%u6237%u3002%22%2C%22BTN1%22%3A%22%u6DFB%u52A0%u7AD9%u70B9%22%2C%22BTN2%22%3A%22%u4FEE%u6539%u9ED8%u8BA4%u9875%22%2C%22BTN3%22%3A%22%u9ED8%u8BA4%u7AD9%u70B9%22%2C%22BTN4%22%3A%22%u5220%u9664%u9009%u4E2D%22%2C%22BTN5%22%3A%22%u5206%u7C7B%u7BA1%u7406%22%2C%22TH1%22%3A%22%u57DF%u540D%22%2C%22TH2%22%3A%22%u7F51%u7AD9%u72B6%u6001%22%2C%22TH3%22%3A%22%u5907%u4EFD%22%2C%22TH4%22%3A%22%u7F51%u7AD9%u76EE%u5F55%22%2C%22TH5%22%3A%22%u5230%u671F%u65E5%u671F%22%2C%22TH6%22%3A%22%u5907%u6CE8%22%2C%22TH7%22%3A%22%u64CD%u4F5C%22%2C%22JS1%22%3A%22%u8BF7%u5148%u5B89%u88C5Web%u670D%u52A1%u5668%21%22%2C%22JS2%22%3A%22%u53BB%u5B89%u88C5%22%7D%2C%22wx%22%3A%7B%7D%2C%22api%22%3A%22%22%2C%22ipv6%22%3A%22%22%2C%22basic_auth%22%3A%7B%22basic_user%22%3A%22%22%2C%22basic_pwd%22%3A%22%22%2C%22open%22%3Afalse%2C%22is_install%22%3Atrue%2C%22value%22%3A%22%u5DF2%u5173%u95ED%22%7D%2C%22show_recommend%22%3Atrue%2C%22debug%22%3A%22%22%2C%22auto_update_panel%22%3Afalse%2C%22public_key%22%3A%22-----BEGIN%20PUBLIC%20KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrg75/rlAbiS/ikQXkDShaBVlBW2O4OMrfo7E4yghDbDqey1FsubRxwjZgIEJ9pmgKruA2GCgEejDHI4NrzqkJpbGggHxXoZCu7zhSDO7elbw0ynht5pLEBjNOLasf4K12mpd3k9ynSN6CD2oCCXN1Yc63Wx3HrBci8ifXd0738wIDAQAB-----END%20PUBLIC%20KEY-----%22%7D
            '''
            '''
            {'order': 'id%20desc',
             'memSize': '12031',
             'ltd_end': '-1',
             'pro_end': '-1',
             'soft_remarks': '%7B%22list%22%3A%5B%22%u5BA2%u670D%u4F18%u5148%u54CD%u5E94%22%2C%2215%u5929%u65E0%u7406%u7531%u9000%u6B3E%22%2C%2215+%u6B3E%u4ED8%u8D39%u63D2%u4EF6%22%2C%22500%u6761%u514D%u8D39%u77ED%u4FE1%uFF08%u5E74%u4ED8%uFF09%22%2C%221%u5F20SSL%u5546%u7528%u8BC1%u4E66%uFF08%u5E74%u4ED8%uFF09%22%2C%22%u4E13%u4EAB%u4E13%u4E1A%u7248%u670D%u52A1%u7FA4%uFF08%u5E74%u4ED8%uFF09%22%5D%2C%22ltd_list%22%3A%5B%22%u66F4%u6362%u6388%u6743IP%22%2C%225%u5206%u949F%u6781%u901F%u54CD%u5E94%22%2C%2215%u5929%u65E0%u7406%u7531%u9000%u6B3E%22%2C%2230+%u6B3E%u4ED8%u8D39%u63D2%u4EF6%22%2C%2220+%u4F01%u4E1A%u7248%u4E13%u4EAB%u529F%u80FD%22%2C%221000%u6761%u514D%u8D39%u77ED%u4FE1%uFF08%u5E74%u4ED8%uFF09%22%2C%222%u5F20SSL%u5546%u7528%u8BC1%u4E66%uFF08%u5E74%u4ED8%uFF09%22%2C%22%u4E13%u4EAB%u4F01%u4E1A%u670D%u52A1%u7FA4%uFF08%u5E74%u4ED8%uFF09%22%5D%2C%22kfqq%22%3A%223007255432%22%2C%22kf%22%3A%22http%3A//q.url.cn/CDfQPS%3F_type%3Dwpa%26qidian%3Dtrue%22%2C%22qun%22%3A%221%22%2C%22activity_list%22%3A%5B%22%3Cspan%20style%3D%5C%22color%3A%23D98704%3Bpadding-right%3A10px%5C%22%3E618%u7279%u60E0%u6D3B%u52A8%uFF0C6%u670815-18%u65E5%uFF0C%u6700%u9AD8%u51CF4700%u5143%3C/span%3E%3Ca%20style%3D%5C%22text-decoration%3Anone%3B%5C%22%20href%3D%5C%22https%3A//www.bt.cn/618%5C%22%20rel%3D%5C%22noreferrer%5C%22%20%20target%3D%5C%22_blank%5C%22%20class%3D%5C%22btlink%5C%22%3E%u70B9%u51FB%u7ACB%u5373%u67E5%u770B%3E%3E%3C/a%3E%22%5D%2C%22kf_list%22%3A%5B%7B%22qq%22%3A%223007255432%22%2C%22kf%22%3A%22http%3A//q.url.cn/CDfQPS%3F_type%3Dwpa%26qidian%3Dtrue%22%7D%2C%7B%22qq%22%3A%222927440070%22%2C%22kf%22%3A%22http%3A//wpa.qq.com/msgrd%3Fv%3D3%26uin%3D2927440070%26site%3Dqq%26menu%3Dyes%26from%3Dmessage%26isappinstalled%3D0%22%7D%5D%2C%22wx_list%22%3A%5B%7B%22ps%22%3A%22%u5728%u7EBF%u5BA2%u670D%22%2C%22kf%22%3A%22https%3A//www.bt.cn/new/wechat_customer%22%7D%5D%7D',
             'force': '0', 
             'serverType': 'nginx', 
             'site_type': '-1', 
             'request_token': '7X7sXHXMeMMFG8JbelY39eat5ZHilnr5R18FGrCxSnAN1Fh6',
             'SetName': '',
             'rank': 'list',
             'sites_path': 'D%3A/BtServer/wwwroot/',
             'ChangePath': '4',
             'bt_user_info': 'undefined',
             'p5': '2',
             'site_model': 'php',
             'softType': '0',
             'p0': '1',
              'bt_config': '%7B%22webserver%22%3A%22nginx%22%2C%22sites_path%22%3A%22D%3A/BtServer/wwwroot/%22%2C%22backup_path%22%3A%22D%3A/backup%22%2C%22status%22%3Atrue%2C%22mysql_root%22%3A%22admin%22%2C%22email%22%3A%22admin@qq.com%22%2C%22distribution%22%3A%22Windows%2010%20Pro%20%28build%2022631%29%20x64%20%28Py3.8.6%29%22%2C%22request_iptype%22%3A%22ipv4%22%2C%22request_type%22%3A%22python%22%2C%22php%22%3A%5B%7B%22setup%22%3Atrue%2C%22version%22%3A%2254%22%2C%22max%22%3A%2250%22%2C%22maxTime%22%3A0%2C%22pathinfo%22%3Atrue%2C%22status%22%3Atrue%7D%2C%7B%22setup%22%3Atrue%2C%22version%22%3A%2274%22%2C%22max%22%3A%2250%22%2C%22maxTime%22%3A0%2C%22pathinfo%22%3Atrue%2C%22status%22%3Atrue%7D%5D%2C%22mysql%22%3A%7B%22setup%22%3Afalse%2C%22status%22%3Afalse%2C%22version%22%3A%22%22%7D%2C%22sqlserver%22%3A%7B%22setup%22%3Afalse%2C%22status%22%3Afalse%2C%22version%22%3A%22%22%7D%2C%22ftp%22%3A%7B%22setup%22%3Afalse%2C%22status%22%3Afalse%2C%22version%22%3A%22%22%7D%2C%22panel%22%3A%7B%22502%22%3A%22%22%2C%22port%22%3A%228888%22%2C%22address%22%3A%2258.216.190.118%22%2C%22domain%22%3A%22%22%2C%22auto%22%3A%22%22%2C%22limitip%22%3A%22%22%2C%22templates%22%3A%5B%5D%2C%22template%22%3A%22default%22%2C%22admin_path%22%3A%22/hebill%22%7D%2C%22systemdate%22%3A%222024-03-05%2010%3A57%3A33%22%2C%22show_workorder%22%3Atrue%2C%22isSetup%22%3Atrue%2C%22lan%22%3A%7B%22H1%22%3A%22%u9996%u9875%22%2C%22H2%22%3A%22%u7F51%u7AD9%u7BA1%u7406%22%2C%22SEARCH%22%3A%22%u7F51%u7AD9%u641C%u7D22%22%2C%22PS%22%3A%22%u4F7F%u7528%u5B9D%u5854Windows%u9762%u677F%u521B%u5EFA%u7AD9%u70B9%u65F6%u4F1A%u81EA%u52A8%u521B%u5EFA%u6743%u9650%u914D%u7F6E%uFF0C%u7EDF%u4E00%u4F7F%u7528www%u7528%u6237%u3002%22%2C%22BTN1%22%3A%22%u6DFB%u52A0%u7AD9%u70B9%22%2C%22BTN2%22%3A%22%u4FEE%u6539%u9ED8%u8BA4%u9875%22%2C%22BTN3%22%3A%22%u9ED8%u8BA4%u7AD9%u70B9%22%2C%22BTN4%22%3A%22%u5220%u9664%u9009%u4E2D%22%2C%22BTN5%22%3A%22%u5206%u7C7B%u7BA1%u7406%22%2C%22TH1%22%3A%22%u57DF%u540D%22%2C%22TH2%22%3A%22%u7F51%u7AD9%u72B6%u6001%22%2C%22TH3%22%3A%22%u5907%u4EFD%22%2C%22TH4%22%3A%22%u7F51%u7AD9%u76EE%u5F55%22%2C%22TH5%22%3A%22%u5230%u671F%u65E5%u671F%22%2C%22TH6%22%3A%22%u5907%u6CE8%22%2C%22TH7%22%3A%22%u64CD%u4F5C%22%2C%22JS1%22%3A%22%u8BF7%u5148%u5B89%u88C5Web%u670D%u52A1%u5668%21%22%2C%22JS2%22%3A%22%u53BB%u5B89%u88C5%22%7D%2C%22wx%22%3A%7B%7D%2C%22api%22%3A%22%22%2C%22ipv6%22%3A%22%22%2C%22basic_auth%22%3A%7B%22basic_user%22%3A%22%22%2C%22basic_pwd%22%3A%22%22%2C%22open%22%3Afalse%2C%22is_install%22%3Atrue%2C%22value%22%3A%22%u5DF2%u5173%u95ED%22%7D%2C%22show_recommend%22%3Atrue%2C%22debug%22%3A%22%22%2C%22auto_update_panel%22%3Afalse%2C%22public_key%22%3A%22-----BEGIN%20PUBLIC%20KEY-----MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCrg75/rlAbiS/ikQXkDShaBVlBW2O4OMrfo7E4yghDbDqey1FsubRxwjZgIEJ9pmgKruA2GCgEejDHI4NrzqkJpbGggHxXoZCu7zhSDO7elbw0ynht5pLEBjNOLasf4K12mpd3k9ynSN6CD2oCCXN1Yc63Wx3HrBci8ifXd0738wIDAQAB-----END%20PUBLIC%20KEY-----%22%7D'}
            '''
            print(self.headers)
            headers = dict(self.headers)
            cookies = {}
            if 'Cookie' in headers:
                for key, morsel in SimpleCookie(headers['Cookie']).items():
                    cookies[key] = morsel.value
            q = urlparse(self.path).query
            get = {}
            if q:
                for p in q.split('&'):
                    k, v = p.split('=')
                    if get.get(k) is None:
                        get[k] = []
                    get[k].append(v)
            from ...features.request.core import Request
            request = Request(
                cookies,
                get,
                parse_qs(self.rfile.read(
                    int(self.headers['Content-Length']) if 'Content-Length' in self.headers else 0).decode('utf-8')),
                headers
            )
            print(request.cookie)
            print(request.get)
            print(request.post)
            print(request.headers)
            # 继续相关操作
            try:
                # 发送响应状态码
                self.send_response(200)
                # 设置响应头
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                # 响应内容
                self.wfile.write(b"Hello, world!")  # 将字符串转换为字节流并发送
            except ConnectionAbortedError as e:
                print("用户已经中断连接或其他异常:", e)

    def do_POST(self):
        pass

    def do_PUT(self):
        pass

    def do_DELETE(self):
        pass
