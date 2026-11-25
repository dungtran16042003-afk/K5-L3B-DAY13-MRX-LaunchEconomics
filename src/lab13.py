"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    raise NotImplementedError('VIẾT Ở ĐÂY')


# ---------- Nhiệm vụ D1 · Cỡ mẫu pilot ----------
def co_mau_hai_ti_le(baseline, muc_tieu, alpha=0.05, power=0.80):
    """Cỡ mẫu tối thiểu mỗi nhánh cho kiểm định hai phía, chia đều."""
    ti_le_gop = (baseline + muc_tieu) / 2
    chuan = NormalDist()
    z_alpha = chuan.inv_cdf(1 - alpha / 2)
    z_power = chuan.inv_cdf(power)
    do_lech_gop = math.sqrt(2 * ti_le_gop * (1 - ti_le_gop))
    do_lech_hai_nhanh = math.sqrt(
        baseline * (1 - baseline) + muc_tieu * (1 - muc_tieu)
    )
    return math.ceil(
        ((z_alpha * do_lech_gop + z_power * do_lech_hai_nhanh) / (muc_tieu - baseline)) ** 2
    )


def in_co_mau_pilot():
    baseline = 0.70
    icc = 0.02
    yeu_cau_moi_nhan_vien = 75
    nhan_vien_moi_nhanh = 20
    depot_moi_nhanh = 6

    co_mau_5_diem = co_mau_hai_ti_le(baseline, 0.75)
    he_so_thiet_ke = 1 + (yeu_cau_moi_nhan_vien - 1) * icc
    co_mau_theo_nhan_vien = math.ceil(co_mau_5_diem * he_so_thiet_ke)
    so_nhan_vien = math.ceil(co_mau_theo_nhan_vien / yeu_cau_moi_nhan_vien)

    co_mau_6_diem = co_mau_hai_ti_le(baseline, 0.76)
    # Giải bất đẳng thức c*m / (1 + (m-1)*ICC) >= n theo m.
    yeu_cau_6_diem = math.ceil(
        co_mau_6_diem * (1 - icc) / (nhan_vien_moi_nhanh - co_mau_6_diem * icc)
    )
    he_so_6_diem = 1 + (yeu_cau_6_diem - 1) * icc

    print('\nD1 · Cỡ mẫu mỗi nhánh')
    print(f'a) Chia theo yêu cầu, +5 điểm: {co_mau_5_diem} yêu cầu')
    print(f'b) Chia theo nhân viên, m=75: DE={he_so_thiet_ke:.2f}, '
          f'{co_mau_theo_nhan_vien} yêu cầu, {so_nhan_vien} nhân viên')
    print(f'c) 20 nhân viên: cỡ mẫu hiệu dụng < {nhan_vien_moi_nhanh / icc:.0f}')
    print(f'd) 6 depot: cỡ mẫu hiệu dụng < {depot_moi_nhanh / icc:.0f}')
    print(f'e) +6 điểm: cần {co_mau_6_diem} yêu cầu hiệu dụng, '
          f'{yeu_cau_6_diem} yêu cầu/nhân viên với 20 nhân viên (DE={he_so_6_diem:.2f})')


# ---------- Nhiệm vụ E1 · Chỉ số từ dữ liệu chạy thử ----------
def in_chi_so_chay_thu(reqs):
    mo_lai = reqs['mo_lai_trong_7_ngay'].eq(1)
    dong_dung_han = reqs['dong_trong_24h'].eq(1) & ~mo_lai
    da_xem = reqs['duoc_xem_lai'].eq(1)
    bo_qua = da_xem & reqs['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    trong_pham_vi = reqs['loai'].isin(['noi_dia', 'hang_nang'])

    print('\nD3 / E1 · Chỉ số trong đợt chạy thử')
    for ten, tu_so, mau_so in (
        ('Đóng trong 24 giờ và không mở lại trong 7 ngày', dong_dung_han.sum(), len(reqs)),
        ('Sửa hoặc bỏ trong các yêu cầu đã xem lại', bo_qua.sum(), da_xem.sum()),
        ('Mở lại trong 7 ngày, toàn mẫu', mo_lai.sum(), len(reqs)),
        ('Mở lại trong 7 ngày, nội địa và hàng nặng', (mo_lai & trong_pham_vi).sum(), trong_pham_vi.sum()),
    ):
        print(f'{ten}: {tu_so}/{mau_so} = {tu_so / mau_so:.2%}')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    in_co_mau_pilot()
    in_chi_so_chay_thu(reqs)
