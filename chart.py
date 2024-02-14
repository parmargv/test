import requests_html
from requests_html import HTMLSession

session = HTMLSession()
response = session.get('https://chartink.com/screener/1-best-swing-trade-gvparmar')
# renders javascript
response.html.render()

for result in response.html.xpath('//*[@id="DataTables_Table_0"]/tbody/tr'):
    print(f'{result.text}\n')