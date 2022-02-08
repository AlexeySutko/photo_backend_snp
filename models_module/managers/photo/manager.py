from django.db.models.manager import BaseManager


class CustomPhotoManager(BaseManager):
    """
    Custom user manager to use email as identifier
    instead of username in authentication / user creation
    """

    def create_photo(self, owner, image, name, description):
        """
        Create and save photo
        """
        photo = self.model(owner=owner, owner_id=owner.id, image=image, name=name, description=description)
        return photo.save()
