from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import wikipedia
from webdriver_manager.chrome import ChromeDriverManager



#driver=webdriver.Chrome(r"E:\chromedriver.exe")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/search?gs_ssp=eJzj4tTP1TcwMU02T1JgNGB0YPBiS8_PT89JBQBASQXT&q=google&rlz=1C1CHZO_enIN945IN945&oq=goog&aqs=chrome.5.69i59j69i57j69i59l2j35i39j46i67i131i199i433i465j0i67i131i433j0i67j0i67i433j0i67i131i433.3051j0j15&sourceid=chrome&ie=UTF-8")
sleep(2)
def any_answer(x):
#    x=input("your question")
    clear=driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[3]/div[1]/div")
    clear.click()
    question=driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/div/div[2]/input")
    question.send_keys(x)
    search=driver.find_element(By.XPATH,"/html/body/div[4]/div[2]/form/div[1]/div[1]/div[2]/button")
    search.click()
    try:
        if x==x:
            answer=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[1]/a").text
            print(answer)
    except Exception:
        try:
            x=x
            GDP=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/block-component/div/div/div[1]/div/div/div[1]/div[1]/div/div[2]/div/div/div[1]/div").text
            print(GDP)
        except Exception:
            try:
                x=x
                army=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div").text
                print(army)
            except Exception:
                try:
                    x=x
                    box1=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/block-component/div/div[1]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]").text
                    print(box1)
   
                except Exception:
                    try:
                         x=x
                         math=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[12]/div[1]/div[2]/div/div/div[1]/div/div[1]/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div[1]").text
                         print(math)
                    except Exception:
                        try:
                            x=x
                            calc=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div[2]/div[2]/div/div/span").text
                            print(calc)
                        except Exception:
                            try:
                                x=x
                                place=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[1]/div[2]/div/div/div[1]/div/div[1]/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/div[1]").text
                                print(place)
                            except Exception:
                                try:
                                    x=x
                                    box=driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div[1]/div[2]/div/div/div[1]/div/div[1]/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/span/span").text
                                    print(box)
                                except Exception:
                                    try:
                                        x=x
                                        wiki=wikipedia.summary(x,sentences=2)
                                        print(wiki)
                                    except Exception :
                                        print("Sorry ! I don't understand ")
"""while True:
    any_answer()"""
    
        


# In[ ]:





# In[ ]:




