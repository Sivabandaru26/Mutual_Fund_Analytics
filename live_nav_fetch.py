<<<<<<< HEAD
import requests
import pandas as pd

funds = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

for name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    data = requests.get(url).json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/{name}.csv",
        index=False
    )

=======
import requests
import pandas as pd

funds = {
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

for name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    data = requests.get(url).json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/{name}.csv",
        index=False
    )

>>>>>>> 5e6528c2a8b061ca81cf7bebe5426257dfbb7c06
    print(name, "saved")