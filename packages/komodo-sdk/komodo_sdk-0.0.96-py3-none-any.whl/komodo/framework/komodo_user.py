from komodo.shared.utils.digest import get_text_digest


class KomodoUser:
    def __init__(self, *, email, name, **kwargs):
        self.email = email
        self.name = name
        self.uid = kwargs.pop('uid', None)
        self.groups = kwargs.pop('groups', [])
        self.language = kwargs.pop('language', None)

        self.role = kwargs.pop('role', 'user')
        self.plan = kwargs.pop('plan', 'free')
        self.verified = kwargs.pop('verified', False)
        self.provider_id = kwargs.pop('provider_id', 'komodo')
        self.token = kwargs.pop('token', '')

        self.allowed_assistants = kwargs.pop('allowed_assistants', [])
        self.preferred_assistant = kwargs.pop('preferred_assistant', '')
        self.kwargs = kwargs

        # each user has a home folder / collection and a default downloads folder
        self.guid = get_text_digest(email)
        self.home_shortcode = self.guid + "_home"
        self.downloads_shortcode = self.guid + "_downloads"

    def __str__(self):
        return f"KomodoUser(email={self.email}, name={self.name}, " \
               f"role={self.role}, plan={self.plan}, verified={self.verified}, " \
               f"allowed_assistants={self.allowed_assistants}, preferred_assistant={self.preferred_assistant})"

    def to_dict(self):
        return {
            'email': self.email,
            'name': self.name,
            'role': self.role,
            'plan': self.plan,
            'verified': self.verified,
            'default_collection': self.home_shortcode,
            'allowed_assistants': self.allowed_assistants,
            'preferred_assistant': self.preferred_assistant}

    @staticmethod
    def default():
        email = "ryan.oberoi@komodoapp.ai"
        return KomodoUser(email=email, name="Ryan Oberoi")
