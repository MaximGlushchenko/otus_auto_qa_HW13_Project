from random import randint, choice

api_username = 'Default'
api_key = '5HSZmRZZihkTwPDu2sW5hjpcmoD50HW3f1bMUtg4UiyGYQdyfXeMMUqrjX18zckqkmVonCoNp5p' \
          'GWVUkhGgkLfbGZrmJNGIMT3Pid3FekeAk667gCOVlxu1CNC9Dq3oVs8IoM9OxNjDcFG2ZXsFZyB' \
          'meG5LgNvEnm1ynajviaPY1Mpcu03roDuIVCpt6CZv1v5NPhLnGMwFE9Z6Yq5BtEy3TxQX3Lac2k' \
          'SSihedz6HW050tSueAQ7ZXwkegoaVbf'

CURRENCY_LIST = ['USD', 'EUR', 'GBP']

PRODUCT_ID_LIST = ['29', '31', '43', '34', '40', '32', '33', '40', '44']

COUPON_LIST = ['1111', '2222', '3333', '4444', '5555']

PRODUCT_ID_AND_QUANTITY_LIST = [(f'{choice(PRODUCT_ID_LIST)}', f'{randint(1, 2)}'),
                                (f'{choice(PRODUCT_ID_LIST)}', f'{randint(3, 4)}'),
                                (f'{choice(PRODUCT_ID_LIST)}', f'{randint(5, 6)}'),
                                (f'{choice(PRODUCT_ID_LIST)}', f'{randint(7, 8)}'),
                                (f'{choice(PRODUCT_ID_LIST)}', f'{randint(9, 10)}')]


KEY_AND_QUANTITY_LIST = [(f'{randint(1, 20)}', f'{randint(1, 10)}'),
                         (f'{randint(20, 40)}', f'{randint(1, 10)}'),
                         (f'{randint(40, 60)}', f'{randint(1, 10)}'),
                         (f'{randint(60, 80)}', f'{randint(1, 10)}'),
                         (f'{randint(80, 100)}', f'{randint(1, 10)}')]

KEY_LIST = [f'{randint(1, 20)}',
            f'{randint(20, 40)}',
            f'{randint(40, 60)}',
            f'{randint(60, 80)}',
            f'{randint(80, 100)}']
