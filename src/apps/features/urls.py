from django.urls import path
from src.apps.features.views import feature_discounts, features, feature_values

urlpatterns = [
    #   FEATURE CRUD URLS OF APIVIEW
    path('feature/api/v1/', features.FeatureListAPIView.as_view(),
         name='list_feature'),
    path('feature-create/api/v1/', features.FeatureCreateAPIView.as_view(),
         name='create_feature'),
    path('feature-update/api/v1/<int:pk>/', features.FeatureUpdateAPIView.as_view(),
         name='update_feature'),
    path('feature-delete/api/v1/<int:pk>/', features.FeatureDestroyAPIView.as_view(),
         name='delete_feature'),
    path('feature-retrieve/api/v1/<int:pk>/', features.FeatureRetrieveAPIView.as_view(),
         name='retrieve_feature'),
    #   FEATURE VALUE URLS OF APIVIEW

    path('feature-value/api/v1/', feature_values.FeatureValueListAPIView.as_view(),
         name='list_feature_value'),
    path('feature-value-create/api/v1/', feature_values.FeatureValueCreateAPIView.as_view(),
         name='create_feature_value'),
    path('feature-value-update/api/v1/<int:pk>/', feature_values.FeatureValueUpdateAPIView.as_view(),
         name='update_feature_value'),
    path('feature-value-delete/api/v1/<int:pk>/', feature_values.FeatureValueDestroyAPIView.as_view(),
         name='delete_feature_value'),
    path('feature-value-retrieve/api/v1/<int:pk>/', feature_values.FeatureValueRetrieveAPIView.as_view(),
         name='retrieve_feature_value'),
    #   FEATURE DISCOUNT URLS OF APIVIEW

    path('discount-feature/api/v1/', feature_discounts.DiscountFeatureListAPIView.as_view(),
         name='list_discount_feature'),
    path('discount-feature-create/api/v1/', feature_discounts.DiscountFeatureCreateAPIView.as_view(),
         name='create_discount_feature'),
    path('discount-feature-update/api/v1/<int:pk>/', feature_discounts.DiscountFeatureUpdateAPIView.as_view(),
         name='update_discount_feature'),
    path('discount-feature-delete/api/v1/<int:pk>/', feature_discounts.DiscountFeatureDestroyAPIView.as_view(),
         name='delete_discount_feature'),
    path('discount-feature-retrieve/api/v1/<int:pk>/', feature_discounts.DiscountFeatureRetrieveAPIView.as_view(),
         name='retrieve_discount_feature'),

]
