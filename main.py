# Starting of the program
############## ! Imports ##############
# ? Selenium --> For interacting with the web browser
from selenium import webdriver
from selenium.webdriver.common.by import By

# ? Time --> For pausing the program
from time import sleep

# ? Questionary --> For beautiful command line prompts
from questionary import text

# ? Os --> For clearing the screen
from os import system, name as OSNAME


############## ! Functions ##############
def spammer(link=None, number=None):
    while True:
        # ? Error Handling
        try:
            # ? If link/number not provided while calling function
            if link == None:
                link = text("Enter the link to the NGL you would like to crash: ").ask()
            if number == None:
                while True:
                    try:
                        number = int(text("Number of messages to spam: ").ask())
                        if number <= 0:
                            raise ValueError
                        break
                    except:
                        print("Please enter a number greater than zero.")

            # ? -1 as already running once
            number -= 1
            newnum = number
            print(newnum)

            # ? Making link proper
            if "https://ngl.link" not in link:
                if "ngl.link/" in link:
                    link = "https://" + link
                else:
                    link = "https://ngl.link/" + link

            # ? Starting the driver
            driver = webdriver.Chrome()

            # ? Opening the website
            driver.get(link)
            sleep(0.5)

            # ? Clicking random
            rand = driver.find_element(By.CLASS_NAME, "dice-button")
            rand.click()
            sleep(0.5)

            # ? Clicking send
            button = driver.find_element(By.CLASS_NAME, "submit")
            button.click()
            sleep(1)

            # ? Quitting incase finished
            if newnum == 0:
                system("clear" if OSNAME == "posix" else "cls")
                exit()

            # ? Doing multiple times
            for x in range(number):
                print(newnum)
                newnum -= 1
                # ? Opening the website
                driver.get(link)
                sleep(0.5)

                # ? Clicking random
                rand = driver.find_element(By.CLASS_NAME, "dice-button")
                rand.click()
                sleep(0.5)

                # ? Clicking send
                button = driver.find_element(By.CLASS_NAME, "submit")
                button.click()
                sleep(3)
        except:
            # ? Closing browser incase rate limited
            driver.close()

            # ? Quitting incase Zero
            if newnum == 0:
                print("Finished!")
                exit()

            # ? Restarting browser as closed
            print("Rate limited, bypassing!")
            sleep(5)
            spammer(link, newnum)


if __name__ == "__main__":
    system("clear" if OSNAME == "posix" else "cls")
    spammer("indusrumors2", 10)
