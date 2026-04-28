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

## Bảng tự đánh giá
STT,Tiêu chí chi tiết (Detailed Criteria),Minh chứng trong mã nguồn (Implementation Details),Điểm tự chấm
1,Hệ thống Menu CLI,Sử dụng vòng lặp vô hạn while True trong hàm main(). Xử lý các lựa chọn không hợp lệ (nhánh else) mà không gây dừng chương trình.,1.0 / 1.0
2,Nhập & Xác thực dữ liệu,"Hàm nhap_mon_moi() thực hiện kiểm tra mã/tên trống, trùng lặp và sử dụng try-except để chặn nhập chữ vào trường giá tiền.",1.0 / 1.0
3,Hiển thị dữ liệu,"Hàm hien_thi_danh_sach() in dữ liệu dưới dạng bảng, căn lề chuẩn xác bằng f-string và định dạng giá tiền VNĐ chuyên nghiệp.",1.0 / 1.0
4,Tìm kiếm cơ bản,Hàm tim_kiem_mon() cho phép tìm chính xác món ăn dựa trên Mã món hoặc Tên món.,1.0 / 1.0
5,Cơ chế Sắp xếp,Hàm sap_xep_menu() sử dụng lambda để sắp xếp danh sách theo Tên (A-Z) hoặc Giá tiền (Thấp đến Cao).,1.0 / 1.0
6,Tính toán cơ bản,"Hàm thong_ke_menu() tính toán chính xác tổng số lượng món, tổng giá trị menu và giá trung bình.",1.0 / 1.0
7,Xử lý tệp TXT,Hàm xuat_bao_cao_txt() lưu trạng thái dữ liệu hiện tại vào file báo cáo .txt với định dạng bảng đẹp mắt.,1.0 / 1.0
8,Logic phức tạp (Nâng cao),"Triển khai tìm kiếm theo chuỗi con (substring search) và thống kê phân loại số lượng món theo từng Danh mục (Cà phê, Trà, Đá xay...).",1.0 / 1.0
9,Lưu trữ JSON (Nâng cao),Sử dụng thư viện json để lưu (luu_du_lieu) và nạp (tai_du_lieu) dữ liệu dưới dạng cấu trúc .json chuyên nghiệp.,1.0 / 1.0
10,Git & Modular Code,Mã nguồn chia thành các hàm đơn nhiệm (Top-Down Design). Repository GitHub có 13 commits và file README hướng dẫn chi tiết.,1.0 / 1.0
,TỔNG CỘNG,Dự án hoàn thiện đầy đủ mọi yêu cầu từ cơ bản đến nâng cao.,10.0 / 10.0
