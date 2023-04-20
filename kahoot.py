import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

browser = uc.Chrome()

def login():

    browser.get('https://create.kahoot.it/creator')
    time.sleep(5)

    email = input('Type your email\n>')
    password = input('Type your password\n>')

    browser.find_element(By.ID, 'username').send_keys(email)
    browser.find_element(By.ID, 'password').send_keys(password)

    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, '#login-submit-btn').click()
    time.sleep(5)
    browser.find_element(By.CSS_SELECTOR, '#template-dialog > div > div.sc-IQBGL.kBsbmW > button').click()
    time.sleep(1)

def questions():

    question = input('Type your question\n>')

    firstanswer = input('Type your first answer option\n>')
    secondanswer = input('Type your second answer option\n>')
    thirdanswer = input('Type your third answer option\n>')
    fourthanswer = input('Type your fourth answer option\n>')

    browser.find_element(By.CSS_SELECTOR, '#question-text-field > div > div.DraftEditor-editorContainer > div > div > div > div').send_keys(question)

    browser.find_element(By.CSS_SELECTOR, '#question-choice-0 > div > div.DraftEditor-editorContainer > div > div').send_keys(firstanswer)
    browser.find_element(By.CSS_SELECTOR, '#question-choice-1 > div > div.DraftEditor-editorContainer > div > div > div > div').send_keys(secondanswer)
    browser.find_element(By.CSS_SELECTOR, '#question-choice-2 > div > div.DraftEditor-editorContainer > div > div > div > div').send_keys(thirdanswer)
    browser.find_element(By.CSS_SELECTOR, '#question-choice-3 > div > div.DraftEditor-editorContainer > div > div > div > div').send_keys(fourthanswer)

def new_slide():
    browser.find_element(By.CSS_SELECTOR, '#main-content > div.side-bar__SideBarActionsContainer-sc-1orx1s4-1.jxvSJQ > div.sc-hBAWal.iEXPxk > span > button').click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, 'body > div.add-new-button__PopupWrapper-sc-99yj7m-0.kERxXf > div:nth-child(2) > div > div.add-new-button__ScrollWrapper-sc-99yj7m-4.HHhhO > div > div > div > section:nth-child(1) > div > button:nth-child(1) > div.create-button__TextGroup-sc-1k1s17b-4.zlyIM > h3').click()

def kahoot():

    login()

    questions()

    time.sleep(3)

    new_slide()

    input()

kahoot()