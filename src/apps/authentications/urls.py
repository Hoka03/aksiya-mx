from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.authentications import views


urlpatterns = [
    # ===================  URLS OF JWT-TOKEN  ==========================
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ==================  URLS OF REGISTER   ==========================
    path('register/send-code/', views.SendCodeAPIView.as_view(), name='send-code'),
    path('register/verify-code/', views.VerifyCodeAPIView.as_view(), name='verify-code'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),

    # ==================  URLS OF FORGOT PASSWORD   ==========================
    path('forgot-password/', views.ForgotPasswordAPIView.as_view(), name='forgot-password'),
    path('forgot-password/confirm/', views.NewPasswordAPIView.as_view(), name='forgot-password'),

]

