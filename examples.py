from fixturefactory import BaseFactory, DjangoMixin

import random

from hunchworks.models import UserProfile, Connection, TranslationLanguage, Invitation
from django.contrib.auth.models import User
from hunchworks import hunchworks_enums as enums


class ConnectionFactory(BaseFactory, DjangoMixin):
    model = Connection
    pk1=None
    pk2=None

    def getparams(self):
        user_profile_id = self.pk1 or self.getRandInst(UserProfile).pk
        other_user_profile_id = self.pk2 or self.getRandInst(UserProfile).pk
        status = random.choice(enums.ConnectionStatus.GetChoices())[0]
        return locals()

class UserFactory(BaseFactory, DjangoMixin):
    model = User

    def getparams(self):
        """ Define parameters to create a new object with.
        Return dict"""

        pk = self.getUnusedPk()
        username = 'markov_%s' % pk
        password = username

        return locals()

class UserProfileFactory(BaseFactory, DjangoMixin):
    model = UserProfile

    def getparams(self):
        user = UserFactory().last_obj_created
        pk = user.pk
        title = random.choice(enums.UserTitle.GetChoices())[0]
        email = '%s@testhunchworks.com' % (user.username)
        privacy = random.choice(enums.PrivacyLevel.GetChoices())[0]

        bio_text = "Soon to be markov text"
        phone = self.phonenumber()
        skype_name = "%s_onskype" % user.username
        website = self.website(user.username)
        #profile_picture = models.ImageField(upload_to="profile_images", blank=True)
        messenger_service = random.choice(enums.MessangerServices.GetChoices())[0]
        translation_language = self.getRandInst(TranslationLanguage)
        invitation = self.getRandInst(Invitation)

        #ConnectionFactory(uid1=pk, uid2=self.getRandInst(model=UserProfile).pk)
        return locals()

    def phonenumber(self):
        return  ''.join([str(random.randint(0,9))
                for x in range(random.choice([7,10,11,13,20]))])
    def website(self, subdomain):
        return  "%s%s%s" % (
                    random.choice(['www.','', 'http://', 'http://www.']),
                    subdomain,
                    random.choice(['.com', '.org', '.me', '.uk', '.it']))

