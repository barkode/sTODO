from time import sleep

import gspread
from google.oauth2.service_account import Credentials

from utils import gen_task_id, time_stamp

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open used google sheets document
SHEET = GSPREAD_CLIENT.open("stodo")


def update_cell(ws, row: int, col: int, data: str):
    ws.update_cell(row, col, data)


def delete_task(user_name: str, task_num: str):
    ws = SHEET.worksheet(user_name)
    row_num = int(task_num) + 1
    ws.delete_rows(row_num)


def edit_task(user_name: str, task_num: str):
    ws = SHEET.worksheet(user_name)
    row_data = ws.row_values(int(task_num) + 1)
    print(row_data)
    print(row_data[2])
    cell = ws.find(row_data[2])
    changed_data = input()
    update_cell(ws, cell.row, 1, changed_data)
    sleep(10)


def show_tasks(user_name: str) -> list:
    ws = SHEET.worksheet(user_name)
    return ws.get_all_records()


def worksheet_append_row(ws_name: str, row: list):
    ws = SHEET.worksheet(ws_name)
    ws.append_row(row)


def add_user_to_base(user_name: str, user_password: str, user_role="user"):
    """
    Function add the new user to the users base
    """
    user = [user_name, user_password, user_role]
    worksheet_append_row("users", user)


def check_user_name(user_name: str) -> bool:
    """
    Function check if user name exist in base
    """
    ws = SHEET.worksheet("users")
    users = ws.col_values(1)[1:]
    if user_name in users:
        print("Sorry the name is exist. Try other name.\n")
        return False
    return True


def check_user_password(user_name: str, user_password: str) -> bool:
    ws = SHEET.worksheet("users")
    lst = ws.get_all_values()
    for el in lst:
        if (el[0] == user_name) and (el[1] == user_password):
            return True
    return False


def create_user_tasks_page(name: str):
    """
    Create a worksheet for each user
    """
    user_wsp = SHEET.add_worksheet(title=name, rows=1, cols=2)
    user_wsp.append_row(["task", "time_stamp"])


def add_task(user_name: str, task: str):
    time_stmp = time_stamp()
    gen_id = gen_task_id()
    user_task = [task, time_stmp, gen_id]
    return worksheet_append_row(user_name, user_task)


def check_user_name_entering(user_name):
    """
    Input user name. Check if user enter not empty string.
    """
    if len(user_name) > 30:
        return {"bool": False, "msg": "The length cannot be more than 30 characters"}
    for char in user_name:
        if (
            char
            not in "aAbBcCdDeEfFgGhHiIgGkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890_"
        ):
            return {
                "bool": False,
                "msg": "The login must contain letters, numbers and an underscore",
            }
    return {"bool": True, "msg": user_name}
