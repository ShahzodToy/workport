from django.test import TestCase
from rest_framework.test import APIClient
from .models import Post, CategoryPost,CommentPost,Portfolio,CategoryPortfolio, Service, Comments,ContactUser, NewsLetterSubs,PricePlan # Import your Post and Category models
from .api.serializers import (PostSerializer ,CommentPostSerializer,
                              PortfoliWorkSerializer, ServiceSerializer, 
                              CommentSerializer,ContacSerializer,
                              NewsSubscribeSerializer,PricePlanserializer) # Import your PostSerializer
from django.db.models import Count
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse



class PostSerializerTest(APITestCase):

    def setUp(self):
        # Create sample category
        self.category = CategoryPost.objects.create(title='Tech')
        
        # Create sample post
        self.post = Post.objects.create(
            title="Test Post",
            desc="Test Post Description",
            img="test_img.jpg",
            category=self.category
        )
        
        # Add some tags to the post
        self.post.tags.add('Django', 'API')
        
        # Mocking the count_like and count_comment methods
        self.post.count_like = lambda: 5  # Mock like count as 5
        self.post.count_comment = lambda: 10  # Mock comment count as 10
        
        self.client = APIClient()

    def test_post_serializer_fields(self):
        # Serialize the post object
        serializer = PostSerializer(self.post)
        serialized_data = serializer.data

        # Assert that the data contains the expected fields and values
        self.assertEqual(serialized_data['title'], 'Test Post')
        self.assertEqual(serialized_data['desc'], 'Test Post Description')
        self.assertEqual(serialized_data['category'], self.category.id)
        self.assertEqual(serialized_data['tags'], ['Django', 'API'])
        self.assertEqual(serialized_data['like_count'], 5)
        self.assertEqual(serialized_data['comment_count'], 10)

    def test_post_serializer_like_count(self):
        # Ensure like count is properly calculated
        serializer = PostSerializer(self.post)
        self.assertEqual(serializer.data['like_count'], 5)

    def test_post_serializer_comment_count(self):
        # Ensure comment count is properly calculated
        serializer = PostSerializer(self.post)
        self.assertEqual(serializer.data['comment_count'], 10)

class CommentPostTest(APITestCase):

    def setUp(self):
        self.category = CategoryPost.objects.create(title='Tech')

        self.post = Post.objects.create(
            title="Test Post",
            desc="Test Post Description",
            img="test_img.jpg",
            category=self.category
        )

        self.comment_post = CommentPost(
            comment = 'Juda zor ekan',
            post = self.post,
            user_name = 'Shahzod',
            email = 'aaaa@gmail.com',
            website = 'google.com'
            )
                      
        self.client = APIClient()

    def test_comment_post(self):

        serializer = CommentPostSerializer(self.comment_post)
        serialized_data = serializer.data

        # Assert that the data contains the expected fields and values
        self.assertEqual(serialized_data['comment'], 'Juda zor ekan')
        self.assertEqual(serialized_data['post'], self.post.id)
        self.assertEqual(serialized_data['user_name'], 'Shahzod')
        self.assertEqual(serialized_data['email'], 'aaaa@gmail.com')
        self.assertEqual(serialized_data['website'], 'google.com')


class PortfolioTest(APITestCase):

    def setUp(self):
        self.category = CategoryPortfolio.objects.create(
            title = 'tech'
        )

        self.portfolio = Portfolio.objects.create(
            img = 'test1.jpg',
            category = self.category
        )

        self.client = APIClient()

    def test_portfolio(self):

        serializer = PortfoliWorkSerializer(self.portfolio)
        serialized_data = serializer.data

        self.assertEqual(serialized_data['img'], '/media/test1.jpg')
        self.assertEqual(serialized_data['category'], self.category.id)
       
class ServiceTest(APITestCase):

    def setUp(self):
        self.service = Service.objects.create(
            logo = 'test1.jpg'
        )
    def test_service(self):

        serializer = ServiceSerializer(self.service)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['logo'],'/media/test1.jpg')

class PortfolioCommentTest(APITestCase):

    def setUp(self):
        self.category = CategoryPortfolio.objects.create(
            title = 'tech'
        )

        self.portfolio = Portfolio.objects.create(
            img = 'test1.jpg',
            category = self.category
        )

        self.comment = Comments.objects.create(
            username = 'Shahzod',
            comment = 'Juda zor ekan',
            user_job = 'data enginer',
            portfolio = self.portfolio,
            rating = 2
        )

        self.client = APIClient()

    def test_portfolio_comment(self):
            
            serializer = CommentSerializer(self.comment)
            serializer_data = serializer.data

            self.assertEqual(serializer_data['username'],'Shahzod')
            self.assertEqual(serializer_data['comment'],'Juda zor ekan')
            self.assertEqual(serializer_data['user_job'],'data enginer')
            self.assertEqual(serializer_data['portfolio'],self.portfolio.id),
            self.assertEqual(serializer_data['rating'],2)
        
class ContactTest(APITestCase):

    def setUp(self):
        self.contact = ContactUser.objects.create(
            email = 'aaa@gmail.com',
            first_name = 'shahzod',
            subject = '123456',
            message = 'soqa'        
            )
        
    def test_service(self):

        serializer = ContacSerializer(self.contact)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['email'],'aaa@gmail.com')
        self.assertEqual(serializer_data['first_name'],'shahzod')
        self.assertEqual(serializer_data['subject'],'123456')
        self.assertEqual(serializer_data['message'],'soqa')


class NewSubscriptionTest(APITestCase):

    def setUp(self):
        self.service = NewsLetterSubs.objects.create(
            email = 'aaa@gmail.com'
        )
    def test_service(self):

        serializer = NewsSubscribeSerializer(self.service)
        serializer_data = serializer.data

        self.assertEqual(serializer_data['email'],'aaa@gmail.com')

# class PricePlanTest(TestCase):

#     def setUp(self):
#         self.service = Service.objects.create(
#             logo = 'test1.jpg',
#             title = 'soqa',
#             desc = 'test1'
#         )

#         self.price = PricePlan.objects.create(
#             info = 'test2',
#             price = 12.00,
#             cretaria_text = 'test2'
#         )

#     def test_service(self):

#         serializer = PricePlanserializer(self.price)
#         serializer_data = serializer.data

       
#         self.assertEqual(serializer_data['info'],'test2')
#         self.assertAlmostEqual(float(serializer_data['price']), 12.00, places=2)
#         self.assertEqual(serializer_data['cretaria_text'],'test2')

# class PostDetailViewTest(APITestCase):

#     def setUp(self):
#         # Create dummy data for testing
#         self.category = CategoryPost.objects.create(title="Tech")
#         self.post = Post.objects.create(title="Test Post", desc="Content", category=self.category)
#         self.comment = CommentPost.objects.create(post=self.post, comment="Nice post!")
#         self.valid_post_url = reverse('post-detail', kwargs={'pk': self.post.id})
        
#     def test_get_valid_post(self):
#         """Test retrieving a valid post with comments and category count"""
#         response = self.client.get(self.valid_post_url)
        
#         post = Post.objects.get(id=self.post.id)
#         comments = CommentPost.objects.filter(post=self.post)
#         comment_serializer = CommentPostSerializer(comments, many=True)
#         post_serializer = PostSerializer(post)
#         category_count = CategoryPost.objects.annotate(post_count=Count('post')).values('title', 'post_count')

#         expected_data = {
#             'posts': post_serializer.data,
#             'comments': comment_serializer.data,
#             'category': category_count  # Converting queryset to list
#         }

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, expected_data)

    

 