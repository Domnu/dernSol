from chat.models import MyUser

user = MyUser.objects.create_user(username='guy', password='your_password', email='guy@example.com')
user.save()
