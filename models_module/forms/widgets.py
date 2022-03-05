from django.forms import ClearableFileInput


class ImageClearableFileInput(ClearableFileInput):
    template_name = 'image_clearable_file_input.html'