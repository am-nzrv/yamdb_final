from csv import DictReader
from django.core.management import BaseCommand
from reviews.models import Comments, Review, GenreTitle, Title, Genre, Category
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        for row in DictReader(open('./static/data/users.csv',
                                   encoding='latin-1')):
            user = User(id=row['id'],
                        username=row['username'],
                        email=row['email'],
                        role=row['role'])
            user.save()
        for row in DictReader(open('./static/data/category.csv',
                                   encoding='latin-1')):
            category = Category(name=row['name'],
                                slug=row['slug'])
            category.save()
        for row in DictReader(open('./static/data/genre.csv',
                                   encoding='latin-1')):
            genre = Genre(name=row['name'],
                          slug=row['slug'])
            genre.save()
        for row in DictReader(open('./static/data/titles.csv',
                                   encoding='latin-1')):
            title = Title(name=row['name'],
                          year=row['year'],
                          category_id=row['category'])
            title.save()
        for row in DictReader(open('./static/data/genre_title.csv',
                                   encoding='latin-1')):
            genre_title = GenreTitle(title_id=row['title_id'],
                                     genre_id=row['genre_id'])
            genre_title.save()
        for row in DictReader(open('./static/data/review.csv',
                                   encoding='latin-1')):
            review = Review(id=row['id'],
                            title_id=row['title_id'],
                            text=row['text'],
                            author_id=row['author'],
                            score=row['score'],
                            )
            review.save()
        for row in DictReader(open('./static/data/comments.csv',
                                   encoding='latin-1')):
            comments = Comments(id=row['id'],
                                review_id=row['review_id'],
                                text=row['text'],
                                author_id=row['author'],
                                )
            comments.save()
