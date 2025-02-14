from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVQuyen



@api_view(['POST'])
def ThemQuyen(request):
    TenQuyen = request.data.get('TenQuyen')
    GiaiThich = request.data.get('GiaiThich')
    result = NVQuyen.ThemQuyen(TenQuyen,GiaiThich)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaQuyen(request,id):
    TenQuyen = request.data.get('TenQuyen')
    GiaiThich = request.data.get('GiaiThich')
    result = NVQuyen.SuaQuyen(id,TenQuyen,GiaiThich)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaQuyen(request,id):
    result = NVQuyen.XoaQuyen(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def TatCaQuyen(request):
    result = NVQuyen.TatCaQuyen()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def ThemThoiGianQuyen(request):
    quyen_id = request.data.get('id')
    thu = request.data.get('thu')
    tg_ra = request.data.get('tg_ra')
    tg_vao = request.data.get('tg_vao')
    result = NVQuyen.ThemThoiGianQuyen(quyen_id, thu, tg_ra, tg_vao)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def XemChiTietQuyen(request,id):
    result = NVQuyen.XemChiTietQuyen(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def SuaThoiGianQuyen(request,id):
    thu = request.data.get('thu')
    tg_ra = request.data.get('tg_ra')
    tg_vao = request.data.get('tg_vao')
    result = NVQuyen.SuaThoiGianQuyen(id, thu, tg_ra, tg_vao)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def ChiTietThoiGianQuyen(request,id):
    result = NVQuyen.ChiTietThoiGianQuyen(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def QuyenNhomSQ(request,id):
    result = NVQuyen.QuyenNhomSQ(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def ThemQuyenNhomSQ(request):
    id_nhomsq = request.data.get("id_nhomsq")
    id_quyen = request.data.get("id_quyen")
    result = NVQuyen.ThemQuyenNhomSQ(id_nhomsq,id_quyen)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaQuyenNhomSQ(request,id):
    id_quyen = request.data.get("id_quyen")
    result = NVQuyen.SuaQuyenNhomSQ(id,id_quyen)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaQuyenNhomSQ(request,id):
    result = NVQuyen.XoaQuyenNhomSQ(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

## Nhóm QNCN

@api_view(['GET'])
def QuyenNhomQNCN(request,id):
    result = NVQuyen.QuyenNhomQNCN(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def ThemQuyenNhomQNCN(request):
    id_nhomQNCN = request.data.get("id_nhomQNCN")
    id_quyen = request.data.get("id_quyen")
    result = NVQuyen.ThemQuyenNhomQNCN(id_nhomQNCN,id_quyen)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaQuyenNhomQNCN(request,id):
    id_quyen = request.data.get("id_quyen")
    result = NVQuyen.SuaQuyenNhomQNCN(id,id_quyen)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaQuyenNhomQNCN(request,id):
    result = NVQuyen.XoaQuyenNhomQNCN(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


## Nhóm VC

@api_view(['GET'])
def QuyenNhomVC(request,id):
    result = NVQuyen.QuyenNhomVC(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def ThemQuyenNhomVC(request):
    id_nhomVC = request.data.get("id_nhomVC")
    id_quyen = request.data.get("id_quyen")
    result = NVQuyen.ThemQuyenNhomVC(id_nhomVC,id_quyen)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def SuaQuyenNhomVC(request,id):
    id_quyen = request.data.get("id_quyen")
    result = NVQuyen.SuaQuyenNhomVC(id,id_quyen)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def XoaQuyenNhomVC(request,id):
    result = NVQuyen.XoaQuyenNhomVC(id)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
