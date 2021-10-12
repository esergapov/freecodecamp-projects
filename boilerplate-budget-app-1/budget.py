class Category:

    def __init__(self, category_name):
        self.category_name = category_name
        self._ledger = []
        self._balance = 0

    @property
    def ledger(self):
         return self._ledger

    def deposit(self, amount, description=''):
        self._ledger.append({"amount": amount, "description": description})
        self.set_balance(amount)
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self._ledger.append({"amount": -amount, "description": description})
            self.set_balance(-amount)
            return True
        return False

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        self._balance += amount
    
    def transfer(self, amount, other):
        if self.withdraw(amount, f'Transfer to {other.category_name}'):
            other.deposit(amount, f'Transfer from {self.category_name}')
            return True
        return False

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True
    
    def __str__(self):
        summary_str = self.category_name.center(30, '*')
        for item in self._ledger:
            desc = item['description'].ljust(23)[:23]
            amount = '{0:.2f}'.format(item['amount']).rjust(7)
            
            summary_str += ''.join(('\n', desc, amount))
        summary_str += f'\nTotal: {self.get_balance()}'
        return summary_str


def create_spend_chart(categories_list):
    withdrawals_per_category_dict = sum_withdrawals(categories_list)
    withdrawals_sum = sum(withdrawals_per_category_dict.values())
    
    histogram_str = draw_histogram(withdrawals_per_category_dict, categories_list, withdrawals_sum)
    horizontal_str = draw_horizontal_line(categories_list)
    description_str = draw_category_names(categories_list, withdrawals_per_category_dict)

    return ''.join((histogram_str, horizontal_str, description_str))


def sum_withdrawals(categories_list):
    withdrawals_dict = dict()
    for category in categories_list:
        withdrawals = 0
        for transaction in category._ledger:
            if transaction['amount'] < 0:
                withdrawals -= transaction['amount']
        withdrawals_dict[category.category_name] = withdrawals
    return withdrawals_dict


def draw_histogram(withdrawals_dict, categories_list, all_withdrawals):
    histogram = "Percentage spent by category\n"

    for perc in list(range(100, -1, -10)):
        percentage_row = f'{perc}| '.rjust(5)
        for category in categories_list:
            if (withdrawals_dict[category.category_name] * 10 // all_withdrawals * 10) >= perc:
                percentage_row += 'o  '
            else:
                percentage_row += '   '
        histogram += f'{percentage_row}\n'
    return histogram


def draw_horizontal_line(categories_list):
    horizontal = '    -'
    for i in range(len(categories_list)):
        horizontal += '---'
    return horizontal


def draw_category_names(categories_list, withdrawals_dict):
    description = ''
    for i in range(len(max(withdrawals_dict.keys(), key=len))):
        description += '\n     '
        for category in categories_list:
            letter = next(iter(category.category_name[i:]), ' ')
            description += f'{letter}  '
    return description
