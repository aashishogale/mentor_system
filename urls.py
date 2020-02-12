from core_views.views import ReturnLink, GetTags, AuthorizationToken, FinalTagCommand, downloadQuestionLink, UpdateRepositoryStatus,ShowAvailableQuestions,ShowUserScreen,ShowMentorScreen
from flask import Blueprint

mentor_system = Blueprint('mentor_system', __name__)

mentor_system.add_url_rule("/getAuthorization", view_func=AuthorizationToken.as_view('authorization_token'), methods=["POST"])
mentor_system.add_url_rule("/getDownloadLink", view_func=downloadQuestionLink.as_view('get_download_link'), methods=["POST"])
mentor_system.add_url_rule("/updateRepositoryStatus", view_func=UpdateRepositoryStatus.as_view('updateRepositoryStatus'), methods=["POST"])
mentor_system.add_url_rule("/showAllQuestions", view_func=ShowAvailableQuestions.as_view('showAvailableQuestions'), methods=["GET"])
mentor_system.add_url_rule("/showMentorScreen", view_func=ShowMentorScreen.as_view('showMentorScreen'), methods=["GET"])
mentor_system.add_url_rule("/showUserScreen", view_func=ShowUserScreen.as_view('showUserScreen'), methods=["GET"])
mentor_system.add_url_rule("/showCommandString", view_func=ReturnLink.as_view('showCommandString'), methods=["POST"])
mentor_system.add_url_rule("/saveTagLink", view_func=FinalTagCommand.as_view('saveTagLink'), methods=["POST"])
mentor_system.add_url_rule("/getTagLink", view_func=GetTags.as_view('getTags'), methods=["GET"])