import json
from prettytable import PrettyTable

def load_catalog(file_path='dictionary.json'):
    """Tải dữ liệu từ Data Dictionary"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['system_metadata']
    except FileNotFoundError:
        print("Lỗi: Không tìm thấy file dictionary.json!")
        return None

def show_all_tables(catalog):
    """Truy vấn 1: Hệ thống có những bảng nào?"""
    print("\nQUYẾN QUẢN TRỊ: LIỆT KÊ DANH SÁCH CÁC BẢNG")
    table = PrettyTable(["STT", "Tên Bảng", "Kiểu Lưu Trữ", "Đường Dẫn File"])
    table.align = "l" # Căn lề trái
    
    for i, t in enumerate(catalog['tables'], 1):
        table.add_row([i, t['table_name'], t['storage_type'], t['file_path']])
    print(table)

def show_student_columns(catalog):
    """Truy vấn 2: Bảng Student có những cột gì?"""
    print("\nQUYẾN QUẢN TRỊ: CẤU TRÚC CHI TIẾT BẢNG 'STUDENT'")
    table = PrettyTable(["Cột", "Kiểu Dữ Liệu", "Độ Dài", "Khóa Chính", "Index"])
    
    # Tìm bảng Student trong Catalog
    student_table = next((t for t in catalog['tables'] if t['table_name'] == 'Student'), None)
    
    if student_table:
        for col in student_table['columns']:
            table.add_row([
                col['column_name'], 
                col['data_type'], 
                col['length'], 
                "✔" if col['is_primary_key'] else "-",
                "✔" if col['has_index'] else "-"
            ])
        print(table)
    else:
        print("Không tìm thấy thông tin bảng Student.")

def show_storage_strategy(catalog):
    """Truy vấn 3: Bảng nào đang lưu kiểu Heap hoặc Sequential?"""
    print("\nQUYẾN QUẢN TRỊ: PHÂN LOẠI CHIẾN LƯỢC LƯU TRỮ")
    
    heap_tables = [t['table_name'] for t in catalog['tables'] if t['storage_type'].lower() == 'heap']
    seq_tables = [t['table_name'] for t in catalog['tables'] if t['storage_type'].lower() == 'sequential']
    
    print(f" HEAP STORAGE       : {', '.join(heap_tables) if heap_tables else 'Không có'}")
    print(f" SEQUENTIAL STORAGE : {', '.join(seq_tables) if seq_tables else 'Không có'}")

def main():
    catalog = load_catalog()
    if not catalog:
        return

    # Thực hiện 3 yêu cầu demo của thầy
    show_all_tables(catalog)
    show_student_columns(catalog)
    show_storage_strategy(catalog)

if __name__ == "__main__":
    main()