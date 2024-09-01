from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from NghiepVu import NVTheRaVao


@api_view(['POST'])
def ThemTheSQ(request):
    SoThe = request.data.get('SoThe')
    SiQuan = request.data.get('SiQuan')
    result = NVTheRaVao.ThemTheSQ(SoThe, SiQuan)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def ThemTheQNCN(request):
    SoThe = request.data.get('SoThe')
    QNCN = request.data.get('QNCN')
    result = NVTheRaVao.ThemTheQNCN(SoThe, QNCN)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST'])
def ThemTheVC(request):
    SoThe = request.data.get('SoThe')
    VC = request.data.get('VC')
    result = NVTheRaVao.ThemTheVC(SoThe, VC)
    if result["status"] == "success":
        return Response(data=result,status=status.HTTP_200_OK)
    else:
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def KTTheSQ(request,id):
    result = NVTheRaVao.KTTheSQ(id)
    return Response(data=result,status=status.HTTP_200_OK)


@api_view(['GET'])
def KTTheQNCN(request,id):
    result = NVTheRaVao.KTTheQNCN(id)
    return Response(data=result,status=status.HTTP_200_OK)


@api_view(['GET'])
def KTTheVC(request,id):
    result = NVTheRaVao.KTTheVC(id)
    return Response(data=result,status=status.HTTP_200_OK)



@api_view(['DELETE'])
def HuyTheSQ(request,id):
    result = NVTheRaVao.HuyTheSQ(id)
    return Response(data=result,status=status.HTTP_200_OK)


@api_view(['DELETE'])
def HuyTheQNCN(request,id):
    result = NVTheRaVao.HuyTheQNCN(id)
    return Response(data=result,status=status.HTTP_200_OK)


@api_view(['DELETE'])
def HuyThevc(request,id):
    result = NVTheRaVao.HuyThevc(id)
    return Response(data=result,status=status.HTTP_200_OK)


@api_view(['POST'])
def ThemNamTheSQ(request):
    the_id = request.data.get('the_id')
    nam = request.data.get('nam')
    result = NVTheRaVao.ThemNamTheSQ(the_id=the_id, nam= nam)
    return Response(data=result,status=status.HTTP_200_OK)
    