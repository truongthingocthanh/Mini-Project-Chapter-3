import os

# Khởi tạo danh sách menu rỗng
menu_quan = []

def hien_thi_menu_chinh():
    print("\n" + "="*40)
    print("☕ HỆ THỐNG QUẢN LÝ MENU QUÁN CÀ PHÊ ☕")
    print("="*40)
    print("1. Thêm món mới vào Menu")
    print("2. Hiển thị danh sách Menu")
    print("3. Tìm kiếm món (Theo Mã hoặc Tên)")
    print("4. Sắp xếp Menu (Theo giá hoặc Tên)")
    print("5. Thống kê cơ bản (Tổng số món, Giá TB)")
    print("6. Lưu dữ liệu & Thoát")
    print("="*40)

def nhap_mon_moi():
    print("\n--- THÊM MÓN MỚI ---")
    # TODO: Nhập ma_mon, ten_mon, danh_muc.
    # TODO: Dùng vòng lặp while để ép người dùng nhập đúng kiểu float cho gia_tien.
    pass

def hien_thi_danh_sach():
    print("\n--- DANH SÁCH MENU ---")
    if not menu_quan:
        print("Menu hiện đang trống!")
        return
    # TODO: Dùng f-string để căn lề (align) tạo thành dạng bảng đẹp mắt.
    pass

def luu_du_lieu(ten_file="menu_data.txt"):
    # TODO: Mở file chế độ 'w', duyệt qua menu_quan và ghi từng dòng.
    pass

def tai_du_lieu(ten_file="menu_data.txt"):
    """Đọc dữ liệu từ file TXT khi khởi động chương trình"""
    # TODO: Kiểm tra xem file tồn tại không (os.path.exists), nếu có thì đọc và append vào menu_quan.
    pass

def main():
    """Hàm điều phối trung tâm (Main Control Flow)"""
    tai_du_lieu() # Load dữ liệu ngay khi bật app
    
    while True: # Vòng lặp vô hạn duy trì chương trình
        hien_thi_menu_chinh()
        lua_chon = input("Vui lòng chọn chức năng (1-6): ")
        
        if lua_chon == '1':
            nhap_mon_moi()
        elif lua_chon == '2':
            hien_thi_danh_sach()
        elif lua_chon == '3':
            print("Đang phát triển tính năng Tìm kiếm...")
        elif lua_chon == '4':
            print("Đang phát triển tính năng Sắp xếp...")
        elif lua_chon == '5':
            print("Đang phát triển tính năng Thống kê...")
        elif lua_chon == '6':
            luu_du_lieu()
            print("Đã lưu dữ liệu. Tạm biệt!")
            break
        else:
            print("⚠ Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 6!")

if __name__ == "__main__":
    main()

    while True:
        try:
            gia_tien = float(input("Nhập giá tiền (VNĐ): "))
            if gia_tien <= 0:
                print("⚠ Giá tiền phải lớn hơn 0!")
            else:
                break # Thoát vòng lặp nếu nhập đúng số thực > 0
        except ValueError:
            print("⚠ Lỗi: Vui lòng chỉ nhập số, không nhập chữ cái!")