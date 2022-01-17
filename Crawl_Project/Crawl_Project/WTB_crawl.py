from selenium import webdriver
from tkinter import *
from urllib.parse import urlparse
from time import sleep

def crawlFinal():
    driver = webdriver.Chrome(
        "chromedriver.exe")
    # C:\\Users\\shubhan.patange\\Desktop\\chromedriver_win32\\chromedriver_win32\\

    driver.get("https://app.channeliq.com/Admin/JobCreator")

    username = driver.find_element_by_class_name("form-control")
    username.send_keys("shubhan.patange@numerator.com")

    password = driver.find_element_by_id("Password")
    password.send_keys("Shubhan*1996")

    sign_in = driver.find_element_by_id("login-btn")
    sign_in.click()

    driver.implicitly_wait(1000)

    links_final = links_entry.get(1.0,END)
    urls = links_final.split("\n")

    driver.get("https://app.channeliq.com/Admin/JobCreator")

    links_input = driver.find_element_by_id("urls")
    links_input.send_keys(urls[0])

    crawl_final = driver.find_element_by_xpath("//button[@type='submit']")
    crawl_final.click()

    sleep(3)

    retailer_name = driver.find_element_by_xpath("(//div[@class='row clearfix'])[2]/div[1]").text.split("\n")[0]
    print(retailer_name)

    done = []
    for i in urls:
        if i == "":
            urls.pop(urls.index(i))
        else:
            i = i + "\n"
            done.append(i)

    integer = No_link.get()
    conv_integer = int(integer)

    integer2 = Repeat.get()
    conv_integer2 = int(integer2)

    done_final = [done[x:x + conv_integer] for x in range(0, len(done), conv_integer)]

    for j in done_final:
        for i in range(conv_integer2):
            driver.get("https://app.channeliq.com/Admin/JobCreator")

            links_input = driver.find_element_by_id("urls")
            links_input.send_keys(j)

            sleep(1)

            dropdown_input = driver.find_element_by_class_name("k-select")
            dropdown_input.click()

            sleep(2)

            client_input = driver.find_element_by_class_name("k-textbox")
            client_input.send_keys(retailer_name)

            sleep(1)
            substring = "'"
            if substring in retailer_name:
                splitting = retailer_name.split("'")
                test_selection = "//div[@class='k-list-scroller']/ul/li[starts-with(text(),'" + splitting[0] + "')]"
            else:
                test_selection = "//div[@class='k-list-scroller']/ul/li[contains(text(),'" + retailer_name + "')]"

            client_final=driver.find_element_by_xpath(test_selection)
            client_final.click()

            sleep(0.5)

            crawl_final = driver.find_element_by_xpath("//button[@type='submit']")
            crawl_final.click()

            sleep(3)

            #back_again = driver.find_element_by_xpath("//div[@class='admin-page-wrapper']")
            #back_again.click()

    driver.quit()
    win.destroy()




win = Tk()

links_label=Label(win, text="Enter the URL")
links_label.grid(row=2, column=0)

links_entry = Text(win)
links_entry.grid(row=2,column=1)


No_link_label = Label(win, text="How many links at one crawl?")
No_link_label.grid(row=3, column=0)

No_link = Entry(win)
No_link.grid(row=3,column=1)

Repeat_label = Label(win, text="How many times to repeat?")
Repeat_label.grid(row=4, column=0)

Repeat = Entry(win)
Repeat.grid(row=4,column=1)

Crawl = Button(win, text= "Crawl", command=crawlFinal)
Crawl.grid(row=5, column=1)


win.mainloop()
