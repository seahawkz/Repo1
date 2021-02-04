import os
import json

import pandas as pd
from sqlalchemy import create_engine


def roster(cluster: str, login: str, fc: str) -> pd.DataFrame:

    """
    :return: roster data frame.
    """

    os.chdir("../configurations/")

    with open("config.json") as json_conf:
        conf = json.load(json_conf)[cluster]
        db = conf["db"]
        host = conf["host"]
        port = conf["port"]
        password = conf["password"]

    query = """
               SELECT fce.employee_id,
                      fce.user_id,
                      fce.shift_pattern,
                      fce.employee_name,
                      fce.supervisor_name,
                      fce.supervisor_user_id,
                      fce.supervisor_employee_id,
                      fce.fc_mgmt_area_id,
                      fce.job_title,
                      fce.psoft_location,
                      fc.warehouse_id, 
                      fce.employee_status
               FROM na_acs_met_ddl.fc_employees fce
               JOIN na_acs_met_ddl.fcs fc
                   ON fce.psoft_location = fc.psoft_location
               WHERE fc.warehouse_id = """ + "'" + fc + "'" + """
                   AND fce.employee_status in ('A', 'L');
            """

    red_engine = create_engine(f"postgresql://{login}:{password}@{host}:{port}/{db}")

    df = pd.read_sql_query(query, red_engine)

    roster_df = pd.DataFrame(df)

    # Clean up column headers
    roster_df.columns = roster_df.columns.str.strip().str.upper().str.replace(r"\W+", "_", regex=True)

    return roster_df