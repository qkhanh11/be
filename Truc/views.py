from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVTruc



@api_view(['POST'])
def ThemTrucBan(request):
    ngay = request.data.get('ngay')
    TBTruong = request.data.get('TBTruong')
    TBPho = request.data.get('TBPho')
    result = NVTruc.ThemTrucBan(ngay,TBTruong,TBPho)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['PUT'])
def SuaTrucBan(request,id):
    TBTruong = request.data.get('TBTruong')
    TBPho = request.data.get('TBPho')
    result = NVTruc.SuaTrucBan(id,TBTruong,TBPho)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaTrucBan(request,id):
    result = NVTruc.XoaTrucBan(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def XemTatCaTrucBan(request):
    result = NVTruc.XemTatCaTrucBan()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def XemChiTietTrucBan(request,id):
    result = NVTruc.XemChiTietTrucBan(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def LayDanhSachCong(request):
    result = NVTruc.LayDanhSachCong()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def TimTrucBanTheoKhoangNgay(request):
    ngay_bat_dau = request.GET.get('ngay_bat_dau')
    ngay_ket_thuc = request.GET.get('ngay_ket_thuc')
    result = NVTruc.TimTrucBanTheoKhoangNgay(ngay_bat_dau, ngay_ket_thuc)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def ThemCong(request):
    TenCong = request.data.get('TenCong')
    ViTri = request.data.get('ViTri')
    result = NVTruc.ThemCong(TenCong, ViTri)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaCong(request,id):
    TenCong = request.data.get('TenCong')
    ViTri = request.data.get('ViTri')
    result = NVTruc.SuaCong(id,TenCong,ViTri)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaCong(request,id):
    result = NVTruc.XoaCong(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def LayThongTinTrucBanTheoID(request,id):
    result = NVTruc.LayThongTinTrucBanTheoID(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def LayTatCaCaGac(request):
    result = NVTruc.LayTatCaCaGac()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def ThemCaGac(request):
    Ca = request.data.get('Ca')
    ThoiGianBatDau = request.data.get('ThoiGianBatDau')
    ThoiGianKetThuc = request.data.get('ThoiGianKetThuc')
    result = NVTruc.ThemCaGac(Ca,ThoiGianBatDau,ThoiGianKetThuc)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaCaGac(request,id):
    Ca = request.data.get('Ca')
    ThoiGianBatDau = request.data.get('ThoiGianBatDau')
    ThoiGianKetThuc = request.data.get('ThoiGianKetThuc')
    result = NVTruc.SuaCaGac(id, Ca,ThoiGianBatDau,ThoiGianKetThuc)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaCaGac(request,id):
    result = NVTruc.XoaCaGac(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaCaGac(request,id):
    result = NVTruc.XoaCaGac(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST) 
    

@api_view(['POST'])
def ThemPCCaGac(request):
    Ngay = request.data.get('Ngay')
    CongGac = request.data.get('CongGac')
    result = NVTruc.ThemPCCaGac(Ngay,CongGac)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def lay_ngay_theo_cong(request,id=0):
    NgayBD = request.GET.get('NgayBD')
    NgayKT = request.GET.get('NgayKT')
    result = NVTruc.lay_ngay_theo_cong(id,NgayBD,NgayKT)
    
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST) 
    

@api_view(['GET'])
def LayCaGacTrongNgayCong(request,id):
    result = NVTruc.LayCaGacTrongNgayCong(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST) 



@api_view(['POST'])
def ThemPhanCongChiTiet(request):
    PCCaGac = request.data.get('PCCaGac')
    MaCS = request.data.get('MaCS')
    result = NVTruc.ThemPhanCongChiTiet(PCCaGac,MaCS)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        print(result)
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET'])
def xem_phan_cong_chi_tiet(request,id):
    result = NVTruc.xem_phan_cong_chi_tiet(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST) 
    

@api_view(['DELETE'])
def xoa_phan_cong_chi_tiet(request,id):
    result = NVTruc.xoa_phan_cong_chi_tiet(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST) 


    


