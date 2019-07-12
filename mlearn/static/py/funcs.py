from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class StrToList:

    def strtolist(string):
        '''
        Transforms the string stored by Prepross model to list
        '''
        to_rem = ['[',
                  ']',
                  '[]',
                  ',']
        string = string.replace(" ", "").split("'")
        for i in to_rem:
            try:
                string = list(filter((i).__ne__, string))
            except:
                pass
        return string
