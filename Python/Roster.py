import io

import urllib3
import pandas as pd
from requests_kerberos import HTTPKerberosAuth, OPTIONAL

from formatter import pandas_format
from retryer import requests_retry_session


def roster(fc):

    url = f"https://fclm-portal.amazon.com/reports/employeeRoster?reportFormat=CSV&warehouseId={fc}"

    with requests_retry_session() as req:
        resp = req.get(url,
                       timeout=30,
                       verify=False,
                       allow_redirects=True,
                       auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL))

        if resp.status_code == 200:

            # Convert string to dataframe
            df = pd.read_csv(io.StringIO(resp.text), sep=",")

            # Clean up headers
            df.columns = df.columns.str.strip().str.upper().str.replace(r"\W+", "_", regex=True)

            print(df)

        else:
            print(resp.raise_for_status())


if __name__ == "__main__":
    pandas_format()
    urllib3.disable_warnings()
    roster("RNO4")