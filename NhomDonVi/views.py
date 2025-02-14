from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVNhomDonVi

# Create your views here.

@api_view(['POST'])
def ThemNhomDonVi(request):
    TenNhom = request.data.get('TenNhom')
    GhiChu = request.data.get('GhiChu')
    response = NVNhomDonVi.ThemNhomDonVi(TenNhom,GhiChu)
    if response["status"] == "success":
        return Response(data={"status": "success", "message": "Nhóm Đơn Vị đã được thêm thành công."},status=status.HTTP_200_OK)
    else:
        return Response(data={"status": "error", "message": 'Có lỗi xảy ra'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaNhomDonVi(request,id):
    try:
        # Lấy dữ liệu từ yêu cầu
        TenNhom = request.data.get('TenNhom')
        GhiChu = request.data.get('GhiChu')

        # Kiểm tra nếu thiếu dữ liệu
        if not id or not TenNhom or GhiChu is None:
            return Response({"status": "error", "message": "Thiếu thông tin cần thiết."}, status=status.HTTP_400_BAD_REQUEST)

        # Gọi hàm SuaNhomDonVi đã định nghĩa trước đó
        result = NVNhomDonVi.SuaNhomDonVi(id, TenNhom, GhiChu)

        # Trả về kết quả từ hàm SuaNhomDonVi
        if result["status"] == "success":
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['DELETE'])
def XoaNhomDonVi(request,id):
    try:
        # Lấy dữ liệu từ yêu cầu
        result = NVNhomDonVi.XoaNhomDonVi(id)
        if result["status"] == "success":
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def NhomDonVi(request):
    # Lấy tên nhóm từ query parameters
    TenNhom = request.query_params.get('TenNhom')

    if not TenNhom:
        result = NVNhomDonVi.TatCaNhomDonVi()
        if result["status"] == "success":
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_404_NOT_FOUND)
    try:
        # Gọi hàm TimNhomDonVi đã định nghĩa trước đó
        result = NVNhomDonVi.TimNhomDonVi(TenNhom)

        # Trả về kết quả từ hàm TimNhomDonVi
        if result["status"] == "success":
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['GET'])
def TatCaNhomDonVi(request):
    TenNhom = request.query_params.get('TenNhom')
    result = NVNhomDonVi.TatCaNhomDonVi()
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def ThongTinNhomDonVi(request,id):
    result = NVNhomDonVi.ThongTinNhomDonVi(id)
    if result["status"] == "success":
        return Response(result, status=status.HTTP_200_OK)
    else:
        return Response(result, status=status.HTTP_404_NOT_FOUND)