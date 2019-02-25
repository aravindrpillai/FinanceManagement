import datetime

from apps.categories.models import EN_Categories
from apps.userregistration.models import EN_Users
from properties.session_properties import SessionProperties

class StaticDataLoader:

    def __init__(self, request):
        self.user_id = request.session[SessionProperties.USER_ID]

    def getPageData(self, page):
        user = EN_Users.objects.get(id=self.user_id)
        return {
            "page_data":{
                "name": user.name,
                "email": user.email,
            },
            "page": page,
            "categories": self.__getUserCategories(),
            "current_date": datetime.datetime.now().strftime("%m/%d/%Y"),
        }

    def __getUserCategories(self):
        return [{
            "id":cat.id,
            "name":cat.name
        }for cat in EN_Categories.objects.filter(user_id=self.user_id, retired=False)]