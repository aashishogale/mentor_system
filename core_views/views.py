from flask.views import MethodView
from flask import Response
import json
from flask import render_template, redirect, request
from core_views.service import Authorization
from config import Config



class AuthorizationToken(MethodView):

    def post(self):
        result = Authorization().get_authorization_token(json.loads(request.data))          
        if not result:
            return Response(json.dumps({"token":""}), status=200, mimetype="application/json")
        return Response(json.dumps({"token":Config.GITHUB_TOKEN}), status=200, mimetype="application/json")


class downloadQuestionLink(MethodView):

    def post(self):
        result = Authorization().get_question(json.loads(request.data)) 
        return Response(json.dumps(result), status=200, mimetype="application/json")

class UpdateRepositoryStatus(MethodView):

    def post(self):
        result = Authorization().update_repository_status(json.loads(request.data)) 
        return Response(json.dumps(result), status=200, mimetype="application/json")


class ShowUserScreen(MethodView):

    def get(self):
        return render_template("userscreen.html")


class ShowMentorScreen(MethodView):

    def get(self):
        return render_template("mentorscreen.html")


class ShowAvailableQuestions(MethodView):

    def get(self):
        result = Authorization().get_all_questions()
        return Response(json.dumps(result), status=200, mimetype="application/json")


class ReturnLink(MethodView):

    def post(self):
        print(request.json)
        result = Authorization().get_commands(json.loads(request.data))
        return Response(json.dumps(result), status=200, mimetype="application/json")

class FinalTagCommand(MethodView):

    def post(self):
        result = Authorization().add_final_tags(json.loads(request.data))
        return Response(json.dumps(result), status=200, mimetype="application/json")

class GetTags(MethodView):

    def get(self):
        result = Authorization().getMentortags()
        return Response(json.dumps(result), status=200, mimetype="application/json")

