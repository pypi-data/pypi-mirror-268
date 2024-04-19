import csv
import datetime
import requests
import json
import urllib
import os
import ast
import hashlib
from os import path
import time
from zvolv_sdk.server_configuration import EnvVariables
from zvolv_sdk import submission

class CommonApi():

    def __init__(self,headers,zvice_id):
        login_response = ast.literal_eval(repr(self))
        self.zvice_id = login_response['businesstagid']
        self.headers = {
            'jwt':  login_response['loginToken'],            
            'Device': 'script',
            'Businessdomain': login_response['businessDomain'],
            'Businesstagid': login_response['businesstagid'],
            'Content-Type': 'application/json'
        }
    
    def create_form_submission(self,form_id, payload):
        login_data = repr(self)
        form_id = str(form_id)

        url = EnvVariables.get_zvolv_localhost_url()+EnvVariables.get_api_17_version() + self.zvice_id + "/forms/" + form_id + "/submissions/"
        method = "POST"

        json_response = submission.execute(rest_url=url, method="POST", data=json.dumps(payload), headers=self.headers)
        print(json_response)
        if 'cardid' in json_response:
            return json_response['cardid']
        else:
            return None


    def update_form_submission(self, form_id, input_data, submission_id):
        form_id = str(form_id)
        submission_id = str(submission_id)
        url = EnvVariables.get_zvolv_localhost_url()+EnvVariables.get_api_17_version() + self.zvice_id + "/forms/" + form_id + "/submissions/" + submission_id
        method = "PUT"
        json_response = submission.execute(rest_url=url, method=method, data=json.dumps(input_data), headers=self.headers)
        return json_response



            ## ref by EDIT_submission_using_NEW_API_sujoy API 
    def update_form_submission1(self, form_ID, input_data, submission_ID, donotcall=None,
                                            extra_autoSearch=None,php_engine=False):
        form_ID = str(form_ID)
        submission_ID = str(submission_ID)        
        body = {}
        if "FormData" in input_data.keys():
            if "type" in input_data['FormData'].keys():
                if input_data['FormData']["type"] == "KEY_LABELS":
                    body['FormData'] = input_data['FormData']
        else:
            subFieldMetaID = self.get_submissionAndfieldMetaID(form_ID, submission_ID)
            subContent = subFieldMetaID['data']['elements'][0]['content']
            print("checked")
            jasub = json.loads(subContent)
            body = {}
            for a in jasub['Elements'][0]['Elements']:
                for k, v in input_data.items():
                    if k == str(a['FormMetaID']):
                        body[a['FormMetaID']] = v
        body['OverrideMetaData'] = False
        method = "PUT"


        if donotcall is None:
            url = EnvVariables.get_zvolv_localhost_url()+EnvVariables.get_api_17_version() + self.zvice_id + "/forms/" + form_ID + "/submissions/" + submission_ID
        else:
            if php_engine:
                url = EnvVariables.get_zvolv_localhost_url()+EnvVariables.get_api_17_version() + self.zvice_id + "/forms/" + form_ID + "/submissions/" + submission_ID \
                  + "?do_not_call_python=" + donotcall + "&execute_engine=true"
            else:
                url = EnvVariables.get_zvolv_localhost_url()+EnvVariables.get_api_17_version() + self.zvice_id + "/forms/" + form_ID + "/submissions/" + submission_ID \
                      + "?do_not_call_python=" + donotcall

        if extra_autoSearch:
            body.update(extra_autoSearch)
        jsonresponse = submission.execute(rest_url=url, method=method, data=json.dumps(body), headers=self.headers)
        return jsonresponse
    
    def get_submissionAndfieldMetaID(self,formID,subID):
        login_data = repr(self)
        formID = str(formID)        
        url = EnvVariables.get_zvolv_localhost_url()+EnvVariables.get_api_17_version() + self.zvice_id + "/forms/" + str(formID) + "/submissions/" + str(subID)
        method = "GET"
        body = {}
        resp = submission.execute(rest_url=url, method=method, data=body, headers=self.headers)
        return resp