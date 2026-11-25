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
CHI_PHI_CO_DINH_THANG = 40_000_000  # đồng / tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1.0 / p
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


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
    reqs_sub = reqs.copy()
    runs_sub = runs[runs['request_id'].isin(reqs_sub['request_id'])].copy()

    if max_lan_chay is not None:
        runs_sub = runs_sub[runs_sub['attempt'] <= max_lan_chay]
        vuot = reqs_sub['so_lan_chay'] > max_lan_chay
        reqs_sub.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs_sub.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs_sub['tokens_in'] / 1000.0 * gia_vao + runs_sub['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs_sub['tool_calls'] * gia_tool
    xem_lai = reqs_sub['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs_sub['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai

    token_tong = float(tien_token.sum())
    tool_tong = float(tien_tool.sum())
    tong = token_tong + tool_tong + float(xem_lai) + float(lam_lai)
    thanh_cong = int((reqs_sub['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong > 0 else float('inf')

    return {
        'token': token_tong,
        'tool': tool_tong,
        'chay_lai': float((tien_token + tien_tool)[runs_sub['attempt'] > 1].sum()),
        'xem_lai': float(xem_lai),
        'lam_lai': float(lam_lai),
        'tong': float(tong),
        'thanh_cong': thanh_cong,
        'cps': float(cps),
        'hoa_don_moi_yc': (token_tong + tool_tong) / len(reqs_sub) if len(reqs_sub) > 0 else 0.0,
    }


def in_nhiem_vu_a3(runs, reqs):
    print('\n--- Nhiệm vụ A3 · Theo loại yêu cầu ---')
    for loai, df_loai in reqs.groupby('loai', sort=False):
        kq = mo_hinh(runs, df_loai)
        ty_le_tc = (df_loai['ket_qua'] == 'thanh_cong').mean() * 100
        tb_lan_chay = df_loai['so_lan_chay'].mean()
        ty_le_baseline = kq['cps'] / BASELINE
        print(
            f"{loai:10s} | n={len(df_loai):4d} | TC={ty_le_tc:5.1f}% | "
            f"lần/yc={tb_lan_chay:4.2f} | cps [simulated]={kq['cps']:8,.0f} đ | {ty_le_baseline:4.2f}x"
        )


def in_nhiem_vu_a4(runs, reqs):
    print('\n--- Nhiệm vụ A4 · Chi phí cố định (noi_dia + hang_nang) ---')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pham_vi)
    tc_thang = 45_000 * (kq_pv['thanh_cong'] / len(reqs))
    co_dinh_moi_viec_full = CHI_PHI_CO_DINH_THANG / tc_thang
    cps_full_co_dinh = kq_pv['cps'] + co_dinh_moi_viec_full

    co_dinh_moi_viec_half = CHI_PHI_CO_DINH_THANG / (tc_thang / 2.0)
    cps_half_co_dinh = kq_pv['cps'] + co_dinh_moi_viec_half

    print(f"Việc thành công/tháng (quy mô 45.000 yc): {tc_thang:,.0f}")
    print(f"CPS phạm vi [simulated]: {kq_pv['cps']:,.0f} đ | + cố định đầy đủ: {cps_full_co_dinh:,.0f} đ ({cps_full_co_dinh / BASELINE:.2f}x)")
    print(f"CPS phạm vi + cố định khối lượng 50% [simulated]: {cps_half_co_dinh:,.0f} đ ({cps_half_co_dinh / BASELINE:.2f}x)")


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

# ---------- Nhiệm vụ B · Bảng độ nhạy ----------
def in_nhiem_vu_b(runs, reqs):
    print('\n--- Nhiệm vụ B1 · Độ nhạy 9 kịch bản ---')
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2.0),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2.0),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    print(f"{'Gốc (A2)':25s} | cps [simulated]={goc:8,.0f} đ |   0.0%")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        pct = (cps / goc - 1.0) * 100.0
        print(f"{ten:25s} | cps [simulated]={cps:8,.0f} đ | {pct:+6.1f}%")

    print('\n--- Nhiệm vụ B2 · Đổi một cặp & xếp hạng 3 yếu tố ---')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    pct_cap = (cps_cap / goc - 1.0) * 100.0
    print(f"Token x2 + Xem lại x2 [simulated]: {cps_cap:,.0f} đ ({pct_cap:+.1f}%)")
    print("Xếp hạng 3 yếu tố mạnh nhất: 1. Số ca làm lại (+51.8%) | 2. Tỉ lệ xem lại (+40.7%) | 3. Lương nhân viên (+23.1%)")

    print('\n--- Nhiệm vụ B3 · Giới hạn chạy lại & chi phí cả hệ thống ---')
    tong_yc = len(reqs)
    for k in [1, 2, 3]:
        kq_k = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = tong_yc - kq_k['thanh_cong']
        ca_he_thong = kq_k['tong'] + khong_tc * BASELINE
        print(
            f"Tối đa {k} lần | trợ lý [simulated]={kq_k['tong']:10,.0f} đ | "
            f"không TC={khong_tc:3d} | cả hệ thống [simulated]={ca_he_thong:10,.0f} đ | "
            f"cps [simulated]={kq_k['cps']:6,.0f} đ"
        )

    print('\n--- Nhiệm vụ B4 · Xem lại 100% phạm vi (noi_dia + hang_nang) ---')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    token_tool_pv = float(
        (runs_pv['tokens_in'] / 1000.0 * GIA_VAO
         + runs_pv['tokens_out'] / 1000.0 * GIA_RA
         + runs_pv['tool_calls'] * GIA_TOOL).sum()
    )
    req_co_ok = int(runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique())
    ca_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    tc_pv = int((pv['ket_qua'] == 'thanh_cong').sum())

    # Kịch bản đề cho: 5 phút xem lại/ca có ok, 9 phút làm lại/ca lam_lai
    tong_b4_9p = token_tool_pv + req_co_ok * 5 * LUONG_PHUT + ca_lam_lai * 9 * LUONG_PHUT
    cps_b4_9p = tong_b4_9p / tc_pv

    # Kịch bản dùng trung bình thực tế cột phut_lam_lai_simulated (~15.3 phút/ca lam_lai)
    tb_lam_lai = float(reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean())
    tong_b4_thuc = token_tool_pv + req_co_ok * 5 * LUONG_PHUT + ca_lam_lai * tb_lam_lai * LUONG_PHUT
    cps_b4_thuc = tong_b4_thuc / tc_pv

    hoa_von_9p = (tc_pv * BASELINE - token_tool_pv - ca_lam_lai * 9 * LUONG_PHUT) / (req_co_ok * LUONG_PHUT)
    hoa_von_thuc = (tc_pv * BASELINE - token_tool_pv - ca_lam_lai * tb_lam_lai * LUONG_PHUT) / (req_co_ok * LUONG_PHUT)

    print(f"9 phút làm lại  -> tổng={tong_b4_9p:,.0f} đ | cps [simulated]={cps_b4_9p:,.0f} đ ({cps_b4_9p / BASELINE:.2f}x) | hòa vốn xem lại <= {hoa_von_9p:.1f} phút")
    print(f"{tb_lam_lai:.1f} phút làm lại -> tổng={tong_b4_thuc:,.0f} đ | cps [simulated]={cps_b4_thuc:,.0f} đ ({cps_b4_thuc / BASELINE:.2f}x) | hòa vốn xem lại <= {hoa_von_thuc:.1f} phút")

if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.2f}')
    in_nhiem_vu_a3(runs, reqs)
    in_nhiem_vu_a4(runs, reqs)
    in_nhiem_vu_b(runs, reqs)
    
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    in_co_mau_pilot()
    in_chi_so_chay_thu(reqs)
