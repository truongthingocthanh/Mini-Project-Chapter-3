import os
import json

# Khởi tạo bảng màu ANSI
class Mau:
    TIEU_DE = '\033[96m'     # Xanh lơ (Cyan) - Dùng cho Header/Menu
    THANH_CONG = '\033[92m'  # Xanh lá (Green) - Dùng cho thông báo thành công
    CANH_BAO = '\033[93m'    # Vàng (Yellow) - Dùng cho cảnh báo/nhập sai
    LOI = '\033[91m'         # Đỏ (Red) - Dùng cho lỗi nghiêm trọng
    IN_DAM = '\033[1m'       # In đậm chữ
    RESET = '\033[0m'        # Xóa định dạng màu (RẤT QUAN TRỌNG)

# Kích hoạt màu ANSI trên hệ điều hành Windows
os.system('')

# Khởi tạo danh sách menu rỗng
menu_quan = []

def hien_thi_menu_chinh():
    """Module hiển thị giao diện CLI có màu sắc"""
    print(f"\n{Mau.TIEU_DE}{Mau.IN_DAM}" + "="*40)
    print("☕ HỆ THỐNG QUẢN LÝ MENU QUÁN CÀ PHÊ ☕")
    print("="*40)
    print("1. Thêm món mới vào Menu")
    print("2. Hiển thị danh sách Menu")
    print("3. Tìm kiếm món (Theo Mã hoặc Tên)")
    print("4. Sắp xếp Menu (Theo giá hoặc Tên)")
    print("5. Thống kê cơ bản (Tổng số món, Giá TB)")
    print("6. Lưu dữ liệu (JSON) & Thoát")
    print("7. Xuất báo cáo ra file .txt") 
    print("="*40 + f"{Mau.RESET}") # Reset màu ở cuối

def nhap_mon_moi(menu):
    """
    Module Input & Validation
    Nhận tham số 'menu' (kiểu List) và cập nhật thêm món mới.
    """
    print(f"\n{Mau.TIEU_DE}{Mau.IN_DAM}" + "-"*15 + " THÊM MÓN MỚI " + "-"*15 + f"{Mau.RESET}")
    
    # 1. Nhập Mã Món (Kiểm tra trùng lặp và rỗng)
    while True:
        ma_mon = input("Nhập mã món (VD: CF01): ").strip().upper()
        if not ma_mon:
            print(f"{Mau.CANH_BAO}⚠ Mã món không được để trống!{Mau.RESET}")
            continue
            
        da_ton_tai = any(mon['ma_mon'] == ma_mon for mon in menu)
        if da_ton_tai:
            print(f"{Mau.CANH_BAO}⚠ Mã '{ma_mon}' đã tồn tại. Vui lòng nhập mã khác!{Mau.RESET}")
        else:
            break
            
    # 2. Nhập Tên Món (Kiểm tra trùng lặp và rỗng)
    while True:
        ten_mon = input("Nhập tên món (VD: Cà phê sữa): ").strip().title()
        if not ten_mon:
            print(f"{Mau.CANH_BAO}⚠ Tên món không được để trống!{Mau.RESET}")
            continue
            
        # Thuật toán chặn trùng Tên món:
        da_ton_tai_ten = any(mon['ten_mon'].lower() == ten_mon.lower() for mon in menu)
        if da_ton_tai_ten:
            print(f"{Mau.CANH_BAO}⚠ Món '{ten_mon}' đã có trong menu. Vui lòng nhập tên khác (VD: Bạc Xỉu Đá)!{Mau.RESET}")
        else:
            break 

    # 3. Nhập Danh mục (Kiểm tra rỗng)
    while True:
        danh_muc = input("Nhập danh mục (VD: Cà phê, Trà, Đá xay): ").strip().title()
        if not danh_muc:
            print(f"{Mau.CANH_BAO}⚠ Danh mục không được để trống!{Mau.RESET}")
        else:
            break
    
    # 4. Nhập Giá tiền 
    while True:
        try:
            gia_tien = float(input("Nhập giá tiền (Có thể nhập tắt, VD: 12 cho 12.000): "))
            
            if gia_tien <= 0:
                print(f"{Mau.CANH_BAO}⚠ Giá tiền phải lớn hơn 0!{Mau.RESET}")
            else:
                if gia_tien < 1000:
                    gia_tien = gia_tien * 1000
                
                if gia_tien >= 100000: 
                    gia_format_canh_bao = f"{gia_tien:,.0f}".replace(',', '.')
                    xac_nhan = input(f"{Mau.CANH_BAO}⚠ Giá món này lên tới {gia_format_canh_bao} VNĐ. Bạn có chắc không? (Y/N): {Mau.RESET}")
                    
                    if xac_nhan.strip().upper() != 'Y':
                        print(f"{Mau.TIEU_DE}ℹ Vui lòng nhập lại giá tiền.{Mau.RESET}")
                        continue # Quay lại vòng lặp bắt nhập lại từ đầu
                
                gia_format = f"{gia_tien:,.0f}".replace(',', '.')
                print(f"{Mau.THANH_CONG}   ↳ Đã ghi nhận giá: {gia_format} VNĐ{Mau.RESET}")
                break
                
        except ValueError:
            print(f"{Mau.LOI}⚠ Lỗi: Vui lòng chỉ nhập số!{Mau.RESET}")
            
    # 5. Đóng gói dữ liệu vào Dictionary và thêm vào List
    mon_moi = {
        'ma_mon': ma_mon,
        'ten_mon': ten_mon,
        'danh_muc': danh_muc,
        'gia_tien': gia_tien
    }
    
    menu.append(mon_moi)
    print(f"{Mau.THANH_CONG}✅ Đã thêm '{ten_mon}' vào menu thành công!{Mau.RESET}")
    return menu

def hien_thi_danh_sach(menu):
    """
    Module Display in ra dạng bảng
    """
    print("\n" + "="*66)
    print(f"{Mau.TIEU_DE}{Mau.IN_DAM}{'DANH SÁCH MENU QUÁN CÀ PHÊ':^66}{Mau.RESET}") 
    print("="*66)
    
    if len(menu) == 0:
        print("📭 Menu hiện đang trống! Hãy thêm món mới.")
        print("="*66)
        return

    # In Header của bảng (Đã được tô màu)
    print(f"{Mau.TIEU_DE}{Mau.IN_DAM}| {'Mã Món':<8} | {'Tên Món':<25} | {'Danh Mục':<12} | {'Giá Tiền':>8} |{Mau.RESET}")
    print("-" * 66)
    
    # In từng dòng dữ liệu
    for mon in menu:
        ma = mon['ma_mon']
        ten = mon['ten_mon']
        dm = mon['danh_muc']
        gia = mon['gia_tien']
        
        # Format giá tiền: dùng dấu phẩy phân cách ngàn, sau đó thay thế bằng dấu chấm
        gia_str = f"{gia:,.0f}".replace(',', '.')
        
        # Căn lề phải 8 ô cho biến gia_str
        print(f"| {ma:<8} | {ten:<25} | {dm:<12} | {gia_str:>8} |")
        
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
        print(f"{Mau.CANH_BAO}⚠ Lựa chọn không hợp lệ!{Mau.RESET}")

def thong_ke_menu(menu):
    """
    Module Statistics + Advanced Statistics (Gom nhóm dữ liệu)
    """
    print("\n" + "="*40)
    print(f"{Mau.TIEU_DE}{Mau.IN_DAM}{'BÁO CÁO THỐNG KÊ MENU':^40}{Mau.RESET}")
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
            json.dump(menu, file, ensure_ascii=False, indent=4)
        print(f"{Mau.THANH_CONG}💾 Đã lưu dữ liệu thành công vào file '{ten_file}'!{Mau.RESET}")
    except Exception as e:
        print(f"{Mau.LOI}⚠ Lỗi khi lưu file: {e}{Mau.RESET}")

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
        print(f"{Mau.LOI}⚠ Lỗi khi đọc file: Có thể file rỗng hoặc sai định dạng.{Mau.RESET}")

def xuat_bao_cao_txt(menu, ten_file="bao_cao_menu.txt"):
    """
    Module Report/File I/O 
    Xuất trạng thái hiện tại của dữ liệu ra tệp .txt.
    """
    if not menu:
        print(f"{Mau.CANH_BAO}⚠ Menu trống, không có gì để xuất báo cáo!{Mau.RESET}")
        return

    try:
        with open(ten_file, 'w', encoding='utf-8') as f:
            f.write("BÁO CÁO DANH SÁCH MENU QUÁN CÀ PHÊ\n")
            f.write("="*40 + "\n")
            f.write(f"{'Mã':<6} | {'Tên món':<20} | {'Giá tiền':>10}\n")
            f.write("-" * 40 + "\n")
            
            for mon in menu:
                gia_vn = f"{mon['gia_tien']:,.0f}".replace(',', '.')
                f.write(f"{mon['ma_mon']:<6} | {mon['ten_mon']:<20} | {gia_vn:>10} VNĐ\n")
            
            f.write("="*40 + "\n")
            f.write(f"Tổng cộng: {len(menu)} món.\n")
            
        print(f"{Mau.THANH_CONG}✅ Đã xuất báo cáo ra file '{ten_file}' thành công!{Mau.RESET}")
    except Exception as e:
        print(f"{Mau.LOI}⚠ Lỗi khi xuất file TXT: {e}{Mau.RESET}")

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
            print(f"{Mau.THANH_CONG}👋 Đã lưu dữ liệu. Tạm biệt và hẹn gặp lại!{Mau.RESET}")
            break
        elif lua_chon == '7':
            xuat_bao_cao_txt(menu_quan)
        else:
            print(f"{Mau.CANH_BAO}⚠ Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 6!{Mau.RESET}")

if __name__ == "__main__":
    main()