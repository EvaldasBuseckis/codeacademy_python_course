# import logging
#
# def dalyba(a, b):
#     return a / b
#
# a = 10
# b = 5
#
# padalinom = dalyba(a, b)
# logging.warning(f"Dalyba: {a} / {b} = {padalinom}")
#
# # WARNING:root:Dalyba: 10 / 5 = 2.0



import logging

# logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG)
#
# def dalyba(a, b):
#     try:
#         padalinom = a / b
#         logging.info(f"Dalyba {a} / {b} = {padalinom}")
#         return padalinom
#     except ZeroDivisionError:
#         logging.error(f"Dalyba: {a} / {b} negalima")
#
# a = 10
# b = 0
# padalinom = dalyba(a, b)
#
#
# logging.basicConfig(filename='aritmetika.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
#
# def dalyba(a, b):
#     return a / b
#
# a = 10
# b = 5
#
# padalinom = dalyba(a, b)
# logging.debug(f"Dalyba: {a} / {b} = {padalinom}")
#
# logging.basicConfig(
#     filename='asmenys.log',
#     level=logging.INFO,
#     format='%(asctime)s:%(levelname)s:%(message)s',
# )
#
# class Asmuo:
#
#     def __init__(self, vardas, pavarde):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         logging.info(f"Sukurtas darbuotojas: {self.vardas} {self.pavarde}")
#
# tadas = Asmuo("Tomas", "Kucinskas")
# rokas = Asmuo("Rokas", "Radzevicius")


# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler('aritmetika.log')
# logger.addHandler(file_handler)
#
# logger.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
# file_handler.setFormatter(formatter)
#
# def dalyba(a, b):
#     return a / b
#
# a = 10
# b = 5
#
# padalinom = dalyba(a, b)
# logger.info(f"Dalyba: {a} / {b} = {padalinom}")
#
#
# import math
#
#
# def sum(*args):
#     total = 0
#     for x in args:
#         total += x
#     return
#
#
# sum(2, 5, 6)
#
#
# def square_root(x: int) -> float:
#     answer = math.sqrt(x)
#     return answer
#
#
# # print(square_root(9))
#
# def len_of_sentence(x):
#     answer = len(x)
#     return answer
#
# # print(len_of_sentence("labadiena"))
#
#
# def divide(x: int, y: int) -> int:
#     return x/y
#
#
# import logging
#
# # logging.basicConfig(filename="aritmetika.log", level=logging.DEBUG)
# logging.basicConfig(filename="aritmetika.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
#
# def sum(*args):
#     total = 0
#     for x in args:
#         total += x
#     logging.debug(f"suma: {total}")
#     return total
#
#
# sum(2, 5, 6)
#
# def square_root(x: int) -> float:
#     answer = math.sqrt(x)
#     logging.info(f"square root: {answer}")
#     return answer
#
#
# square_root(9)
#




