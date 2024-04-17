from __future__ import annotations

import requests

from .const import (
    BASE_ENDPOINT,
    BASE_HOSTNAME,
    BASE_URL,
    CMD_LOGIN,
    CMD_LOGIN_TOKEN,
    CMD_LOGOUT,
    CMD_PROFILE,
    CMD_METERPOINTS,
    CMD_INVOICES,
    CMD_PERIOD,
    CMD_OBJECTSETTINGS,
    CMD_TEMPERATURE,
    CLIENT_HEADERS,
    TOKEN_EXPIRATION,
    USER_AGENT_TEMPLATE,
)

#https://api4.energiinfo.se/?access_token=none&cmd=login

class EnergiinfoClient:
    """
    A generic Python API client.
    """
    api_url: str
    session = ""
    access_token = None
    status = "OK"
    error_message = None
    logged_in = False
    siteid = ""

    def __init__(self, apiurl: str, siteid: str, token: str = None):
         self.api_url = apiurl
         self.session = requests.Session()
         self.siteid = siteid
         if token is not None:
             self.authenticateToken(token)
    def getStatus(self):
        return self.status

    def getErrorMessage(self):
        return self.error_message

    def authenticateToken(self, token: str):
        login_url = self.api_url + "/?cmd={}".format(CMD_LOGIN_TOKEN)

        data = {
            'site': self.siteid,
            'access_token': token,
        }

        error_message = ''

        try:
            response = self.session.post(login_url, data=data)
            # Check if the login request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                self.status = response.json().get('status')
                if self.status == 'ERR':
                    self.error_message = response.json().get('error_message')
                if self.status == 'OK':
                    self.logged_in = True
                    self.access_token = response.json().get('access_token')
                    return self.access_token
            elif response.status_code >= 400 and response.status_code < 500:
                self.status = 'ERR'
                self.error_message = f"Client Error: {response.status_code}"
                return {'status': self.status, 'error_message': self.error_message}
            elif response.status_code == 500:
                self.status = 'ERR'
                self.error_message = 'Internal server error'
                return {'status': self.status, 'error_message': self.error_message}
            else:
                self.status = 'ERR'
                self.error_message = response.json().get('error_message')
                # print(f"Failed to execute cmd: {command}. Status code: {response.status_code}")
                return None
                self.error_message = str(e)
        except requests.exceptions.RequestException as e:
            # Handle request exceptions such as network errors
            self.status = 'ERR'
            self.error_message = f"Request Exception: {e}"
            return None
        except ValueError as e:
            # Handle JSON parsing errors
            self.status = 'ERR'
            self.error_message = f"JSON Parsing Error: {e}"
            return None
        except Exception as e:
            # Catch any other unexpected exceptions
            self.status = 'ERR'
            self.error_message = f"An unexpected error occurred: {e}"
            return None

    def get_access_token(self):
        if self.access_token is not None:
            self.authenticateToken(self.access_token)

        return self.access_token


    def authenticate(self, username: str, password: str, type: str = 'permanent'):
        headers = {
            # ... (your headers for login)
        }
        data = {
            'site': self.siteid,
            'Username': username,
            'Password': password,
            'Captcha': '',
            'type': type,  # permanent remembers the login
        }

        response = self.run_command(self.api_url, CMD_LOGIN, headers=headers, data=data)

        if response is not None:
            self.status = response.get('status', 'ERR')
            if self.status == 'OK':
                self.logged_in = True
                self.access_token = response.get('access_token')
            else:
                self.error_message = response.get('error_message', 'Unknown error')
                self.logged_in = False

            return self.access_token if self.status == 'OK' else None
        else:
            self.status = 'ERR'
            self.error_message = 'Authentication request failed.'
            return None

    def run_command(self, apiurl: str, command: str, headers, data):
        error_message = ''
        commandurl = apiurl + '/?access_token={}&cmd={}'.format(self.access_token, command)

        try:
            response = self.session.post(commandurl, headers=headers, data=data)
            # Check if the login request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                self.status = response.json().get('status')
                if self.status == 'ERR':
                    self.error_message = response.json().get('error_message')
                return response.json()
            elif response.status_code >= 400 and response.status_code < 500:
                self.status = 'ERR'
                self.error_message = f"Client Error: {response.status_code}"
                return {'status': self.status, 'error_message': self.error_message}
            elif response.status_code == 500:
                self.status = 'ERR'
                self.error_message = 'Internal server error'
                return {'status': self.status, 'error_message': self.error_message}
            else:
                self.status = 'ERR'
                self.error_message = response.json().get('error_message')
                # print(f"Failed to execute cmd: {command}. Status code: {response.status_code}")
                return None
                self.error_message = str(e)
        except requests.exceptions.RequestException as e:
            # Handle request exceptions such as network errors
            self.status = 'ERR'
            self.error_message = f"Request Exception: {e}"
            return None
        except ValueError as e:
            # Handle JSON parsing errors
            self.status = 'ERR'
            self.error_message = f"JSON Parsing Error: {e}"
            return None
        except Exception as e:
            # Catch any other unexpected exceptions
            self.status = 'ERR'
            self.error_message = f"An unexpected error occurred: {e}"
            return None
    def logout(self):
        if self.logged_in == True:
            response = self.run_command(self.api_url, CMD_LOGOUT, None, None)
        else:
            self.status = 'ERR'
            self.error_message = 'Not logged in'
            return None

        if response['status'] == 'OK':
            # Parse the JSON response
            self.status = response['status']
            if self.status == 'ERR':
                self.error_message = response_data.get('error_message')
                self.logged_in = False
            else:
                self.logged_in = False
        else:
            return None

    def get_metering_points(self):
        meterpoints = self.run_command(self.api_url, CMD_METERPOINTS, None, None)
        if meterpoints['status'] == 'OK':
            return meterpoints['list']
        else:
            return None

    def get_invoices(self, period):
        data_params = {
            'period': period,
        }
        invoicedata = self.run_command(self.api_url, CMD_INVOICES, None, data_params)
        if invoicedata['status'] == 'OK':
            return invoicedata['list']
        else:
            return None

    def get_interruptions(self, ):
        data_params = {
            'type': 'avbrottsinfo',
        }
        interruptions = self.run_command(self.api_url, CMD_OBJECTSETTINGS, None, data_params)
        print(interruptions)
        if interruptions['status'] == 'OK':
            return interruptions['value']
        else:
            return None

    def get_period_values(self, meteringpoint_id, period, signal, interval):
        data_params = {
            'meteringpoint_id': meteringpoint_id,
            'period': period,
            'signal': signal,
            'interval': interval,
        }
        perioddata = self.run_command(self.api_url, CMD_PERIOD, None, data_params)
        if perioddata and perioddata['status'] == 'OK':
            return perioddata['values']
        else:
            return None
