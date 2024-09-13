import pickle
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# Đường dẫn đến msedgedriver
edge_driver_path = "B:\\Documents\\DataScience Research(09 2024)\\edgedriver_win64\\msedgedriver.exe"

# Khởi tạo trình duyệt Edge
service = Service(executable_path=edge_driver_path)
browser = webdriver.Edge(service=service)

# 1. Mở trang đăng nhập
# Bước này tôi đăng nhập gián tiếp qua link này để lúc đăng nhập xong nó vào thẳng luôn đỡ qua trang chủ lại mất công tìm thẻ button để nhấn vào 
browser.get("https://www.kalodata.com/video/detail?id=7396229557373766919&language=vi-VN&currency=VND&region=VN&dateRange=%5B%222024-08-30%22%2C%222024-09-05%22%5D")

# Đợi để trang tải xong
sleep(2)

# 3. Nhập số điện thoại
try:
    phone_field = browser.find_element(By.ID, "register_phone")
    phone_field.clear()
    phone_field.send_keys("0904708498")  # Thay đổi số điện thoại nếu cần
except Exception as e:
    print(f"Không tìm thấy trường số điện thoại: {e}")

# 4. Nhập mật khẩu
try:
    password_field = browser.find_element(By.ID, "register_password")
    password_field.clear()
    password_field.send_keys("trongtiktok")  # Thay đổi mật khẩu nếu cần
except Exception as e:
    print(f"Không tìm thấy trường mật khẩu: {e}")

# 5. Nhấn vào nút đăng nhập
try:
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Log in')]")
    submit_button.click()
    sleep(2)  # Đợi trang tải xong
except Exception as e:
    print(f"Không tìm thấy nút đăng nhập (submit): {e}")

# 6. Điều hướng đến trang shop chi tiết sau khi đăng nhập
try:
    browser.get("https://www.kalodata.com/product/detail?id=1729577314986658654&language=vi-VN&currency=VND&region=VN")
    sleep(1)  # Đợi trang shop tải xong
except Exception as e:
    print(f"Không thể điều hướng đến trang sản phẩm: {e}")

# 7. Nhấn vào nút "Đã hiểu" để tắt thông báo
try:
    da_hieu_button = browser.find_element(By.XPATH, "//div[text()='Đã hiểu']")
    da_hieu_button.click()
    sleep(1)  # Đợi thông báo tắt

    # Chuyển sang tab mới sau khi nhấn 'Đã hiểu'
    browser.switch_to.window(browser.window_handles[-1])  # Chuyển sang tab mới (tab cuối cùng mở)
    print("Đã chuyển sang tab mới.")

    sleep(1)  # Đợi trang mới tải xong

    # Quay lại tab cũ
    browser.switch_to.window(browser.window_handles[0])  # Chuyển lại về tab đầu tiên
    print("Đã quay lại tab cũ.")
    sleep(1)
    
except Exception as e:
    print(f"Không tìm thấy nút 'Đã hiểu': {e}")

# Tìm hàng chứa dữ liệu
try:
    # Xác định thẻ <tr> theo class hoặc thuộc tính data-row-key
    row_element = browser.find_element(By.CSS_SELECTOR, 'tr[data-row-key="7133578070679127041"]')
    
    # Cào thông tin từ các cột bên trong <tr>
    # Cột 1: Thứ tự
    order = row_element.find_element(By.CSS_SELECTOR, 'td:nth-child(1) div').text
    
    # Cột 2: Thông tin người dùng (Tên và số lượng người theo dõi)
    username = row_element.find_element(By.CSS_SELECTOR, '.line-clamp-1').text
    followers = row_element.find_element(By.CSS_SELECTOR, '.text-base-999').text
    
    # Cột 3: Giá trị đầu tiên
    value_1 = row_element.find_element(By.CSS_SELECTOR, 'td:nth-child(3)').text
    
    # Cột 4: Giá trị thứ hai
    value_2 = row_element.find_element(By.CSS_SELECTOR, 'td:nth-child(4)').text
    
    # Cột 5: Giá trị thứ ba
    value_3 = row_element.find_element(By.CSS_SELECTOR, 'td:nth-child(5)').text
    
    # Cột 6: Giá trị thứ tư
    value_4 = row_element.find_element(By.CSS_SELECTOR, 'td:nth-child(6)').text

    # In kết quả
    print(f"Thứ tự: {order}")
    print(f"Người dùng: {username}")
    print(f"Số người theo dõi: {followers}")
    print(f"Giá trị 1: {value_1}")
    print(f"Giá trị 2: {value_2}")
    print(f"Giá trị 3: {value_3}")
    print(f"Giá trị 4: {value_4}")

except Exception as e:
    print(f"Có lỗi xảy ra khi cào dữ liệu: {e}")


#  đoạn này có thể dùng để lưu cookie để đỡ phải đăng nhâpj nhiều lần
# pickle.dump(browser.get_cookies(), open("my_cookie.pkl", "wb"))

# Đóng trình duyệt
browser.quit()
