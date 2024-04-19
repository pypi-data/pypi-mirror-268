from requests import get
from bs4 import BeautifulSoup
from colorama import Fore
from .tools import p_to_e_int, p_to_e_str

class irarz:
    def __init__(self):
        self.response = get("https://irarz.com").text
    def arz(self) -> dict:
        result = dict()
        html = BeautifulSoup(self.response, 'html.parser')
        result['dollar'] = p_to_e_int(html.find("span", id='usdmax').text)
        result['euro'] = p_to_e_int(html.find("span", id='price_eur').text)
        return result

    def arz_digial(self) -> dict:
        result = dict()
        html = BeautifulSoup(self.response, 'html.parser')
        result['btc'] = float(p_to_e_str(html.find('span', id='crypto-btc').text).replace("\n", "").replace(" ", "").replace(",", ""))
        result['eth'] = float(p_to_e_str(html.find('span', id='crypto-eth').text).replace("\n", "").replace(" ", "").replace(",", ""))
        result['ada'] = float(p_to_e_str(html.find('span', id='crypto-ada').text).replace("\n", "").replace(" ", "").replace(",", ""))
        result['doge'] = float(p_to_e_str(html.find('span', id='crypto-doge').text).replace("\n", "").replace(" ", "").replace(",", ""))
        result['xrp'] = float(p_to_e_str(html.find('span', id='crypto-xrp').text).replace("\n", "").replace(" ", "").replace(",", ""))
        result['trx'] = float(p_to_e_str(html.find('span', id='crypto-trx').text).replace("\n", "").replace(" ", "").replace(",", ""))
        return result

    def gold(self) -> dict:
        result = dict()
        html = BeautifulSoup(self.response, 'html.parser')
        result['coin'] = p_to_e_int(html.find('span', id='sekeb').text)
        result['half_coin'] = p_to_e_int(html.find('span', id='nim').text)
        result['quarter_coin'] = p_to_e_int(html.find('span', id='rob').text)
        result['gerami_coin'] = p_to_e_int(html.find('span', id='gerami').text)
        result['gold18'] = p_to_e_int(html.find('span', id='geram18').text)
        result['gold24'] = p_to_e_int(html.find('span', id='geram24').text)
        result['mesghal_gold'] = p_to_e_int(html.find('span', id='mesghal').text)
        return result

    def car(self) -> dict:
        result = dict()
        html = BeautifulSoup(get("https://irarz.com/car").text, "html.parser")
        all = html.find_all("div", {"class":"card"})
        for i in range(len(all)):
            company_name = all[i].find("div", {"class":"card-body"}).find("div", {"class":"text-center"}).h2.span.text
            company_logo = all[i].find("div", {"class":"card-body"}).find("div", {"class":"text-center"}).h2.img.attrs["src"]
            all_products = all[i].find("div", {"class":"card-body"}).find("table", {"class":"table table-striped"}).tbody.find_all("tr")
            products_list = []
            for i in range(len(all_products)):
                info = all_products[i].find_all("td")
                name = info[0].text
                model = p_to_e_int(info[1].text)
                price = p_to_e_int(info[2].span.text)
                products_list.append({"name":name, "model":model, "price":price})
            result[company_name] = {"logo":company_logo, "products":products_list}
        return result
