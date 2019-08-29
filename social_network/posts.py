from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=datetime.today()):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
        self.user = user

    def _string_last_name(self):
        return self.user.last_name

    def __str__(self):
        user_fullname = '@' + self.user.first_name + ' ' + self._string_last_name() + ': '
        post_timestamp = self.timestamp.strftime("%A, %b %d, %Y")
        post_text = '"{post_text}"'.format(post_text=self.text) + "\n\t"

        return user_fullname + post_text + self._string_helper() + post_timestamp


class TextPost(Post):
    def __init__(self, text, timestamp=datetime.today()):
        super().__init__(text, timestamp)

    def _string_helper(self):
        return ""


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=datetime.today()):
        super().__init__(text, timestamp)
        self.image_url = image_url

    def _string_helper(self):
        return self.image_url + "\n\t"


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=datetime.today()):
        super().__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def _string_last_name(self):
        return "Checked In"

    def _string_helper(self):
        return str(self.latitude) + ", " + str(self.longitude) + "\n\t"
