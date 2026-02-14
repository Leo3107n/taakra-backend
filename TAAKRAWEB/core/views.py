from rest_framework import generics, permissions, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import Category, Competition, Registration
from .serializers import CategorySerializer, CompetitionSerializer, RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]

class CompetitionListView(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]
    
class CompetitionDetailView(generics.RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

class RegisterCompetitionView(APIView):
    def post(self, request):
        user = request.user
        competition_id = request.data.get("competition_id")
        try:
            competition = Competition.objects.get(id=competition_id)
            reg, created = Registration.objects.get_or_create(user=user, competition=competition)
            if not created:
                return Response({"detail": "Already registered"}, status=status.HTTP_400_BAD_REQUEST)
            competition.registrations_count += 1
            competition.save()
            return Response({"detail": "Registered successfully"}, status=status.HTTP_201_CREATED)
        except Competition.DoesNotExist:
            return Response({"detail": "Competition not found"}, status=status.HTTP_404_NOT_FOUND)

class MyRegistrationsView(generics.ListAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)
    


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class MostRegisteredCompetitionsView(generics.ListAPIView):
    serializer_class = CompetitionSerializer

    def get_queryset(self):
        return Competition.objects.annotate(
            registrations_count=Count('registration')
        ).order_by('-registrations_count')
    
class NewCompetitionsView(generics.ListAPIView):
    serializer_class = CompetitionSerializer

    def get_queryset(self):
        return Competition.objects.all().order_by('-created_at')


class TrendingCompetitionsView(generics.ListAPIView):
    serializer_class = CompetitionSerializer

    def get_queryset(self):
        week_ago = timezone.now() - timedelta(days=7)
        return Competition.objects.filter(
            created_at__gte=week_ago
        ).annotate(
            registrations_count=Count('registration')
        ).order_by('-registrations_count')
    
class AIChatBotView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_message = request.data.get('message', '')
        # Hackathon quick fake AI reply
        reply = f"Hello! You asked: '{user_message}'. We'll get back to you shortly!"
        return Response({"reply": reply})