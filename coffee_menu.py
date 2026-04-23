import os
import json

# Khởi tạo danh sách menu rỗng
menu_quan = []

def hien_thi_menu_chinh():
    """Module hiển thị giao diện CLI"""
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

def nhap_mon_moi(menu):
    """
    Module Input & Validation
    Nhận tham số 'menu' (kiểu List) và cập nhật thêm món mới.
    """
    print("\n" + "-"*15 + " THÊM MÓN MỚI " + "-"*15)
    
    # 1. Nhập Mã Món (Kiểm tra trùng lặp và không được rỗng)
    while True:
        ma_mon = input("Nhập mã món (VD: CF01): ").strip().upper()
        if not ma_mon:
            print("⚠ Mã món không được để trống!")
            continue
            
        # Kiểm tra mã đã tồn tại chưa bằng List Comprehension
        da_ton_tai = any(mon['ma_mon'] == ma_mon for mon in menu)
        if da_ton_tai:
            print(f"⚠ Mã '{ma_mon}' đã tồn tại. Vui lòng nhập mã khác!")
        else:
            break # Thoát vòng lặp nếu mã hợp lệ
            
    # 2. Nhập Tên và Danh mục
    ten_mon = input("Nhập tên món (VD: Cà phê sữa): ").strip().title()
    danh_muc = input("Nhập danh mục (VD: Cà phê, Trà, Đá xay): ").strip().title()
    
    # 3. Nhập Giá tiền (Ép kiểu Float và kiểm tra > 0)
    while True:
        try:
            gia_tien = float(input("Nhập giá tiền (VNĐ): "))
            if gia_tien <= 0:
                print("⚠ Giá tiền phải lớn hơn 0!")
            else:
                break
        except ValueError:
            print("⚠ Lỗi: Vui lòng chỉ nhập số, không nhập chữ cái hoặc ký tự đặc biệt!")
            
    # 4. Đóng gói dữ liệu vào Dictionary và thêm vào List
    mon_moi = {
        'ma_mon': ma_mon,
        'ten_mon': ten_mon,
        'danh_muc': danh_muc,
        'gia_tien': gia_tien
    }
    
    menu.append(mon_moi)
    print(f"✅ Đã thêm '{ten_mon}' vào menu thành công!")
    return menu

def hien_thi_danh_sach(menu):
    """
    Module Display in ra dạng bảng
    """
    print("\n" + "="*66)
    print(f"{'DANH SÁCH MENU QUÁN CÀ PHÊ':^66}") 
    print("="*66)
    
    if len(menu) == 0:
        print("📭 Menu hiện đang trống! Hãy thêm món mới.")
        print("="*66)
        return

    # In Header của bảng
    print(f"| {'Mã Món':<8} | {'Tên Món':<25} | {'Danh Mục':<12} | {'Giá Tiền':>8} |")
    print("-" * 66)
    
    # In từng dòng dữ liệu
    for mon in menu:
        ma = mon['ma_mon']
        ten = mon['ten_mon']
        dm = mon['danh_muc']
        gia = mon['gia_tien']
        
        print(f"| {ma:<8} | {ten:<25} | {dm:<12} | {gia:>8,.0f} |")
        
    print("="*66)

def tim_kiem_mon(menu):
    """
    Module Search + Advanced Search (Khớp chuỗi con)
    """
    print("\n" + "-"*15 + " TÌM KIẾM MÓN " + "-"*15)
    if not menu:
        print("📭 Menu hiện đang trống!")
        return

    tu_khoa = input("Nhập Mã hoặc Tên món cần tìm: ").strip().lower()
    
    ket_qua_tim_kiem = []
    for mon in menu:
        if tu_khoa in mon['ma_mon'].lower() or tu_khoa in mon['ten_mon'].lower():
            ket_qua_tim_kiem.append(mon)
            
    if len(ket_qua_tim_kiem) > 0:
        print(f"\n🔍 Tìm thấy {len(ket_qua_tim_kiem)} kết quả phù hợp:")
        hien_thi_danh_sach(ket_qua_tim_kiem)
    else:
        print(f"❌ Không tìm thấy món nào chứa từ khóa '{tu_khoa}'.")

def sap_xep_menu(menu):
    """
    Module Sort 
    Sắp xếp in-place (thay đổi trực tiếp list gốc)
    """
    print("\n" + "-"*15 + " SẮP XẾP MENU " + "-"*15)
    if not menu:
        print("📭 Menu hiện đang trống!")
        return

    print("1. Sắp xếp theo Tên món (A-Z)")
    print("2. Sắp xếp theo Giá tiền (Thấp đến Cao)")
    chon = input("Chọn tiêu chí sắp xếp (1-2): ")

    if chon == '1':
        menu.sort(key=lambda x: x['ten_mon'])
        print("\n✅ Đã sắp xếp Menu theo Tên (A-Z).")
        hien_thi_danh_sach(menu)
    elif chon == '2':
        menu.sort(key=lambda x: x['gia_tien'])
        print("\n✅ Đã sắp xếp Menu theo Giá tiền (Tăng dần).")
        hien_thi_danh_sach(menu)
    else:
        print("⚠ Lựa chọn không hợp lệ!")

def thong_ke_menu(menu):
    """
    Module Statistics + Advanced Statistics (Gom nhóm dữ liệu)
    """
    print("\n" + "="*40)
    print(f"{'BÁO CÁO THỐNG KÊ MENU':^40}")
    print("="*40)
    
    if not menu:
        print("📭 Menu hiện đang trống! Không có dữ liệu để thống kê.")
        return

    tong_so_mon = len(menu)
    tong_gia = sum(mon['gia_tien'] for mon in menu)
    gia_trung_binh = tong_gia / tong_so_mon

    print(f"📊 Tổng số món đang bán: {tong_so_mon} món")
    print(f"💰 Mức giá trung bình: {gia_trung_binh:,.0f} VNĐ")
    
    print("\n📈 Phân bổ theo danh mục:")
    thong_ke_dm = {}
    for mon in menu:
        dm = mon['danh_muc']
        thong_ke_dm[dm] = thong_ke_dm.get(dm, 0) + 1
        
    for dm, so_luong in thong_ke_dm.items():
        print(f"   - {dm:<15}: {so_luong} món")
    print("="*40)

def luu_du_lieu(menu, ten_file="menu_data.json"):
    """Lưu dữ liệu cấu trúc JSON (1.0 Điểm Nâng cao)"""
    try:
        with open(ten_file, 'w', encoding='utf-8') as file:
            # indent=4 giúp file JSON tự động format đẹp mắt
            json.dump(menu, file, ensure_ascii=False, indent=4)
        print(f"💾 Đã lưu dữ liệu thành công vào file '{ten_file}'!")
    except Exception as e:
        print(f"⚠ Lỗi khi lưu file: {e}")

def tai_du_lieu(menu, ten_file="menu_data.json"):
    """Đọc dữ liệu từ file JSON"""
    if not os.path.exists(ten_file):
        print(f"ℹ Không tìm thấy file '{ten_file}'. Sẽ khởi tạo menu mới.")
        return

    try:
        with open(ten_file, 'r', encoding='utf-8') as file:
            du_lieu_json = json.load(file)
            menu.extend(du_lieu_json) # Đổ toàn bộ dữ liệu vào list
        print(f"📂 Đã tải thành công {len(menu)} món từ file '{ten_file}'.")
    except Exception as e:
        print(f"⚠ Lỗi khi đọc file: Có thể file rỗng hoặc sai định dạng.")

def main():
    """Hàm điều phối trung tâm (Main Control Flow)"""
    tai_du_lieu(menu_quan) 
    
    while True:
        hien_thi_menu_chinh()
        lua_chon = input("Vui lòng chọn chức năng (1-6): ").strip()
        
        if lua_chon == '1':
            nhap_mon_moi(menu_quan)
        elif lua_chon == '2':
            hien_thi_danh_sach(menu_quan)
        elif lua_chon == '3':
            tim_kiem_mon(menu_quan)
        elif lua_chon == '4':
            sap_xep_menu(menu_quan)
        elif lua_chon == '5':
            thong_ke_menu(menu_quan)
        elif lua_chon == '6':
            luu_du_lieu(menu_quan)
            print("👋 Đã lưu dữ liệu. Tạm biệt và hẹn gặp lại!")
            break
        else:
            print("⚠ Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 6!")

if __name__ == "__main__":
    main()