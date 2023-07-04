import tkinter as tk
from tkinter import messagebox
import time
from selenium.webdriver import Chrome

def cnpj_iteration(driver, cnpj_list, date_init, date_final):
    driver.get('https://www2.agencianet.fazenda.df.gov.br/')
    time.sleep(10)

    driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/a').click()
    time.sleep(10)

    driver.find_element_by_xpath('//*[@id="boxMainMenu"]/ul/li[2]/a').click()
    driver.find_element_by_xpath('//*[@id="coluna1"]/ul/li[8]/a').click()
    driver.find_element_by_xpath('//*[@id="coluna2"]/ul/li[5]/span/a/span[1]').click()
    time.sleep(20)

    for cnpj in cnpj_list:
        driver.find_element_by_xpath('//*[@id="CpfCnpj"]').click()
        driver.send_keys(cnpj)
        driver.find_element_by_xpath('//*[@id="DataInicio"]').click()
        driver.send_keys(date_init)
        driver.find_element_by_xpath('//*[@id="DataFim"]').click()
        driver.send_keys(date_final)
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div/div[2]/form/div[7]/div/button[2]').click()
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div[2]/div[1]/table/tbody/tr[1]/td[5]/a[2]/img').click()

    driver.quit()


def retrieve_nf():
    date_init = entry_date_init.get()
    date_final = entry_date_final.get()
    cnpj_input = entry_cnpj_list.get()
    cnpjs = cnpj_input.split(",")
    cnpj_list = [str(cnpj.strip()) for cnpj in cnpjs]
    driver = Chrome('/usr/lib/chromium-browser/chromedriver')

    try:
        cnpj_iteration(driver, cnpj_list, date_init, date_final)
        messagebox.showinfo("Success", "NF retrieval completed successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        driver.quit()


# Create tkinter window
window = tk.Tk()
window.title("NF_Auto")
window.geometry("400x300")

# Create labels for date init
label_date_init = tk.Label(window, text="Initial Date:")
label_date_init.pack()

# Create entry fields for date init
entry_date_init = tk.Entry(window)
entry_date_init.pack()

# create labels for date final
label_date_final = tk.Label(window, text="Final Date:")
label_date_final.pack()

# Create entry fields for date final
entry_date_final = tk.Entry(window)
entry_date_final.pack()

# Create labels for cnpj list
label_cnpj_list = tk.Label(window, text="CNPJ List (separated by commas):")
label_cnpj_list.pack()

# Create entry fields for cnpj list
entry_cnpj_list = tk.Entry(window)
entry_cnpj_list.pack()

# Create button
retrieve_button = tk.Button(window, text="Retrieve NF", command=retrieve_nf)
retrieve_button.pack()

# Run the tkinter event loop
window.mainloop()
