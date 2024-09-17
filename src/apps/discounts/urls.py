from django.urls import path

from apps.discounts.views import discount_service, discount_image, discount

urlpatterns = [
    #       DISCOUNT CRUD URLS OF APIVIEW
    path('discount/api/v1/', discount.DiscountListAPIView.as_view(),
         name='list_discount'),
    path('discount-create/api/v1', discount.DiscountCreateAPIView.as_view(),
         name='create_discount'),
    path('discount-update/api/v1/<int:pk>/', discount.DiscountUpdateAPIView.as_view(),
         name='update_discount'),
    path('discount-delete/api/v1/<int:pk>/', discount.DiscountDestroyAPIView.as_view(),
         name='delete_discount'),
    path('discount-retrieve/api/v1/<int:pk>/', discount.DiscountCreateAPIView.as_view(),
         name='retrieve_discount'),


    #       DISCOUNT IMAGE URLS OF APIVIEW
    path('discount-image/api/v1/', discount_image.DiscountImageListAPIView.as_view(),
         name='list_discount_image'),
    path('discount-image-create/api/v1/', discount_image.DiscountImageCreateAPIView.as_view(),
         name='create_discount_image'),
    path('discount-image-update/api/v1/<int:pk>/', discount_image.DiscountImageUpdateAPIView.as_view(),
         name='update_discount_image'),
    path('discount-image-delete/api/v1/<int:pk>/', discount_image.DiscountImageDestroyAPIView.as_view(),
         name='delete_discount_image'),
    path('discount-image-retrieve/api/v1/<int:pk>/', discount_image.DiscountImageRetrieveAPIView.as_view(),
         name='retrieve_discount_image'),


    #       DISCOUNT SERVICE URLS OF APIVIEW
    path('service-discount/api/v1/', discount_service.ServiceDiscountListAPIView.as_view(),
         name='list_service_discount'),
    path('service-discount-create/api/v1/', discount_service.ServiceDiscountCreateAPIView.as_view(),
         name='create_service_discount'),
    path('service-discount-update/api/v1/<int:pk>/', discount_service.ServiceDiscountUpdateAPIView.as_view(),
         name='update_service_discount'),
    path('service-discount-delete/api/v1/<int:pk>/', discount_service.ServiceDiscountDestroyAPIView.as_view(),
         name='delete_service_discount'),
    path('service-discount-retrieve/api/v1/<int:pk>/', discount_service.ServiceDiscountRetrieveAPIView.as_view(),
         name='retrieve_service_discount'),

]


