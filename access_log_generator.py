import random
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def access_log_generator():
    methods = ["GET", "POST", "HEAD", "PUT", "DELETE", "OPTIONS"]
    url = ["/", "/index.php", "/contacts", "/api/v1/users", "/catalog/items/", "/assets/css/style.css", 
           "/js/main.js", "/images/logo.png", "/favicon.ico", "/wp-admin/", "/wp-login.php", 
           "/.env", "/admin/config.php", "/robots.txt"]
    protocols = ["HTTP/1.1","HTTP/2.0", "HTTP/3"]
    answer_code = [200, 301, 304, 403, 404, 500, 502]
    answer_size = [0, 42, 154, 230, 2340, 4512, 8910, 124500, 2567000]
    sources = ["-", "https://google.com", "https://yandex.ru", "https://github.com", "https://mysite.com"]
    browsers = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
                "Mozilla/5.0 (compatible; Googlebot/2.1; +http://google.com)",
                "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com)"]
    
    zone = ZoneInfo("Europe/Moscow") # поменять текущий регион
    current_time = datetime.now(zone)
    
    with open("access.log", "w", encoding="utf-8") as file:
        for _ in range(10000):
            ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
            current_time += timedelta(seconds=random.randint(1, 10))
            time = current_time.strftime("%d/%b/%Y:%H:%M:%S %z")
            line = (
                f'{ip} - - [{time}] "{random.choice(methods)} {random.choice(url)} {random.choice(protocols)}" '
                f'{random.choice(answer_code)} {random.choice(answer_size)} "{random.choice(sources)}" '
                f'"{random.choice(browsers)}"\n'
            )

            file.write(line)