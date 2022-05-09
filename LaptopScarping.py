#-----/////////Here You can Also save Product details in MS EXCEL FILE//////////////////-----
#import pandas as pd
#-----/////////Here You can Also save Product details in MS EXCEL FILE//////////////////-----
import requests
from bs4 import BeautifulSoup

#-----Input Var
search=input('Search Product : ')

#BaseUrl



#url="https://www.newegg.com/RTX-Studio-Laptops/Store/ID-1562?cm_sp=Cat_Laptops_1-_-TopNav-_-RTX-Studio-Laptops"
url="https://www.newegg.com/p/pl?d={search}"

webContent=requests.get(url)
doc = BeautifulSoup(webContent.text, "html.parser")

# lapName = [doc.find_all("a", attrs={'class':"item-title"})]
# img  = [x.get_text() for x in doc.find_all("img", attrs={'class':"checkedimg"})]
price = [x.parent.find("strong").get_text() for x in doc.find_all(text="$")]
product  = [x.get_text() for x in doc.find_all("a", attrs={'class':"item-title"})]

#TODO:Change here Title of 
TITLE="Mobiles"
productDetails={'Laptop':product,'Price':price}
print(productDetails)
# productDetails={'Laptop':product,'Price':price,'IMAGE':img}


#-----/////////Here You can Also save Product details in MS EXCEL FILE//////////////////-----
#Here Creating csv file with pandas

#df=pd.DataFrame(productDetails)
#df.to_csv(f'{TITLE}InNewegg.csv')



    
