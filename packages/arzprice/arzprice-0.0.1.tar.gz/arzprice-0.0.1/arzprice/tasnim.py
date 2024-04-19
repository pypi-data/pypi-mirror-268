from requests import get
from bs4 import BeautifulSoup
from colorama import Fore
from .tools import p_to_e_int, p_to_e_str

class tasnim:
    def arz() -> dict:
        response = get("https://www.tasnimnews.com/fa/currency").text
        result = list()
        html = BeautifulSoup(response, "html.parser")
        all = html.find_all("div", {"class":"coins-container"})[-1].table.tbody.find_all("tr")
        for i in range(len(all)):
            info = all[i].find_all("td")
            name = info[0].text.replace("قیمت ", "")
            price = p_to_e_int(info[1].text)
            change = info[2].text
            low = p_to_e_int(info[3].text)
            high = p_to_e_int(info[4].text)
            update = p_to_e_str(info[5].text)
            result.append({"name":name, "price":price, "change":change, "low":low, "high":high, "update":update})
        return result