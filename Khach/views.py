from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVKhach


@api_view(['POST'])
def ThemTheKhach(request):
    sothe = request.data.get('sothe')
    result = NVKhach.ThemTheKhach(sothe)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def HuyTheKhach(request,id):
    result = NVKhach.HuyThe(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def LayTheKhach(request):
    result = NVKhach.lay_the_khach_hieu_luc()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def ThemLoaiKhach(request):
    TenLoaiKhach = request.data.get('TenLoaiKhach')
    result = NVKhach.ThemLoaiKhach(TenLoaiKhach)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def SuaLoaiKhach(request,id):
    TenLoaiKhach = request.data.get('TenLoaiKhach')
    result = NVKhach.SuaLoaiKhach(id,TenLoaiKhach)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def HuyLoaiKhach(request,id):
    result = NVKhach.XoaLoaiKhach(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def LayLoaiKhach(request):
    result = NVKhach.LayLoaiKhach()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def TiepKhachSQ(request):
    SiQuan = request.data.get('MaSiQuan')
    HoTenKhach = request.data.get('HoTenKhach')
    SoDinhDanh = request.data.get('SoDinhDanh')
    Loai = request.data.get('Loai')
    TheKhach = request.data.get('TheKhach')
    GhiChu = request.data.get('GhiChu')
    print(SiQuan,HoTenKhach,SoDinhDanh,Loai,TheKhach,GhiChu)
    result = NVKhach.TiepKhachSQ(SiQuan,HoTenKhach,SoDinhDanh,Loai,TheKhach,GhiChu)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def DangTiepKhachSQ(request):
    result = NVKhach.DangTiepKhachSQ()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def TraKhachSQ(request,id):
    result = NVKhach.TraKhachSQ(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def DanhSachTiepKhachSiQuan(request):
    result = NVKhach.DanhSachTiepKhachSiQuan()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def danh_sach_the_khach(request):
    result = NVKhach.danh_sach_the_khach()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaTheKhach(request,id):
    SoThe = request.data.get('SoThe')
    result = NVKhach.SuaTheKhach(id,SoThe)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def TraTheKhach(request,id):
    result = NVKhach.TraTheKhach(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ThongKeTrongThang(request):
    result = NVKhach.ThongKeTrongThang()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ThongKeKhachTrongNgay(request):
    result = NVKhach.ThongKeKhachTrongNgay()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ThongKeTheoNam(request):
    nam = request.GET.get('nam')
    result = NVKhach.ThongKeTheoNam(nam)
    # if result["status"] == "success":
    #     return Response(data=result,status=status.HTTP_200_OK)
    # else:
    #     return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    return Response(data=result,status=status.HTTP_200_OK)



@api_view(['PUT'])
def SuaTiepKhachSQ(request,id):
    SiQuan = request.data.get('SiQuan')
    HoTenKhach = request.data.get('HoTenKhach')
    SoDinhDanh = request.data.get('SoDinhDanh')
    Loai = request.data.get('Loai')
    NgayBD = request.data.get('NgayBD')
    GioBD = request.data.get('GioBD')
    NgayKT = request.data.get('NgayKT')
    GioKT = request.data.get('GioKT')
    GhiChu = request.data.get('GhiChu')
    TraThe = request.data.get('TraTheKhach')
    TheKhach = request.data.get('TheKhach')
    result = NVKhach.SuaTiepKhachSQ(id,SiQuan,HoTenKhach,SoDinhDanh,Loai,TheKhach,NgayBD, GioBD,NgayKT,GioKT,GhiChu,TraThe)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def ThemLSTiepKhachSQ(request):
    SiQuan = request.data.get('SiQuan')
    HoTenKhach = request.data.get('HoTenKhach')
    SoDinhDanh = request.data.get('SoDinhDanh')
    Loai = request.data.get('Loai')
    NgayBD = request.data.get('NgayBD')
    GioBD = request.data.get('GioBD')
    NgayKT = request.data.get('NgayKT')
    GioKT = request.data.get('GioKT')
    GhiChu = request.data.get('GhiChu')
    TraThe = request.data.get('TraTheKhach')
    TheKhach = request.data.get('TheKhach')
    print(NgayBD,NgayKT,GioBD,GioKT)
    result = NVKhach.ThemLSTiepKhachSQ(SiQuan,HoTenKhach,SoDinhDanh,Loai,TheKhach,NgayBD, GioBD,NgayKT,GioKT,GhiChu,TraThe)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def TraTheKhachSQ(request,id):
    result = NVKhach.TraTheKhachSQ(id)    # if result["status"] == "success":
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def DaTraKhachSQ(request):
    result = NVKhach.DaTraKhachSQ()    # if result["status"] == "success":
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def ChiTietTiepKhachSQ(request,id):
    result = NVKhach.ChiTietTiepKhachSQ(id)    # if result["status"] == "success":
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)