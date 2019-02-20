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
            "page": page
        }