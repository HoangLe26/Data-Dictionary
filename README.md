# HƯỚNG DẪN CHẠY DEMO - CHỦ ĐỀ 4: DATA DICTIONARY / SYSTEM CATALOG

## 1. THÔNG TIN CHUNG
- **Đơn vị:** Học viện Công nghệ Bưu chính Viễn thông (PTIT)
- **Bài tập:** Mô phỏng các cơ chế Storage Management
- **Chủ đề 4:** Data Dictionary / System Catalog
- **Mục tiêu:** Mô phỏng quá trình tra cứu và quản trị Metadata của hệ quản trị cơ sở dữ liệu (DBMS) thông qua System Catalog mà không cần truy xuất trực tiếp vào các file dữ liệu vật lý có kích thước lớn.

## 2. CẤU TRÚC THƯ MỤC
Để chương trình hoạt động đúng, vui lòng đảm bảo các file sau được đặt trong cùng một thư mục:
- `demo_final.py`: Mã nguồn Python mô phỏng trình quản trị xử lý truy vấn.
- `dictionary.json`: File đóng vai trò là System Catalog, chứa toàn bộ Metadata (cấu trúc, kiểu lưu trữ, index) của hệ thống.
- `Student.txt`: File dữ liệu vật lý chứa thông tin sinh viên.
- `Course.txt`: File dữ liệu vật lý chứa thông tin môn học.
- `Enrollment.txt`: File dữ liệu vật lý chứa thông tin đăng ký môn học.

## 3. YÊU CẦU HỆ THỐNG
- Python 3.6 trở lên.
- Thư viện mở rộng: `prettytable`.
- Để cài đặt thư viện `prettytable`, mở Terminal / Command Prompt và chạy lệnh sau:
  ```bash
  pip install prettytable
  ```

## 4. HƯỚNG DẪN CHẠY DEMO
- **Bước 1:** Mở Terminal hoặc Command Prompt.
- **Bước 2:** Dùng lệnh `cd` để di chuyển đến thư mục chứa file `demo_final.py`.
- **Bước 3:** Khởi chạy chương trình bằng lệnh sau:
  ```bash
  python demo_final.py
  ```

## 5. GIẢI THÍCH KẾT QUẢ DEMO (KỊCH BẢN BÁO CÁO)
Sau khi chạy lệnh, chương trình sẽ in ra 3 kết quả mô phỏng các truy vấn quản trị như yêu cầu của đề bài:

- **Truy vấn 1: Hệ thống có những bảng nào?** Chương trình đọc file `dictionary.json` và in ra danh sách 3 bảng (Student, Course, Enrollment) kèm theo kiểu lưu trữ và đường dẫn file vật lý tương ứng.
  
- **Truy vấn 2: Bảng Student có những cột gì?** Chương trình tra cứu Metadata để in ra chính xác 5 cột của bảng Student gồm: tên cột, kiểu dữ liệu, độ dài, dấu hiệu khóa chính (Primary Key) và chỉ mục (Index). Tất cả được thực hiện với thời gian 0ms mà không cần phải mở file `Student.txt` nặng gần 80MB để quét dữ liệu.
  
- **Truy vấn 3: Bảng nào đang lưu kiểu Heap hoặc Sequential?** Chương trình lọc từ System Catalog ra được bảng Student đang lưu kiểu Sequential (tuần tự theo ID), còn bảng Course và Enrollment được lưu kiểu Heap (không có thứ tự). Thông tin này giúp Bộ tối ưu hóa truy vấn (Query Optimizer) của DBMS đưa ra quyết định quét bảng hoặc sử dụng Index một cách hợp lý nhất.
