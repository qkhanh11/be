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