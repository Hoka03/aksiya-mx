from django.urls import path

from apps.discounts.views import discount_service, discount_image, discount


urlpatterns = [
    #       DISCOUNT CRUD URLS OF APIVIEW
    path('discount/', discount.DiscountListAPIView.as_view(),
         name='list_discount'),
    path('discount-create', discount.DiscountCreateAPIView.as_view(),
         name='create_discount'),
    path('discount-update/<int:pk>/', discount.DiscountUpdateAPIView.as_view(),
         name='update_discount'),
    path('discount-delete/<int:pk>/', discount.DiscountDestroyAPIView.as_view(),
         name='delete_discount'),
    path('discount-retrieve/<int:pk>/', discount.DiscountCreateAPIView.as_view(),
         name='retrieve_discount'),


    #       DISCOUNT IMAGE URLS OF APIVIEW
    path('discount-image/', discount_image.DiscountImageListAPIView.as_view(),
         name='list_discount_image'),
    path('discount-image-create/', discount_image.DiscountImageCreateAPIView.as_view(),
         name='create_discount_image'),
    path('discount-image-update/<int:pk>/', discount_image.DiscountImageUpdateAPIView.as_view(),
         name='update_discount_image'),
    path('discount-image-delete/<int:pk>/', discount_image.DiscountImageDestroyAPIView.as_view(),
         name='delete_discount_image'),
    path('discount-image-retrieve/<int:pk>/', discount_image.DiscountImageRetrieveAPIView.as_view(),
         name='retrieve_discount_image'),


    #       DISCOUNT SERVICE URLS OF APIVIEW
    path('service-discount/', discount_service.ServiceDiscountListAPIView.as_view(),
         name='list_service_discount'),
    path('service-discount-create/', discount_service.ServiceDiscountCreateAPIView.as_view(),
         name='create_service_discount'),
    path('service-discount-update/<int:pk>/', discount_service.ServiceDiscountUpdateAPIView.as_view(),
         name='update_service_discount'),
    path('service-discount-delete/<int:pk>/', discount_service.ServiceDiscountDestroyAPIView.as_view(),
         name='delete_service_discount'),
    path('service-discount-retrieve/<int:pk>/', discount_service.ServiceDiscountRetrieveAPIView.as_view(),
         name='retrieve_service_discount'),

]


