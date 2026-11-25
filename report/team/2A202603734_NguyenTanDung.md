# Báo cáo cá nhân — Nguyễn Tấn Dũng - 2A202603734

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tấn Dũng
- MSSV: 2A202603734
- Email: 26ai.dungnt15@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1, kiêm nhóm trưởng

## 2. Phần việc phụ trách

- Điều phối nhóm 3 người, chia việc, theo dõi điều kiện "Xong khi" của từng checkpoint.
- Nhiệm vụ C: gắn nhãn độc lập 20 ca lỗi (người gắn nhãn 1).
- Nhiệm vụ D: chủ `pilot_plan.yaml`.
- Nhiệm vụ E: chốt `ho_so_launch_v0.md` và đề xuất cuối; trình bày trước hội đồng Gate 2a.
- Điền `TEAM.md`, `group_report.md`; nộp link repo lên LMS.

## 3. Đóng góp cụ thể

- Viết `pilot_plan.yaml`: năm câu D1, năm câu D2, đánh đổi chấp nhận mức chênh 6 điểm, hai luật dừng (an toàn, mức sử dụng) đủ bốn vế.
- (Cập nhật sau) Gắn nhãn 20 ca lỗi; hoàn thiện luật dừng về chi phí và phạm vi sau khi có số A, B; điền hồ sơ launch.

## 4. Bằng chứng

- Commit `03ff33d` trên `main`: `report/team/pilot_plan.yaml`.
- (Cập nhật sau) Bộ nhãn độc lập, `ho_so_launch_v0.md`.

## 5. Công cụ AI đã dùng

- Claude Code: đọc và tóm tắt đề, tài liệu, quy tắc; soạn bản nháp `pilot_plan.yaml` và file chia việc nội bộ.
- Cách tự kiểm tra: chạy lại các số D1 (1.251; 3.103; 1.000; 300; 299) và các chỉ số 82,83%, 27,12%, 4,25% bằng Python trên hai file CSV; tự tính lại power 0,642 ở mức chênh 5 điểm; kiểm tra `yaml.safe_load` đọc được file và không còn dấu hỏi nào ngoài dòng chú thích.
- Không dùng AI để gắn nhãn 20 ca lỗi hay chấm duyệt chéo.

## 6. Tự đánh giá

(Điền sau khi hoàn thành bài lab.)
