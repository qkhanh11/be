from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVRaVaoSQ

@api_view(['POST'])
def RaVaoSQ(request):
    sothe = request.data.get('sothe')
    trangthai = request.data.get('trangthai')
    cong = request.data.get('cong')
    result = NVRaVaoSQ.RaVaoSQ(sothe,trangthai,cong)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def RaVaoSQDacBiet(request):
    sothe = request.data.get('sothe')
    trangthai = request.data.get('trangthai')
    cong = request.data.get('cong')
    result = NVRaVaoSQ.RaVaoSQDacBiet(sothe,trangthai,cong)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def lay_lich_su_ra_vao(request):
    result = NVRaVaoSQ.lay_lich_su_ra_vao()
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)