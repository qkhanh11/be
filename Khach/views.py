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


