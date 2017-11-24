

from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveAPIView
from book_management.models import Pet
from .serializers import (
						 
						  AuthorCreateSerializer,
					
						)
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from django.contrib.auth.mixins import LoginRequiredMixin



# class BookListAPIView(ListAPIView):
# 	queryset=Book.objects.all()
# 	serializer_class=BookListSerializer




# class BookDetailAPIView(RetrieveAPIView):
# 	queryset=Book.objects.all()
# 	serializer_class=BookDetailSerializer
# 	lookup_field='pk'

	


# class BookCreateAPIView(CreateAPIView):
# 	queryset=Book.objects.all()
# 	serializer_class=BookcreateSerializer
# 	permission_classes=[IsAdminUser,]



# class BookInstanceCreateAPIView(CreateAPIView):
#     queryset=BookInstance.objects.all()
#     serializer_class=BookInstanceCreateSerializer
#     permission_classes=[IsAuthenticated,IsAdminUser]
#     permission_classes=[IsAdminUser,]

  

    # def perform_create(self, serializer):
    #     serializer.save(borrower=self.request.user)
    #     return self.request.user
 
 


# class GenreCreateAPIView(CreateAPIView):
# 	queryset=Genre.objects.all()
# 	serializer_class=GenreCreateSerializer
# 	permission_classes=[IsAdminUser,]



class AuthorCreateAPIView(CreateAPIView):
	queryset=Pet.objects.all()
	template_name = 'pet_list.html'
	serializer_class=AuthorCreateSerializer
	permission_classes=[IsAdminUser,]


# class InstanceAPIView(ListAPIView):
#     queryset=BookInstance.objects.all()
#     serializer_class=BookInstanceListSerializer
   

#     def get_queryset(self):
#             return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')










