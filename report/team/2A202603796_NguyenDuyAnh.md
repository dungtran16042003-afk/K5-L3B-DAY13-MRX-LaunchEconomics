# Báo cáo cá nhân — HoVaTen-MSSV

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên: Nguyen Duy Anh
- MSSV: 2A202603796
- Email: 26ai.anhnd15@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người viết code + người gắn nhãn 2

## 2. Phần việc phụ trách

- CP1 (Task A): Viết các hàm tính kinh tế chạy lại (A1), hàm `mo_hinh()` (A2), tính chi phí theo 4 loại yêu cầu (A3) và chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` (A4) trong `src/lab13.py`.
- CP2 (Task B): Viết code độ nhạy cho 9 kịch bản đơn lẻ (B1), kịch bản đổi cặp và xếp hạng 3 yếu tố (B2), giới hạn 1–3 lần chạy kèm chi phí hệ thống (B3), và xem lại 100% phạm vi `noi_dia` + `hang_nang` (B4).
- CP3 (Task C): Gắn nhãn độc lập 20 ca lỗi (ngồi tách nhau, không trao đổi trước khi so nhãn), so nhãn với TV1 và chốt quy tắc phân biệt các ca lệch.
- CP4–CP5 (Task D, E & Gate 2a): Kiểm số cỡ mẫu D1 và kiểm tra `yaml.safe_load` cho `report/team/pilot_plan.yaml`; rà soát `report/team/chi_so.md` và `report/team/ho_so_launch_v0.md`; tham gia chấm nhóm khác vào `report/team/phieu_cham.md`, phản biện Gate 2a và kiểm tra chạy lại `python3 lab13.py` trên máy khác trước khi nộp.

## 3. Đóng góp cụ thể

- Đưa cả 3 phép thử A1 (`1,20 · 1,25 · 1,25`) đạt `ĐẠT` trước khi chạy tính toán trên dữ liệu.
- Tính ra chi phí mỗi việc thành công gốc `4.472 đ` [simulated] (gấp `16,3 lần` hóa đơn token + tool chia số yêu cầu `274,7 đ`), tách được `noi_dia` (`2.696 đ` [simulated], `0,22x`) và `hang_nang` (`8.221 đ` [simulated], `0,69x`) so với `quoc_te` (`22.515 đ` [simulated], `1,88x`) và `doi_tac` (`10.215 đ` [simulated], `0,85x`), cùng mức cộng chi phí cố định `4.599 đ` [simulated] (quy mô đầy đủ) và `5.784 đ` [simulated] (khối lượng 50%).
- Xuất đủ số liệu độ nhạy B1–B4, xác định 3 yếu tố ảnh hưởng mạnh nhất: (1) số ca làm lại (`+51,8%` [simulated]), (2) tỉ lệ xem lại (`+40,7%` [simulated]), (3) lương nhân viên (`+23,1%` [simulated]), chỉ ra chi phí cả hệ thống thấp nhất ở tối đa 2 lần chạy (`6.901.220 đ` [simulated]) và mức chi phí khi xem lại 100% (`11.743 đ` [simulated] với 9 phút làm lại; `12.415 đ` [simulated] với `15,3` phút làm lại).
- Hoàn thành bộ nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR trước khi đối chiếu với TV1 và giữ nguyên bản nhãn độc lập sau khi so.

## 4. Bằng chứng
- f3ce482/70a6de8
- File code: `src/lab13.py` (các hàm A1, `mo_hinh`, tính A3, A4 và B1–B4).
- Output chạy từ `src/logix_runs.csv` và `src/logix_requests.csv`: 3 phép thử A1 in `ĐẠT`; `cps = 4,471.97 đ` [simulated]; bảng 9 kịch bản B1, cặp B2 (`6.543 đ`, `+46,3%` [simulated]), bảng B3 và B4.
- Bộ nhãn độc lập 20 ca lỗi phục vụ tổng hợp trong `report/team/bang_loi.md`, phiếu chấm duyệt chéo trong `report/team/phieu_cham.md`, và các commit push lên repo nhóm trước hạn.

## 5. Công cụ AI đã dùng

- Công cụ AI hỗ trợ giải thích công thức, gợi ý cấu trúc hàm trong `src/lab13.py`, giải thích nguyên nhân gốc các ca lỗi và soát lỗi code/định dạng.
- Cách tự kiểm tra: đối chiếu trực tiếp 3 assertion của A1; kiểm tra tính đối xứng giảm một nửa bằng nửa mức tăng ở B1, tính cộng gộp ở B2, bảo toàn tổng `1.200` yêu cầu ở B3, tính tay kiểm tra B4, chạy lại `python3 lab13.py` trên máy khác, và rà soát không còn từ `"production"` hay thiếu nhãn `simulated`.

## 6. Tự đánh giá

...