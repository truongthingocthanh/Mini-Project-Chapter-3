# Mini-Project-Chapter-3
# ☕ Hệ Thống Quản Lý Menu Quán Cà Phê

Đây là một dự án ứng dụng Console (CLI) được xây dựng bằng Python, áp dụng triết lý Lập trình Mệnh lệnh và Thủ tục (Imperative and Procedural Programming) nhằm quản lý thực đơn cho một quán cà phê.

## 🚀 1. Giới thiệu chương trình
Chương trình cho phép người dùng (nhân viên/quản lý) thực hiện các thao tác CRUD (Thêm, Đọc, Sửa, Xóa) trên danh sách đồ uống. Dữ liệu được lưu trữ cấu trúc dưới định dạng `JSON` và hỗ trợ xuất báo cáo thống kê ra tệp `TXT`. Giao diện dòng lệnh được tích hợp mã màu ANSI mang lại trải nghiệm trực quan, bắt mắt và dễ sử dụng.

## ⚙️ 2. Yêu cầu & Cách cài đặt
- **Yêu cầu hệ thống:** Máy tính cần cài đặt sẵn **Python**. Không yêu cầu cài đặt thêm thư viện ngoài (sử dụng thư viện chuẩn `os`, `json` của Python).
- **Cách cài đặt & Chạy chương trình:**
  1. Clone kho lưu trữ này hoặc tải file `coffee_menu.py` về máy.
  2. Mở Terminal (hoặc Command Prompt, PowerShell) tại thư mục chứa file.
  3. Gõ lệnh sau để khởi chạy:
     ```bash
     python coffee_menu.py
     ```
     Nếu có Visual Studio Code và VS code đã tích hợp các thư viện cũng như python. Có thể mở thư mục và chạy trực tiếp trên VS code.

## 📖 3. Cách sử dụng chương trình
Sau khi khởi chạy, chương trình sẽ tự động nạp dữ liệu từ file `menu_data.json` (nếu có) và hiển thị Bảng Menu chính gồm 9 lựa chọn. Nhập số từ `1` đến `9` để thao tác:
1. **Thêm món mới:** Nhập mã, tên, danh mục và giá. *(Mẹo: Có thể nhập tắt giá, vd: gõ `15` hệ thống sẽ tự động nhân lên thành `15.000 VNĐ`).*
2. **Hiển thị danh sách:** Xem toàn bộ thực đơn dưới dạng bảng được căn lề chuẩn xác.
3. **Tìm kiếm:** Gõ một đoạn khóa, hệ thống sẽ tìm các món có chứa từ khóa đó trong Mã hoặc Tên (Khớp chuỗi con, không phân biệt hoa thường).
4. **Sắp xếp:** Sắp xếp danh sách theo Tên món (A-Z) hoặc theo Giá tiền (Tăng dần).
5. **Thống kê:** Xem tổng số món, mức giá trung bình và báo cáo phân bổ số lượng món theo từng nhóm danh mục.
6. **Xóa món:** Nhập mã món để xóa. Hệ thống sẽ có chốt chặn hỏi xác nhận `Y/N` để tránh xóa nhầm.
7. **Sửa thông tin:** Nhập mã món để cập nhật. *(Mẹo: Có thể nhấn `Enter` bỏ qua nếu chỉ muốn giữ nguyên thông tin cũ của trường đó).*
8. **Lưu & Thoát:** Ghi đè trạng thái dữ liệu hiện tại vào file JSON và đóng chương trình một cách an toàn.
9. **Xuất báo cáo TXT:** Xuất toàn bộ bảng danh sách menu và tổng kết ra file `bao_cao_menu.txt` phục vụ mục đích in ấn hoặc báo cáo.

## 🧩 4. Cấu trúc các hàm (Modular Design)
Dự án được thiết kế theo kiến trúc **Top-Down**, chia nhỏ logic thành các hàm (module) độc lập, truyền dữ liệu qua tham số để tránh hoàn toàn biến toàn cục (tránh Side-effects):
- `hien_thi_menu_chinh()`: Xử lý giao diện hiển thị các lựa chọn.
- `nhap_mon_moi(menu)`: Đảm nhận nhận Input, xác thực dữ liệu (chống rỗng, chống trùng lặp mã/tên, ép kiểu số thực, cảnh báo giá tiền quá cao).
- `hien_thi_danh_sach(menu)`: Format dữ liệu thành cấu trúc bảng, xử lý dấu chấm ngăn cách hàng ngàn chuẩn Việt Nam.
- `tim_kiem_mon(menu)`: Xử lý logic tìm kiếm chuỗi con.
- `sap_xep_menu(menu)`: Thao tác sắp xếp danh sách trực tiếp (in-place) sử dụng hàm ẩn danh `lambda`.
- `thong_ke_menu(menu)`: Tính toán cơ bản và thu thập dữ liệu gom nhóm (Grouping) bằng Dictionary.
- `xoa_mon(menu)` & `sua_mon(menu)`: Thao tác tìm kiếm, cập nhật và xóa phần tử trong danh sách List.
- `luu_du_lieu(menu, ten_file)` & `tai_du_lieu(menu, ten_file)`: Đảm nhận module File I/O làm việc với định dạng JSON.
- `xuat_bao_cao_txt(menu, ten_file)`: Ghi dữ liệu dạng văn bản cấu trúc bảng ra tệp TXT.
- `main()`: Hàm điều phối luồng điều khiển trung tâm (Main Control Flow).

## 🔄 5. Cách chương trình chạy (Luồng hoạt động)
Dự án vận hành theo mô hình vòng đời khép kín:
1. **Khởi động (Initialize):** Khi gọi file, hàm `main()` được kích hoạt. Máy tính chạy hàm `tai_du_lieu()` để nạp toàn bộ cấu trúc từ `menu_data.json` vào bộ nhớ RAM (biến List `menu_quan`).
2. **Vòng lặp tương tác (Interactive Loop):** Vòng lặp vô hạn `while True` liên tục vẽ lại menu và chờ người dùng nhập lệnh điều khiển.
3. **Điều hướng (Branching):** Dựa vào lựa chọn (1-9) của người dùng, khối `if/elif` sẽ gọi đến đúng hàm chuyên biệt để xử lý. Biến `menu_quan` được truyền liên tục giữa các hàm như một tham số.
4. **Kết thúc (Termination):** Khi người dùng chọn chức năng số `8`, hàm `luu_du_lieu()` được kích hoạt để "chụp" lại trạng thái cuối cùng của bộ nhớ, lưu đè xuống ổ cứng (JSON) trước khi gọi lệnh `break` để thoát hoàn toàn vòng lặp, kết thúc chương trình.
