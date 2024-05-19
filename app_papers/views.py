from django.core.files.base import ContentFile
from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from reportlab.lib.pagesizes import letter
import io
from reportlab.pdfgen import canvas

from app_papers.filters import PapersFilter, ReferencesFilter
from app_papers.models import Papers, References, Reviews
from app_papers.serializers import (
    PapersSerializer, GetPapersSerializer,
    ReferenceSerializer, GetReferencesSerializer,
    ReviewsSerializer, GetReviewsSerializer
)


class PapersViewSet(viewsets.ModelViewSet):
    queryset = Papers.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PapersFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetPapersSerializer
        return PapersSerializer

    def get_queryset(self):
        if self.request.method == 'POST':
            return super().get_queryset().filter(author=self.request.user)
        search_query = self.request.GET.get("search", None)
        if search_query:
            return Papers.objects.filter(
                paper_title_uz__icontains=search_query
            ) | Papers.objects.filter(
                paper_title_ru__icontains=search_query
            ) | Papers.objects.filter(
                paper_title_en__icontains=search_query
            ) | Papers.objects.filter(
                paper_description_uz__icontains=search_query
            ) | Papers.objects.filter(
                paper_description_ru__icontains=search_query
            ) | Papers.objects.filter(
                paper_description_en__icontains=search_query
            ) | Papers.objects.filter(
                paper_content_uz__icontains=search_query
            ) | Papers.objects.filter(
                paper_content_ru__icontains=search_query
            ) | Papers.objects.filter(
                paper_content_en__icontains=search_query
            ) | Papers.objects.filter(
                paper_tegs__icontains=search_query
            )
        return Papers.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Papers.objects.filter(pk=instance.pk).update(paper_views=F('paper_views') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = References.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReferencesFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetReferencesSerializer
        return ReferenceSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetReviewsSerializer
        return ReviewsSerializer

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = Reviews.objects.get(pk=response.data['id'])
        self.create_pdf(instance)
        return response

    def create_pdf(self, instance):
        text = instance.review_text

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter
        p.drawString(100, height - 100, text)
        p.showPage()
        p.save()

        buffer.seek(0)
        pdf_content = buffer.getvalue()
        buffer.close()

        instance.review_file.save(f'{instance.pk}.pdf', ContentFile(pdf_content))
