from model import LSRaVaoHVModel,LSRaVaoQNCNModel,LSRaVaoSQModel,LSRaVaoVCModel,TheSiQuanModel
from .NVQuyen import ThoiGianTrongNgay_NhomSQ
from datetime import datetime, timedelta, date


def KiemTraVaoSQ(sothe):
    try:
        # Lấy thời gian vào muộn nhất cho nhóm sĩ quan từ hàm ThoiGianTrongNgay_NhomSQ
        thoi_gian_response = ThoiGianTrongNgay_NhomSQ(sothe)
        
        if thoi_gian_response['status'] == 'error':
            return thoi_gian_response  # Trả về thông báo lỗi nếu không lấy được thời gian

        tg_vao_muon_nhat = thoi_gian_response['data']['ThoiGianVaoMuonNhat']

        # Tính thời gian vào của sĩ quan (thời điểm hiện tại cộng thêm 7 giờ)
        current_time_plus_7_hours = datetime.now() + timedelta(hours=7)

        # Lấy thẻ sĩ quan với số thẻ đã cho
        the = TheSiQuanModel.TheSiQuanModel.objects.filter(SoThe=sothe).first()
        
        if not the:
            return {"status": "error", "message": "Không tìm thấy thẻ với số thẻ này."}


        # So sánh thời gian vào (thời điểm hiện tại cộng thêm 7 giờ) với thời gian muộn nhất
        if tg_vao_muon_nhat and current_time_plus_7_hours <= tg_vao_muon_nhat:
            return {"status": "success", "message": "Sĩ quan vào trước giờ muộn nhất."}
        else:
            return {"status": "error", "message": "Vào muộn."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}

def ThemLSRaVaoSQ():
    ...