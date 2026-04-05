import random

# Cấu hình số lượng bản ghi
NUM_STUDENTS = 1000000
NUM_COURSES = 1000000
NUM_ENROLLMENTS = 1000000

# Bộ từ vựng để sinh tên tiếng Việt ngẫu nhiên
first_names = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Vũ", "Đặng", "Bùi", "Đỗ", "Hồ"]
middle_names = ["Hải", "Văn", "Thị", "Minh", "Thanh", "Đức", "Ngọc", "Hữu", "Thu", "Hoài"]
last_names = ["Nam", "Anh", "Linh", "Hùng", "Cường", "Trang", "Tuấn", "Khoa", "Nhung", "Đạt"]

# 1. Sinh dữ liệu Course
def generate_courses():
    depts = ["CNTT", "ATTT", "DTVT", "PTDT"]
    subjects = ["Cơ sở dữ liệu", "Cấu trúc dữ liệu", "Lập trình Web", "Mạng máy tính", "Hệ điều hành", "Kinh tế chính trị Mác - Lênin", "Phát triển phần mềm"]

    with open('Course.txt', 'w', encoding='utf-8') as f:
        f.write('course_id,course_name,credits,dept_name\n')
        for i in range(1, NUM_COURSES + 1):
            course_id = f"INT{i:04d}"
            name = f"{random.choice(subjects)} {i}"
            credits = random.randint(2, 4)
            dept = random.choice(depts)
            f.write(f"{course_id},{name},{credits},{dept}\n")
            
    print(f"✅ Đã tạo xong {NUM_COURSES} bản ghi Course.txt")

# 2. Sinh dữ liệu Student
def generate_students():
    with open('Student.txt', 'w', encoding='utf-8') as f:
        f.write('student_id,full_name,class_name,email,phone\n')
        for i in range(1, NUM_STUDENTS + 1):
            student_id = f"B23DCCE{i:03d}"
            full_name = f"{random.choice(first_names)} {random.choice(middle_names)} {random.choice(last_names)}"
            class_name = f"D23CQCN{random.randint(1, 15):02d}-B"
            email = f"{student_id.lower()}@student.edu.vn"
            phone = f"09{random.randint(10000000, 99999999)}"
            f.write(f"{student_id},{full_name},{class_name},{email},{phone}\n")
            
    print(f"✅ Đã tạo xong {NUM_STUDENTS} bản ghi Student.txt")

# 3. Sinh dữ liệu Enrollment
def generate_enrollments():
    semesters = ["20231", "20232", "20241", "20242", "20251"]
    
    with open('Enrollment.txt', 'w', encoding='utf-8') as f:
        f.write('student_id,course_id,semester,score\n')
        for _ in range(1, NUM_ENROLLMENTS + 1):
            student_id = f"B23DCCE{random.randint(1, NUM_STUDENTS):03d}"
            course_id = f"INT{random.randint(1, NUM_COURSES):04d}"
            semester = random.choice(semesters)
            score = random.uniform(0, 10) # Điểm hệ 10
            f.write(f"{student_id},{course_id},{semester},{score:.1f}\n")
            
    print(f"✅ Đã tạo xong {NUM_ENROLLMENTS} bản ghi Enrollment.txt")

# Thực thi
if __name__ == "__main__":
    generate_courses()
    generate_students()
    generate_enrollments()