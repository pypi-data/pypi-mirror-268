import sys
from datetime import datetime, time
import time as t
import pyperclip
from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

class Reservation(Thread):
    # main_url = "https://reservation.nowonsc.kr/sports" # 신청 url 주소
    # fields_txt = { 12: "마들", 13: "초안산", 14: "불암산", 115: "수락산" }
    prod_mode = True

    def __init__(self, nowon_id, nowon_pwd, fields, dates, times):
        Thread.__init__(self)
        self.main_url = "https://reservation.nowonsc.kr/sports" # 신청 url 주소
        self.fields_txt = { 12: "마들", 13: "초안산", 14: "불암산", 115: "수락산" }
        self.nowon_id = nowon_id
        self.nowon_pwd = nowon_pwd
        self.fields = fields
        self.dates = dates
        self.times = times

    # create a session
    def CreateSession(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        #options.add_argument('--no-sandbox')
        #options.add_argument("--single-process")
        #options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) 
        #driver = webdriver.Chrome(service=service, options=options)

        # 크롬 버전 이슈로 오류 발생할 때 service, driver 대신 이 코드 사용
        #CHROMEDRIVER_PATH = './chromedriver'
        #driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)

        return driver

    def reservation(self):
        driver = self.CreateSession()
        if driver == None:
            return False
        print("create driver")

        try:
            driver.implicitly_wait(30)
            action = ActionChains(driver)
            driver.get(f"{self.main_url}/reserve_date?cate1=7&cate2={self.fields[0]}")

            # 1. 로그인 단계
            if WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'memberId'))):    
                driver.maximize_window()
                driver.find_element('id', 'memberId').send_keys(self.nowon_id)
                driver.find_element('id', 'memberPassword').send_keys(self.nowon_pwd)
                driver.find_element(By.CSS_SELECTOR,".btn_area > button").click()


                # 로그인 처리를 위해 딜레이 체크
                try:
                    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'password_old')))
                except TimeoutException:
                    pass

                # 최대한 가까운 시간부터 새로고침 하기 위해서 (트래픽이 높으면 벤처리 하는 것 같아서 추가함)
                target_time = time(9, 59, 59)
                while True:
                    now = datetime.now().time()
                    # 현재 시간과 목표 시간 비교
                    if now >= target_time:
                        break
                    # 1초 대기
                    print("작업 대기중")
                    t.sleep(1)

                print("작업 시작")

                # 구장 순서대로 하나씩 수행
                f_idx = 0
                while True:
                    if f_idx == len(self.fields):
                        break
                    
                    # 날짜 우선순위대로 하나씩 수행
                    d_idx = 0
                    while True:
                        print(f"예약시도: {self.fields_txt[self.fields[f_idx]]} / {self.dates[d_idx]}")

                        driver.get(f"{self.main_url}/reserve_date?cate1=7&cate2={self.fields[f_idx]}")
                        if WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".clndr-next-button"))):
                            
                            # 익월로 넘어가는 버튼
                            driver.find_element(By.CSS_SELECTOR,".clndr-next-button").click()

                            if WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"#reserve_{self.dates[d_idx]} .reserve"))):

                                # 예약날짜 조회
                                r_day = driver.find_element(By.CSS_SELECTOR, f"#reserve_{self.dates[d_idx]} .reserve")

                                # 아직 예약 안 열린 경우 날짜조회부터 다시
                                if(r_day.text == '준비중'):
                                    print("!!! 준비중")
                                    t.sleep(0.5)
                                    continue
                                
                                # 예약 시작
                                if(r_day.text == '예약가능'):
                                    # 날짜 선택
                                    r_day.click()
                                    
                                    if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, f"time_chk{self.times[0]}"))):
                                        r_possible = False
                                        time_chk = None
                                        time_txt = None

                                        for time_idx in range(len(self.times)):
                                            if driver.find_element(By.ID, f"time_chk{self.times[time_idx]}").is_enabled():
                                                r_possible = True
                                                driver.find_element(By.CSS_SELECTOR, f"#time_chk{self.times[time_idx]} + label").click()
                                                time_chk = driver.find_element(By.ID, f"time_chk{self.times[time_idx]}")
                                                break
                                            time_idx += 1

                                        if r_possible:
                                            if WebDriverWait(driver, 10).until(EC.element_to_be_selected(time_chk)):
                                                if time_chk.is_selected():
                                                    time_txt = time_chk.get_attribute("value")
                                                    driver.find_element(By.ID, "reserved_submit").click()
                                                    
                                                    alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
                                                    alert.accept()

                                                    capt = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "capt_cnt")))
                                                    action.double_click(capt).perform()
                                                    action.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
                                                    driver.find_element(By.ID, "value").send_keys(pyperclip.paste())
                                                    driver.find_element(By.ID, "capt_check").click()
                                                    try:
                                                        cpat_alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
                                                        cpat_alert.accept()
                                                    except Exception:
                                                        print("capt_alert error 재실행")
                                                        continue
                                                    
                                                    notice_confirm = driver.find_element(By.ID, "notice_confirm")
                                                    driver.execute_script("arguments[0].click();", notice_confirm)

                                                    driver.find_element(By.CSS_SELECTOR, ".btn_area button[type='submit']").click()
                                                    try:
                                                        WebDriverWait(driver, 3).until(EC.alert_is_present())
                                                        success_alert = driver.switch_to.alert
                                                        success_msg = success_alert.text
                                                        success_flag =  False
                                                        if(success_msg == '예약이 신청 되었습니다.'):
                                                            success_flag = True
                                                            
                                                        success_alert.accept()
                                                        if success_flag:
                                                            print(f"=== 예약완료: {self.fields_txt[self.fields[f_idx]]} / {self.dates[d_idx]} / {time_txt}")
                                                            d_idx += 1
                                                        
                                                    except Exception:
                                                        print("success_alert error 재실행")
                                                        continue
                                        else:
                                            print("!!! 예약마감(시간) ")
                                            d_idx += 1
                                else:
                                    print("!!! 예약마감(요일)")
                                    d_idx += 1
                                
                                if d_idx == len(self.dates):
                                    f_idx += 1
                                    break
        except Exception as e:
            print("Failed : " + str(e))
        finally:
            print('end')
            #driver.quit()

