from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVNhomDoiTuong


@api_view(['POST'])
def ThemNhomSQ(request):
    TenNhom = request.data.get('TenNhom')
    print(TenNhom)
    result = NVNhomDoiTuong.ThemNhomSQ(TenNhom)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def ThemNhomQNCN(request):
    TenNhom = request.data.get('TenNhom')
    result = NVNhomDoiTuong.ThemNhomQNCN(TenNhom)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def ThemNhomVC(request):
    TenNhom = request.data.get('TenNhom')
    result = NVNhomDoiTuong.ThemNhomVC(TenNhom)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def NhomSQ(request):
    result = NVNhomDoiTuong.NhomSQ()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def NhomQNCN(request):
    result = NVNhomDoiTuong.NhomQNCN()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def NhomVC(request):
    result = NVNhomDoiTuong.NhomVC()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaNhomSQ(request,id):
    TenNhom = request.data.get('TenNhom')
    result = NVNhomDoiTuong.SuaNhomSQ(id,TenNhom)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaNhomQNCN(request,id):
    TenNhom = request.data.get('TenNhom')
    result = NVNhomDoiTuong.SuaNhomQNCN(id,TenNhom)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaNhomVC(request,id):
    TenNhom = request.data.get('TenNhom')
    result = NVNhomDoiTuong.SuaNhomVC(id,TenNhom)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaNhomSQ(request,id):
    try:
        # Lấy dữ liệu từ yêu cầu
        result = NVNhomDoiTuong.XoaNhomSQ(id)
        if result["status"] == "success":
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['DELETE'])
def XoaNhomQNCN(request,id):
    try:
        # Lấy dữ liệu từ yêu cầu
        result = NVNhomDoiTuong.XoaNhomQNCN(id)
        if result["status"] == "success":
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['DELETE'])
def XoaNhomVC(request,id):
    try:
        # Lấy dữ liệu từ yêu cầu
        result = NVNhomDoiTuong.XoaNhomVC(id)
        if result["status"] == "success":
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)