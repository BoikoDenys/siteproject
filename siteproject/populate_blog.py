import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','siteproject.settings')

import django
django.setup()

import random
from blog.models import Post, Comment, UserProfileInfo
from faker import Faker

fakegen = Faker()

def populate(N=25):
    '''
    Create N Entries of Dates Accessed
    '''

    for _ in range(7):
        fake_username = fakegen.user_name()
        fake_email = fakegen.email()
        fake_password = fakegen.password(length=10)
        user = UserProfileInfo.objects.get_or_create(username=fake_username,
                                                    email=fake_email,
                                                    password=fake_password)[0]
        user.set_password(user.password)
        user.save()

    for entry in range(N):

        for _ in range(7):
            fake_username = fakegen.user_name()

            user = UserProfileInfo.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        fake_username = fakegen.user_name()
        fake_title =
        fake_date = fakegen.date()
        fake_name = fakegen.company()


        post = Post.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        comment = Comment.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
