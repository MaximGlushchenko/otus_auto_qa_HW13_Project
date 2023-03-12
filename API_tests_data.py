from random import randint, choice

api_username = 'Default'
api_key = '10xocPi4Lbx4P4UiPzSDzAvMQIk5WaZSz2t9EKd2QtQKOdxF8jby9NU4PJ6rAAUSUzUW' \
          'yPSOsMBxUBEkXCSgsxcEqLzoQ9ixCvvJEGYviHz7pq7s2EaNH6TxMPXqmsHZ5oY2PT7X' \
          'Fg5UbyyYZPbnOf6WSW5kP7DipSxgxKxABcwNAbAHNhsbielTxy2uUCQhDNaPv6MuZLfh' \
          'yRephC9WFNNxfsl893HUaS5ZetsbfR6jiXeWdL2W6X8nUPRKNFD5'

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
