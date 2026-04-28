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
STT,Tiêu chí chấm điểm (Theo đề bài),Minh chứng hoàn thành xuất sắc trong Code của bạn,Điểm tự chấm
1,"Hệ thống Menu CLI(Menu tương tác vòng lặp vô hạn, không văng lỗi khi nhập sai) ","Sử dụng vòng lặp while True ở hàm main(). Nếu người dùng nhập chữ hoặc số ngoài khoảng 1-9, hệ thống sẽ rơi vào nhánh else cảnh báo lỗi bằng màu ANSI vàng thay vì bị crash (văng lỗi).",1.0 / 1.0
2,"Nhập & Xác thực dữ liệu(Thêm bản ghi, xác thực kiểu dữ liệu chặn nhập chữ vào số) ","Hàm nhap_mon_moi() có tới 4 vòng lặp xác thực: chặn để trống, chặn trùng lặp mã/tên món. Đặc biệt, dùng try...except ValueError để chặn nhập chữ vào giá tiền một cách triệt để.",1.0 / 1.0
3,"Hiển thị dữ liệu(Căn lề chuẩn xác, cấu trúc bảng) ","Hàm hien_thi_danh_sach() định dạng bảng cực kỳ ngay ngắn bằng cú pháp căn lề f-string (:<8, :<25). Giá tiền được tự động chuyển đổi từ dấu phẩy sang dấu chấm chuẩn Việt Nam (15.000 VNĐ).",1.0 / 1.0
4,Tìm kiếm cơ bản(Tìm theo ID hoặc Tên) ,Hàm tim_kiem_mon() linh hoạt cho phép người dùng gõ cả mã món lẫn tên món để tra cứu.,1.0 / 1.0
5,Cơ chế Sắp xếp(Sắp xếp theo số học hoặc chữ cái) ,Hàm sap_xep_menu() cung cấp 2 tùy chọn: Sắp xếp theo Tên (chữ cái A-Z) và theo Giá tiền (số học). Áp dụng hàm ẩn danh lambda để tối ưu hóa thuật toán sắp xếp.,1.0 / 1.0
6,"Tính toán cơ bản(Tính tổng, trung bình, đếm) ","Hàm thong_ke_menu() đếm tổng số lượng món (len), tính tổng giá trị (sum) và tính ra mức giá trung bình của toàn bộ menu.",1.0 / 1.0
7,Xử lý tệp TXT(Lưu và tải dữ liệu .txt không mất) ,Hàm xuat_bao_cao_txt() hỗ trợ xuất trạng thái menu hiện tại ra file văn bản bao_cao_menu.txt dưới dạng bảng biểu chuyên nghiệp phục vụ in ấn báo cáo.,1.0 / 1.0
8,"[Nâng cao] Logic phức tạp(Tìm chuỗi con, lọc điều kiện, HOẶC thống kê nhóm) ","Vượt yêu cầu đề bài (Làm 2/3):- Tìm kiếm chuỗi con: Không phân biệt hoa thường với .lower() và toán tử in.- Thống kê nhóm: Dùng Dictionary để đếm số lượng món theo từng Nhóm danh mục (Cà phê, Trà...).",1.0 / 1.0
9,[Nâng cao] JSON/DBMS(Xuất nhập dữ liệu JSON hoặc SQLite) ,"Xây dựng 2 hàm luu_du_lieu và tai_du_lieu tích hợp thư viện json. Dữ liệu cấu trúc được lưu trữ bền vững vào menu_data.json, đảm bảo an toàn tắt/mở app.",1.0 / 1.0
10,"Git & Mã nguồn mô-đun(GitHub >=3 commits, chia hàm, không Spaghetti code) ","Dự án có README đầy đủ, GitHub có tới 13 commits. Mã nguồn áp dụng triệt để thiết kế Top-Down, chia thành 10 module hàm đơn nhiệm. Đặc biệt, truyền biến qua tham số để triệt tiêu hoàn toàn lỗi ""Side effects"".",1.0 / 1.0
,TỔNG CỘNG ĐIỂM TỰ ĐÁNH GIÁ:,"Sản phẩm hoàn thiện, logic chặt chẽ, tối ưu UX/UI.",10.0 / 10.0
