# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994/1.200 = 82,83% |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 48/177 = 27,12% |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51/1.200 = 4,25% |
| Dùng | Đề xuất: tỉ lệ yêu cầu được phân vào nhóm trợ lý thực sự hiện gợi ý | Số yêu cầu có ít nhất một gợi ý đã hiển thị, chia số yêu cầu được phân vào nhóm trợ lý | Không cần tính |
| An toàn | Đề xuất: tỉ lệ hoàn sai tiền trong mẫu kiểm tra | Số yêu cầu có số tiền đã hoàn khác số tiền phải hoàn, chia số yêu cầu đã kiểm tra | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống ticket | `request_id`, `trace_id`, `created_at`, `loai` | Khi nhận yêu cầu, ở cả hai nhánh |
| `input_validation_failed` | Dịch vụ tiếp nhận hoàn phí | `request_id`, `trace_id`, `field`, `error_code`, `occurred_at` | Khi một trường không đạt kiểm tra định dạng, trước khi tạo lệnh hoàn |
| `pilot_assignment_recorded` | Dịch vụ phân nhóm | `request_id`, `trace_id`, `arm`, `staff_id`, `assigned_at` | Khi ghi nhận nhánh của yêu cầu |
| `agent_suggestion_shown` | Giao diện CSKH | `request_id`, `trace_id`, `staff_id`, `shown_at` | Khi gợi ý hiển thị |
| `agent_run_completed` | Trợ lý | `request_id`, `trace_id`, `attempt`, `status`, `completed_at` | Khi kết thúc mỗi lần chạy |
| `staff_review_decision` | Giao diện CSKH | `request_id`, `trace_id`, `decision` (giữ, sửa, bỏ), `review_minutes`, `reviewed_at` | Khi nhân viên chốt quyết định |
| `staff_rework_completed` | Giao diện CSKH | `request_id`, `trace_id`, `rework_minutes`, `completed_at` | Khi nhân viên sửa xong một kết quả sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `trace_id`, `idempotency_key`, `result` (ok, lỗi), `http_status`, `occurred_at` | Sau mỗi lần thử ghi giao dịch hoàn tiền |
| `handoff_to_staff` | Trợ lý | `request_id`, `trace_id`, `loai`, `reason` (ví dụ `thieu_du_lieu`), `handed_off_at` | Khi yêu cầu được chuyển vào hàng đợi của nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id`, `trace_id`, `closed_at` | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | `request_id`, `trace_id`, `reopened_at` | Khi yêu cầu mở lại |
| `refund_audit_completed` | Kế toán | `request_id`, `trace_id`, `paid_vnd`, `expected_vnd`, `audited_at` | Khi hoàn tất kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Đóng đúng hạn và mở lại: nối sự kiện nhận, đóng và mở lại. Chỉ tính các yêu cầu đã đủ thời gian theo dõi 7 ngày sau khi đóng đối với phần mở lại.
- Bỏ qua gợi ý: đếm quyết định sửa hoặc bỏ trên số yêu cầu có quyết định xem lại.
- Hiện gợi ý: nối sự kiện phân nhánh và hiển thị. Hoàn sai tiền: so sánh hai số tiền trong sự kiện kiểm tra.
- Dùng cùng `trace_id` từ lúc tạo yêu cầu và đếm theo `request_id` để các lần chạy lại không làm tăng mẫu số.
- [Bảng khắc phục](bang_loi.md) dùng `input_validation_failed` cho ca 1, `refund_ledger_write` để đối soát ca 7 và `handoff_to_staff` với `reason=thieu_du_lieu` cho ca 4.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng | B1 toàn mẫu: làm lại gấp đôi → 6.787 đ/việc, tăng 51,8% (`simulated`) | Theo tuần, số yêu cầu có `staff_rework_completed` chia cho số yêu cầu trong phạm vi. Mốc chạy thử: 48/982 = 4,89%. | Nếu tỷ lệ vượt mốc chạy thử, rà trace các ca làm lại theo loại yêu cầu trước khi mở rộng. | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% | B4 trong phạm vi pilot: 11.743–12.415 đ/việc, bằng 0,98–1,03× mức 12.000 đ (`simulated`) | Theo tuần, dùng `agent_run_completed` và `staff_review_decision` để đo tỷ lệ xem lại trên yêu cầu có lượt `ok`, cùng số phút xem lại trung bình. | Nếu vẫn phải xem lại toàn bộ và trung bình vượt 4,8 phút/lượt, giữ nguyên phạm vi và thử rút ngắn thao tác. Chỉ thử giảm tỷ lệ xem lại khi chỉ số an toàn đạt ngưỡng pilot. | Trưởng nhóm CSKH |
