
def can_approve(instance):
    photo = instance
    if photo.future_name and photo.future_image is None:
        return False
    return True
