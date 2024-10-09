import pandas as pd

# Đường dẫn đến file Excel
file_path = r'B:\Documents\Kỳ 1 - Năm 4\Nhập môn Khoa Học Dữ Liệu\BTL\Project_E-Commerce Growth Analysis(TikTokShop)\Data\Creator_chuaCH_1thang.xlsx'

# Đọc file Excel
df = pd.read_excel(file_path)

# Kiểm tra xem cột "Rank" có tồn tại không
if 'Rank' in df.columns:
    # Tăng giá trị trong cột Rank lên 1
    df['Rank'] = df['Rank'] + 1
    
    # Ghi lại file Excel sau khi cập nhật
    df.to_excel(file_path, index=False)
    print("Đã tăng giá trị cột 'Rank' lên 1 và lưu lại file.")
else:
    print("Cột 'Rank' không tồn tại trong file Excel.")
