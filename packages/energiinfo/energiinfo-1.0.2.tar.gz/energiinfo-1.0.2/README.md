# `energiinfo`
The `energiinfo` is a python wrapper for energiinfo API


The background color is `#ffffff` for light mode and `#000000` for dark mode.
Simple code example:
```from energiinfo.api import EnergiinfoClient

api = EnergiinfoClient('https://api4.energiinfo.se','siteid','username','password')

if api.getLoginStatus() == True and api.getStatus() == "OK":
    print("====== avbrottsinfo ======")
    avbrottsinfo = api.get_interruptions()
    print(avbrottsinfo)
    print("====== meteringpoints ======")
    meter_list = api.get_metering_points()
    print(meter_list)
    print("====== invoices ======")
    invoices = api.get_invoices('2024')
    print(invoices)
    print("====== period 2024 ======")
    period_data = api.get_period_values('107223', '2024', 'ActiveEnergy', 'month')
    print(period_data)
    print("====== period 202402 ======")
    period_data = api.get_period_values('107223', '202402', 'ActiveEnergy', 'day')
    print(period_data)
    print("====== period 20240225 ======")
    period_data = api.get_period_values('107223', '20240225', 'ActiveEnergy', 'hour')
    print(period_data)
    print("====== period 2024030800 ======")
    period_data = api.get_period_values('107223', '2024030800', 'ActiveEnergy', 'quarter')
    print(period_data)
    api.logout()
else:
    print('Login failed: ' + api.getErrorMessage())
```

