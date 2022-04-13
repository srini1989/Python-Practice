GOMAIL_SERVER = "mx.gomail.com"
YOMAIL_SERVER = "mx.yomail.com"


class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class GoogleAccount(Contact):
    synced_contacts = []

    def sync(self):
        print("Syncing {} contact with Server".format(self.name))
        GoogleAccount.synced_contacts.append(self)
        return True

    def __str__(self):
        return "{}, {}".format(self.name, self.email)


class YahooAccount(Contact):
    synced_contacts = []

    def sync(self):
        print("Syncing {} contact with Server".format(self.name))
        YahooAccount.synced_contacts.append(self)
        return True

    def __str__(self):
        return "{}, {}".format(self.name, self.email)
