class CustomStrategy(object):
    """
    A strategy that ensures file creation on save and existence

    """

    def on_existence_required(self, file):
        file.generate()

    def on_content_required(self, file):
        file.generate()

    def on_source_saved(self, file):
        file.generate()