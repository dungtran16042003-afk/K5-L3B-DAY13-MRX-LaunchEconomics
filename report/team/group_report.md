# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: MRX (nhóm 3 người; đề bài thiết kế cho 4 người nên các vai được gộp, xem `TEAM.md`)
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Lab 13 yêu cầu nhóm lập hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN (dữ liệu giả lập) và bảo vệ trước hội đồng Gate 2a. Hồ sơ trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot thiết kế thế nào để ra quyết định. Nhóm đi theo thứ tự A → E: tính chi phí từ trace, bảng độ nhạy, phân loại lỗi, kế hoạch pilot, rồi ghép thành một trang hồ sơ. Gate 2a chỉ duyệt kế hoạch pilot.

## 3. Giải pháp

- **A, B (chi phí, độ nhạy):** `src/lab13.py` tính chi phí mỗi việc thành công từ hai file CSV, tử số tính mọi lần chạy, mẫu số chỉ đếm `thanh_cong`; kết quả ở `report/team/bang_chi_phi.md`.
- **C (lỗi):** hai người gắn nhãn độc lập 20 ca, so nhãn, viết lại định nghĩa vì đồng thuận chưa đủ 80%, lập bảng khắc phục 5 ca; kết quả ở `report/team/bang_loi.md`.
- **D (pilot):** tính cỡ mẫu ba cách chia, chọn chia theo nhân viên 20 + 20; kết quả ở `report/team/pilot_plan.yaml`.
- **E (chỉ số, hồ sơ):** `report/team/chi_so.md` (chỉ số, event có `trace_id`, rủi ro kinh tế) và `report/team/ho_so_launch_v0.md` (bảy mục và đề xuất).

## 4. Kết quả

Các số tính từ cột `_simulated` ghi nhãn `simulated`.

- Chi phí mỗi việc thành công: 4.472 đ toàn mẫu, gấp 16,3 lần hoá đơn token và tool chia số yêu cầu (274,7 đ); hơn 92% là giờ nhân viên [simulated].
- Chi phí cả hệ thống: 5.865 đ/yêu cầu, bằng 0,49× mức 12.000 đ khi nhân viên tự làm [simulated]. `quoc_te` đắt 1,88× nên bị loại khỏi phạm vi.
- Ba yếu tố nhạy nhất: số ca làm lại (+51,8%), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1%) [simulated]. Xem lại 100% làm chi phí 11.743 đ (0,98×) [simulated].
- Lỗi: đồng thuận độc lập 15/20 = 75%, bảng khắc phục đủ năm loại.
- Pilot: chia theo 20 + 20 nhân viên, cần 859 yêu cầu hiệu dụng mỗi nhóm cho mức chênh 6 điểm; power khoảng 0,64 nếu tác động thật là 5 điểm.
- **Đề xuất: Go có điều kiện** (bốn điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra, xem `ho_so_launch_v0.md`).
- Kết quả duyệt chéo nhận được từ hội đồng: (điền sau buổi duyệt chéo)

## 5. Khó khăn và cách xử lý

- Đề bài thiết kế cho 4 người, nhóm có 3: gộp vai (người viết code kiêm gắn nhãn 2; người kiểm số kiêm giữ hồ sơ).
- Đồng thuận nhãn lần đầu chỉ 75%, dưới 80%: nhóm bàn 5 ca lệch, chốt nhãn thống nhất, viết một câu quy tắc cho mỗi ca và viết lại định nghĩa năm loại.
- Con số phụ trong slide và hướng dẫn lệch nhau (số việc đẩy sang nhân viên khi giới hạn 1 lần chạy: 97 và 85): nhóm dùng số do `lab13.py` tự tính, không chép.
- Trộn việc của nhiều người vào cùng `src/lab13.py` dễ gây conflict: mỗi người phụ trách một phần, kéo `main` về trước khi push.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Toàn bộ dữ liệu là giả lập; phút xem lại và làm lại là số `simulated`, cần thay bằng phút đo thật sau tuần đầu của pilot.
- Mẫu chỉ có 20 nhân viên và 6 depot, chưa phủ đủ 40 nhân viên và 12 depot của công ty.
- Chia theo nhân viên chưa đủ cỡ mẫu cho mức chênh 5 điểm (tối đa 1.000 so với 1.251 cần có); nhóm chấp nhận mức 6 điểm.
- Đợt chạy thử không có nhóm đối chứng nên các chỉ số chỉ là "chỉ số trong đợt chạy thử".
- Ước tính của nhóm: với khoảng 1.227 yêu cầu `noi_dia` + `hang_nang` mỗi ngày, bước rollout 0.50 cần khoảng 10 ngày để đủ 299 yêu cầu mỗi nhân viên, dài hơn một tuần ghi trong mẫu kế hoạch.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com
- Tài liệu statsmodels, lớp `NormalIndPower`
- Tài liệu lab: `README.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, slide Ngày 13
