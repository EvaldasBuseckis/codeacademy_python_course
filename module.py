from datetime import datetime

# def check_id(id:str) -> bool:
#
#     if len(id)!=11:
#         return False
#
#     for i in id:
#         try:
#             int(i)
#         except Exception as e:
#             return False
#
#     if 3 <= int(id[0]) and int(id[0]) <= 6:
#         return

our_date = "39609043712"


def check_date(id:str) -> bool:
    if int(id[0]) > 4:
        date = f"20{id[1:3]}-{id[3:5]}-{id[5:7]}"
    else:
        date = f"19{id[1:3]}-{id[3:5]}-{id[5:7]}"


    if type(datetime.strptime(date, "%Y-%m-%d")) == type(datetime):





check_date("39609043712")


# print(our_date[1:7])