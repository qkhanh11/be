from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import FileResponse
import os
from .test import create_word_document
from datetime import datetime


@api_view(['GET'])
def generate_word_file(request):
    # Tạo file Word với header và footer
    file_path = create_word_document()
    now = datetime.now()
    day = now.strftime('%d')
    month = now.strftime('%m')  # Thay đổi định dạng tháng nếu cần
    year = now.year
    try:
        # Mở file mà không dùng 'with' để tránh việc file bị đóng
        if os.path.exists(file_path):
            doc_file = open(file_path, 'rb')
            response = FileResponse(doc_file, as_attachment=True, filename=f"BaoCao_{day}_{month}_{year}.docx")
            return response
        else:
            return Response({"error": "File không tồn tại"}, status=404)
        file_path.delete()
    except Exception as e:
        return Response({"error": str(e)}, status=500)
