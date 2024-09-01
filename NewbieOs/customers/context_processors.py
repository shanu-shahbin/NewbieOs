from django.contrib.auth.models import User

def user_count(request):
    """
    Context processor to add the user count to all templates.
    """
    user_count = User.objects.count()  # Count all users
    return {'user_count': user_count}
