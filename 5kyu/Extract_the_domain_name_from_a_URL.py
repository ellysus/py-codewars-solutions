import re
def domain_name(url):
    return re.sub(r'(http:\/\/|https:\/\/|www\.)|(?=\.).*','',url)