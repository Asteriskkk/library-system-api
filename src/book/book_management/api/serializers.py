from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField



from book_management.models import Book,BookInstance,Genre,Author

class BookListSerializer(serializers.ModelSerializer):
    book_detail_url =HyperlinkedIdentityField(
         view_name='api:book_details',
         lookup_field='pk'
         )
    class Meta:
        model=Book
        fields=['title','book_detail_url']
        



class BookcreateSerializer(serializers.ModelSerializer):
    back =HyperlinkedIdentityField(
         view_name='books'
         )
    class Meta:
        model=Book
        fields=['title','author','summary','isbn','genre','back']



class BookInstanceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookInstance
        fields=['borrower','book','imprint','due_back','status',]
      

class GenreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields=['name']





class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['first_name','last_name','date_of_birth','date_of_death']






class BookDetailSerializer(serializers.ModelSerializer):
    author= serializers.CharField(source="author.first_name",read_only=True)
    genre= GenreCreateSerializer(many=True,read_only=True)

    class Meta:
        model=Book
        fields=['title','author','summary','isbn','genre']



class BookInstanceListSerializer(serializers.ModelSerializer):
    # book = serializers.StringRelatedField(many=False)
    book = serializers.CharField(source="book.title", read_only=True)
    borrower = serializers.CharField(source="borrower.username", read_only=True)
    status = serializers.CharField(source="get_status_display", read_only=True)
    copies = BookDetailSerializer(source='book')

    class Meta:
        model=BookInstance
        fields=['borrower','copies','imprint','due_back','status','book']












