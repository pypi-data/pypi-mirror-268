import datetime

BASE_HOSTNAME = "api4.energiinfo.se"
BASE_URL = "https://" + BASE_HOSTNAME + "/"
BASE_ENDPOINT = BASE_URL

# Commands
#cmd=login
CMD_LOGIN="login"
CMD_LOGIN_TOKEN="login/access_token"
#cmd=login
CMD_LOGOUT="logout"
#cmd=meteringpoints
CMD_METERPOINTS="meteringpoints"
#cmd=invoices
CMD_INVOICES="invoices"
#cmd=servicesettings/get
CMD_SETTINGS="servicesettings/get"
#cmd=period
CMD_PERIOD="period"
#cmd=period/sort
CMD_SORT="period/sort"
#cmd=user/profile
CMD_PROFILE="user/profile"
#cmd=objectsettings
CMD_OBJECTSETTINGS="objectsettings"
#cmd=temperature
CMD_TEMPERATURE="temperature"
#cmd=temperature
CMD_OBJECTSETTINGS="objectsettings"
CMD_LOADERSTATUS="loader/status"


USER_AGENT_TEMPLATE = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/85.0.{BUILD}.{REV} Safari/537.36"
)
CLIENT_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

TOKEN_EXPIRATION = datetime.timedelta(minutes=60)