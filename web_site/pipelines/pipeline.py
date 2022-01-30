

def get_avatar(backend, strategy, details, response,
               user=None, *args, **kwargs):
    url = None
    if backend.name == 'github':
        url = response.get('avatar_url', '')
    if backend.name == 'google-oauth2':
        try:
            url = response["picture"]
        except KeyError:
            url = response['image'].get('url')
        ext = url.split('.')[-1]
    if url:
        user.avatar = url
        user.save()
