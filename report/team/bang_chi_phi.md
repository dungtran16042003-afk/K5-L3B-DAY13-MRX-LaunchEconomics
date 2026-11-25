# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 lần — ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 lần — ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25× — ĐẠT |

## A2 · Mô hình chi phí từ trace

| Khoản | Giá trị | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585,13 đ | `logix_runs.csv` | đo từ trace |
| Tool | 84.000,00 đ | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804,49 đ | Token và tool với `attempt > 1` | đo từ trace |
| Xem lại | 1.780.000,00 đ | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000,00 đ | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585,13 đ | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 việc | `ket_qua == 'thanh_cong'` | đếm từ dữ liệu |
| Chi phí mỗi việc thành công | 4.471,97 đ/việc | Tổng chi phí ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,65 đ/yêu cầu | `logix_runs.csv`, chia cho 1.200 yêu cầu | đo từ trace |

Phép tính đối chiếu cho TV3: [(5.771.712 × 26 + 734.774 × 130) ÷ 1.000 + 5.600 × 15] ÷ 1.200 = 274,65 đ/yêu cầu. Cộng token và tool trên cả 1.624 lần chạy.

- Chi phí mỗi việc thành công gấp 16,28 lần hóa đơn token và tool chia theo yêu cầu (`simulated`).
- Làm lại chiếm tỷ trọng lớn nhất, 51,77% tổng chi phí (`simulated`).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- `quoc_te` tốn 1,88× chi phí nhân viên tự làm (`simulated`). Tăng giới hạn từ 2 lên 3 lần vẫn chỉ có 41/150 việc thành công, còn chi phí tăng từ 20.605 lên 22.515 đ/việc (`simulated`).

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (`simulated`) | So với 12.000 đ (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Ở cả hai mức khối lượng, chi phí vẫn dưới 12.000 đ. Khi khối lượng giảm một nửa, phần cố định tăng gấp đôi và tổng chi phí lên 5.784 đ/việc (`simulated`).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (`simulated`) | So với A2 (`simulated`) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Mốc A2 là 4.471,97 đ/việc (`simulated`). Trước khi làm tròn, cả 3 cặp gấp đôi và giảm một nửa đều cho mức giảm bằng đúng một nửa mức tăng.

## B2 · Đổi một cặp và xếp hạng

- Giá token và tỉ lệ xem lại cùng gấp đôi: 6.543 đ/việc, tăng 46,3% (`simulated`), bằng tổng hai tác động riêng trên cùng mốc A2.
- Xếp hạng theo các kịch bản B1: 1. Số ca làm lại (+51,8%) · 2. Tỉ lệ xem lại (+40,7%) · 3. Lương nhân viên (+23,1%), đều `simulated`.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (`simulated`) | Số yêu cầu không thành công | Chi phí cả hệ thống (`simulated`) | Chi phí mỗi việc thành công (`simulated`) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Hai lần cho chi phí cả hệ thống thấp nhất (6.901.220 đ). Một lần cho chi phí trợ lý mỗi việc thành công thấp nhất (4.111 đ), đồng thời để lại thêm 85 yêu cầu cho nhân viên xử lý. Các số chi phí là `simulated`.

## B4 · Nếu phải xem lại tất cả

- Xem lại 948 yêu cầu có lượt chạy `ok` với 5 phút/yêu cầu, tính thêm 48 ca làm lại và chia cho 900 việc thành công. Với 9 phút làm lại/ca, chi phí là 11.743 đ (0,98×). Dùng trung bình chưa làm tròn của dữ liệu (khoảng 15,3 phút), chi phí là 12.415 đ (1,03×). Cả hai mức là `simulated`.
- Pilot cần đo thời gian xem lại và mức có thể giảm tỷ lệ xem lại mà vẫn an toàn. Nếu vẫn xem lại 100%, mức hòa vốn khoảng 5,1 phút/lượt ở kịch bản 9 phút làm lại và 4,8 phút/lượt ở kịch bản 15,3 phút (`simulated`).
