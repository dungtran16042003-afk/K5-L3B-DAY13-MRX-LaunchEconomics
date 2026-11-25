# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Tấn Dũng · Người gắn nhãn 2: Nguyễn Duy Anh (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngầm | Hệ thống | Không | Hệ thống |
| 9 | Hệ thống | Do người dùng | Không | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Hệ thống | Do người dùng | Không | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Ngữ cảnh | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 15 / 20 = 75%. Dưới ngưỡng 80%, nên nhóm đã viết lại định nghĩa trước khi đi tiếp (xem mục dưới). Hai bộ nhãn độc lập được giữ nguyên, không sửa sau khi so.

## Quy tắc phân biệt cho các ca không trùng

Năm ca không trùng: 3, 8, 9, 14, 19. Nhóm đã bàn và chốt lấy nhãn của người gắn nhãn 2 cho cả năm ca; mỗi ca có một câu quy tắc phân biệt.

- Ca 3 (Ngữ cảnh): trợ lý làm đúng thiết kế (hoàn về ví LogiX trong 5 phút), chỉ có kỳ vọng nhận tiền về tài khoản ngân hàng của khách không khớp; không có điều khoản nào bị vi phạm nên không phải Hệ thống.
- Ca 8 (Hệ thống): trích dẫn "Điều 7.2" không tồn tại là sai so với chính sách hiện hành và nhìn thấy được trong câu trả lời; Ngầm chỉ dùng khi không ai nhận ra cho tới khi kiểm tra.
- Ca 9 (Do người dùng): gốc lỗi là khách nhập mã đơn sàn thương mại điện tử thay vì mã vận đơn; việc trợ lý không gợi ý lại là chỗ cần cải thiện, ghi ở cột khắc phục.
- Ca 14 (Do người dùng): gốc lỗi là khách bấm nhầm "Xác nhận đã nhận tiền" khi chưa nhận; hệ thống hoạt động đúng thiết kế.
- Ca 19 (Giới hạn hệ thống): trợ lý chỉ truy cập được dữ liệu 12 tháng nên không thể tra đơn 14 tháng trước, và đã nói rõ giới hạn đó; đây là dữ liệu không có, không phải giả định lệch hoàn cảnh.

Định nghĩa đã viết lại (vì đồng thuận 75% < 80%), thêm một câu quyết định cho mỗi loại hay lẫn:
- Do người dùng: gốc lỗi là đầu vào hoặc thao tác của khách (nhập sai, chọn sai, bấm nhầm); việc hệ thống không gợi ý sửa là chỗ cải thiện, không đổi nhãn.
- Hệ thống: trợ lý làm sai so với thiết kế hoặc chính sách và sai đó đã lộ ra (khách báo, nhân viên bắt được, hoặc đọc thấy ngay trong câu trả lời).
- Ngữ cảnh: trợ lý làm đúng thiết kế và đúng chính sách, nhưng kỳ vọng hoặc hoàn cảnh của khách không khớp giả định của thiết kế.
- Giới hạn hệ thống: không có dữ liệu, ngoài phạm vi hoặc đầu vào không xử lý được; trợ lý không thể làm dù có cố.
- Ngầm: có sai thật nhưng không ai nhận ra cho tới khi kiểm tra mẫu hoặc giám sát.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Năm ca được chọn đều là ca hai người gắn trùng nhãn. Cách phát hiện đo được (event, ngưỡng, tần suất), người phụ trách là một vai trò của LogiX-VN, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `input_validation_failed` khi số tài khoản sai định dạng; cảnh báo khi vượt 2% số yêu cầu mỗi ngày | Kiểm tra độ dài và định dạng số tài khoản trước khi tạo lệnh hoàn, yêu cầu khách xác nhận lại | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi `refund_ledger_write` kết quả ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 10 | Ngữ cảnh | Tỉ lệ `ticket_reopened` của các yêu cầu bị từ chối do bất khả kháng, theo tuần; cảnh báo khi vượt 10% | Khi có thông báo bất khả kháng, ứng dụng thay dòng "cam kết giao 24 giờ"; tin nhắn từ chối nêu rõ điều khoản và lý do | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason` = thieu_du_lieu, theo loại yêu cầu; cảnh báo khi vượt 5% số yêu cầu mỗi tuần | Giữ cách chuyển nhân viên kèm tóm tắt; đưa `quoc_te` ra khỏi phạm vi pilot (1,88× so với 12.000 đ, simulated) | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn mỗi tuần so với bảng giá hiện hành (event `refund_audit_completed`); ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng |
