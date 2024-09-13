import scipy.stats as stats
import numpy as np

# Thông tin bài toán
x_bar = 8900  # Trung bình mẫu
sigma = 500    # Độ lệch chuẩn của tổng thể
n = 15         # Kích thước mẫu
confidence_level = 0.95  # Mức tin cậy

# Tính giá trị z từ phân phối chuẩn tắc
z_alpha = stats.norm.ppf(1 - (1 - confidence_level) / 2)

# Tính khoảng tin cậy
margin_of_error = z_alpha * (sigma / np.sqrt(n))
lower_bound = x_bar - margin_of_error
upper_bound = x_bar + margin_of_error

print(f"Khoảng tin cậy {confidence_level * 100}% cho tuổi thọ trung bình là ({lower_bound:.2f}, {upper_bound:.2f})")
