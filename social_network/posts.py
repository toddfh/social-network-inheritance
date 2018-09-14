from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
        self.user = user

class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)
        self.text = text
        self.timestamp = timestamp
        self.readable_date = self.timestamp.strftime('%A, %b %d, %Y')

    def __str__(self):
        first_last = self.user.first_name + ' ' + self.user.last_name
        return '@{}: "{}"\n\t{}'.format(first_last, self.text,
                                        self.readable_date)


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        self.text = text
        self.image_url = image_url
        self.timestamp = timestamp
        self.readable_date = self.timestamp.strftime('%A, %b %d, %Y')

    def __str__(self):
        first_last = self.user.first_name + ' ' + self.user.last_name
        return '@{}: "{}"\n\t{}\n\t{}'.format(first_last, self.text,
                                self.image_url, self.readable_date)


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        self.text = text
        self.latitude = latitude
        self.longitude = longitude
        self.coords = str(self.latitude) + ', ' + str(self.longitude)
        self.timestamp = timestamp
        self.readable_date = self.timestamp.strftime('%A, %b %d, %Y')

    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}\n\t{}'.format(self.user.first_name,
        self.text, self.coords, self.readable_date)
