# Báo cáo cá nhân — Nguyễn Tấn Dũng - 2A202603734

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tấn Dũng
- MSSV: 2A202603734
- Email: 26ai.dungnt15@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1, kiêm nhóm trưởng

## 2. Phần việc phụ trách

- Điều phối nhóm 3 người, chia việc, theo dõi điều kiện "Xong khi" của từng checkpoint.
- Nhiệm vụ C: gắn nhãn độc lập 20 ca lỗi (người gắn nhãn 1), cùng người gắn nhãn 2 chốt nhãn các ca lệch.
- Nhiệm vụ D: chủ `pilot_plan.yaml`.
- Nhiệm vụ E: chốt `ho_so_launch_v0.md` và đề xuất cuối; trình bày trước hội đồng Gate 2a.
- Điền `TEAM.md`, `group_report.md`; nộp link repo lên LMS.

## 3. Đóng góp cụ thể

- Viết `pilot_plan.yaml`: năm câu D1, năm câu D2, đánh đổi chấp nhận mức chênh 6 điểm, ba luật dừng (an toàn, chi phí, mức sử dụng) đủ bốn vế, phạm vi `noi_dia` + `hang_nang`, danh sách số giả lập.
- Gắn nhãn độc lập 20 ca lỗi; so với người gắn nhãn 2 được 15/20 = 75%; cùng nhóm chốt nhãn 5 ca lệch (3, 8, 9, 14, 19) và viết lại định nghĩa năm loại.
- Hoàn thiện `bang_loi.md` (bảng khắc phục 5 ca), mục 5 và 6 của `ho_so_launch_v0.md`, dòng đề xuất cuối (Go có điều kiện), `group_report.md`, `TEAM.md`.
- Chia việc cho nhóm 3 người và điều phối kéo `main` về trước khi push.

## 4. Bằng chứng

- Commit `03ff33d`, `e3b8070`: `report/team/pilot_plan.yaml`.
- Commit `877c3c7`: `TEAM.md`, báo cáo cá nhân, `group_report.md`.
- Commit `89abd0c`: `bang_loi.md`, `ho_so_launch_v0.md`, `group_report.md`.
- Bộ nhãn độc lập của người gắn nhãn 1 nằm ở cột "Nhãn người 1" trong `report/team/bang_loi.md`.

## 5. Công cụ AI đã dùng

- Claude Code: đọc và tóm tắt đề, tài liệu, quy tắc; soạn bản nháp `pilot_plan.yaml`, bảng khắc phục 5 ca, các câu quy tắc cho ca lệch, dòng đề xuất và `group_report.md`. Các bản nháp này đã được nhóm đọc và chỉnh lại.
- Cách tự kiểm tra: chạy lại các số D1 (1.251; 3.103; 1.000; 300; 299) và các chỉ số 82,83%, 27,12%, 4,25% bằng Python trên hai file CSV; tự tính lại power 0,642 ở mức chênh 5 điểm; đối chiếu từng con số trong hồ sơ với output của `lab13.py`; kiểm tra `yaml.safe_load` đọc được file và không còn dấu hỏi nào ngoài dòng chú thích.
- Không dùng AI để gắn nhãn 20 ca lỗi hay chấm duyệt chéo; nhãn do người gắn bằng tay, độc lập.

## 6. Tự đánh giá

(Điền sau khi hoàn thành bài lab.)
