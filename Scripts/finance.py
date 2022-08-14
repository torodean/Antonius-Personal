##################################################################################
## Program: finance.py
## Author: Antonius Torode
## Date: 8/4/2022
## Purpose: For calculating various finance related things.
##################################################################################

import argparse
import math
import datetime


def extract_value(line, delimiter="="):
    """
    Extracts the value from the config line.
    The line should be formatted "variable=value".
    :param line: The line to parse
    :param delimiter:  The delimiter value to use. Default = "="
    :return variable: The variable preceding the delimiter
    :return value: The variable proceeding the delimiter
    """
    variable = line.split(delimiter)[0]
    value = line.split(delimiter)[1]
    return variable, value


def extract_config_value(line):
    """
    Extracts the keyword, identifier, and value of a config file line.
    The lines should be formatted "keyword_identifier=value"
    :param line: The line from the config file.
    :return keyword: The keyword found.
    :return identifier: The identifier found.
    :return value: The value found.
    """
    variable, value = extract_value(line, "=")
    keyword, identifier = extract_value(variable, "_")
    return keyword, identifier, value


def config_help():
    """
    Prints the config file help information.
    :return:
    """
    print("--- Config File File Information ---")
    print("Start all values with the appropriate field (keyword) followed by an underscore then an identifier.")
    print("Anything coming after the first underscore is an identifier.")
    print(
        "For example, utilities_gas and utilities_electric would give two salaries that will be added together when needed.")
    print("Valid keywords are salary, utilities, expense, etc.")
    print("Start all comments with a '#'. These lines will be ignored.")
    print("All values should be positive or negative depending on if it's added or subtracted to the totals each week.")


def get_medicare_taxes_from_total_income(total_income):
    """
    The Medicare tax (ignores pre-tax deductions) = 1.45% of total earnings.
    https://www.irs.gov/taxtopics/tc751
    :param total_income: The total earnings for the year.
    :return: the medicare yearly tax
    """
    medicare_rate = 0.0145
    return total_income * medicare_rate


def get_OASDI_taxes_from_total_income(total_income):
    """
    The OASDI (Old Age, Survivors, and Disability Insurance program) = 6.2% of total earnings (ignores pre-tax deductions).
    https://www.irs.gov/taxtopics/tc751
    :param total_income: The total earnings for the year.
    :return: the OASDI yearly tax
    """
    OASDI_rate = 0.062
    return total_income * OASDI_rate


class Finance:
    """
    The main class containing any finance related information.
    """

    def log(self, text, force_print=False):
        """
        Writes information to a log, optionally prints the data if verbose is enabled.
        :param: text is the text to log.
        :return:
        """
        log_file = open(self.log_file_name, "a")
        now = datetime.datetime.now()
        log_file.write("{}: {}\n".format(now, text))
        log_file.close()
        if self.verbose or force_print:
            print(text)

    def __init__(self):
        # Initialize variables
        self.log_file_name = "log.txt"  # log file name. Defaults to log.txt
        self.income = []  # Storage for all various income sources.
        self.total_income_monthly = 0  # Storage for total monthly income
        self.expenses = []  # Storage for all various expenses.
        self.total_expenses_monthly = 0  # Storage for total monthly expenses.
        self.pretax_expenses = []  # Storage for all various pretax expenses.
        self.total_pretax_expenses_monthly = 0  # Storage for total monthly pretax expenses.
        self.savings = []  # Storage for amount in monthly savings.
        self.inflation_starting = 0  # Starting inflation rate.
        self.inflation_variable = 0  # Variable inflation rate
        self.timeframe_months = 0  # timeframe to run the program (in months).

        self.parser = argparse.ArgumentParser()

        # Adds arguments that can be passed with program.
        self.parser.add_argument('-c',
                                 '--config',
                                 help='Config File to use.',
                                 type=str,
                                 required=False,
                                 default='None')
        self.parser.add_argument('-C',
                                 '--confighelp',
                                 help='Prints help information for the config file.',
                                 required=False,
                                 action='store_true',
                                 default=False)
        self.parser.add_argument('-v',
                                 '--verbose',
                                 help='Verbose Output.',
                                 required=False,
                                 action='store_true',
                                 default=True)  # TODO - remove this when testing is done.

        # Sets all passed arguments to program variables.
        args = self.parser.parse_args()
        self.verbose = args.verbose

        # Prints the help for the config.
        if args.confighelp:
            config_help()

        # config file defaults to "None" when no parameter is entered.
        self.configFile = args.config

        # Loads the config file.
        if self.configFile != "None":
            print("Loading config file: {}".format(self.configFile))
            self.load_config_file()
        else:
            print("ERROR: No config file entered.")
            exit(1)

        # This is the taxable income for federal taxes. It removes the pre-tax deductions from the total.
        self.taxable_income_yearly = self.total_income_monthly + self.total_pretax_expenses_monthly * 12.0
        self.log("Calculated taxable income: {0:.2f}".format(self.taxable_income_yearly))
        self.generate_inflation_model()

    def load_config_file(self):
        """
        This does the work of loading the config file.
        :return:
        """
        file = open(self.configFile, "r")

        for line in file.readlines():
            # Ignore comments.
            if line[0] == '#':
                continue
            else:
                comment_start_loc = line.find("#")
                line = line[0:comment_start_loc]

            # set all variables to lower case.
            line.lower()

            # Search for logfile name and set appropriate value.
            if "logfile" in line:
                self.log_file_name = extract_value(line)[1]
                self.log("Log file set to: {}".format(self.log_file_name))

            # Search for salaries
            if "salary" in line or "income" in line:
                income_line = []
                keyword, identifier, value = extract_config_value(line)
                income_line.append(identifier)
                income_line.append(value)
                self.total_income_monthly += float(value)
                self.income.append(income_line)
                self.log("Added income line: {}".format(income_line))

            # Search for expenses
            if "expense" in line or "utilities" in line:
                expense_line = []
                keyword, identifier, value = extract_config_value(line)
                expense_line.append(identifier)
                expense_line.append(value)
                self.total_expenses_monthly += float(value)
                self.expenses.append(expense_line)
                self.log("Added expense line: {}".format(expense_line))

            # Search for savings
            if "saving" in line or "savings" in line:
                savings_line = []
                keyword, identifier, value = extract_config_value(line)
                savings_line.append(identifier)
                savings_line.append(value)
                if identifier == "starting" or identifier == "start":
                    self.savings.append(float(value))
                self.expenses.append(savings_line)
                self.log("Added savings line: {}".format(savings_line))

            # Search for pretax values
            if "pretax" in line:
                pretax_line = []
                keyword, identifier, value = extract_config_value(line)
                pretax_line.append(identifier)
                pretax_line.append(value)
                self.total_pretax_expenses_monthly += float(value)
                self.expenses.append(pretax_line)
                self.log("Added pretax line: {}".format(pretax_line))

            # Search for the timeframe value.
            if "timeframe" in line:
                value = extract_value(line)[1]
                self.timeframe_months += float(value) * 12.0
                self.log("Setting app time frame to {0:.2f} months.".format(self.timeframe_months))

            # Search for inflation rate values
            if "inflation" in line:
                keyword, identifier, value = extract_config_value(line)
                if "start" in identifier:
                    self.inflation_starting = float(value)
                    self.log("Starting inflation rate: {0:.4f}".format(self.inflation_starting))
                elif "variability" in identifier or "variable" in identifier:
                    self.inflation_variable = float(value)
                    self.log("Inflation variability rate: {0:.4f}".format(self.inflation_variable))

    def get_taxes_from_taxable_income(self, taxable_income, deduction=0.00, single=True, head_of_household=False):
        """
        Calculates taxes on a taxable income. Optimizes deductible based on input vs standard.
        :param taxable_income: The income to calculate taxes from.
        :param deduction: A deductible to use.
        :param single: True if filing as single, False if filing as a joint married couple.
        :param head_of_household: True if filing as head of household, False if not.
        :return: The percent tax rate and total taxes [percent, taxes]
        """
        self.log(
            "\nCalculating taxes with get_taxes_from_taxable_income({0:.2f}, {1:.2f})".format(taxable_income, single))
        total = 0

        # Values taken from https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2022
        # Start these arrays at 0.
        tax_bracket_single = [0.00, 10275.00, 41775.00, 89075.00, 170050.00, 215950.00, 539900.00, math.inf]
        tax_bracket_married = [0.00, 20550.00, 83550.00, 178150.00, 340100.00, 431900.00, 647850.00, math.inf]
        tax_rate_bracket = [0.00, 0.10, 0.12, 0.22, 0.24, 0.32, 0.35, 0.37]
        standard_deductible_single = 12950.00
        standard_deductible_head_of_household = 19400.00
        standard_deductible_married = 25900.00

        # Adjust values for single vs married.
        if single:
            if head_of_household:
                deductible = standard_deductible_head_of_household
                tax_bracket = tax_bracket_single
            else:
                deductible = standard_deductible_single
                tax_bracket = tax_bracket_single
        else:
            deductible = standard_deductible_married
            tax_bracket = tax_bracket_married

        # Use input deduction if larger than the standard deductible.
        if deduction > deductible:
            deductible = deduction

        # Adjust taxable income.
        taxable_income -= deductible
        self.log(
            "...Using gross taxable income as {0:.2f} with deductible of {1:.2f}".format(taxable_income, deductible))

        bracket = 1
        while True:
            if taxable_income > tax_bracket[bracket]:
                # Calculate the taxable income between brackets.
                tax_bracket_income = tax_bracket[bracket] - tax_bracket[bracket - 1]
                total += tax_rate_bracket[bracket] * tax_bracket_income
            else:
                # Calculate the taxable income left until next bracket cap.
                tax_bracket_income = taxable_income - tax_bracket[bracket - 1]
                total += tax_rate_bracket[bracket] * tax_bracket_income

                # Print this since it will be skipped for the last one.
                tax_bracket_income -= tax_rate_bracket[bracket]
                self.log("...bracket[{0}] = {1} -> total: {2:.2f}, temp_income: {3:.2f}".format(bracket,
                                                                                                tax_bracket[bracket],
                                                                                                total,
                                                                                                tax_bracket_income))

                break  # There's no more money to tax after this.

            tax_bracket_income -= tax_rate_bracket[bracket]
            self.log(
                "...bracket[{0}] = {1} -> total: {2:.2f}, temp_income: {3:.2f}".format(bracket, tax_bracket[bracket],
                                                                                       total, tax_bracket_income))
            bracket += 1

        percent = total / taxable_income
        total_monthly = total / 12.0
        self.log("Finished tax calculation - percent: {0:.4f}, total: {1:.2f})".format(percent, total))
        self.log("Total federal taxes: percent = {0:.4f}, yearly = {1:.2f}, monthly = {2:.2f}".format(percent, total,
                                                                                                      total_monthly))
        return percent, total

    def get_total_taxes(self):
        """
        Returns the total taxes paid yearly and monthly.
        :return: percentage, total_taxes_yearly, total_taxes_monthly
        """
        federal_taxes_yearly = self.get_taxes_from_taxable_income(self.taxable_income_yearly, True)[1]
        OASDI_taxes_yearly = get_OASDI_taxes_from_total_income(self.total_income_monthly)
        medicare_taxes_yearly = get_medicare_taxes_from_total_income(self.total_income_monthly)
        total_taxes_yearly = federal_taxes_yearly + OASDI_taxes_yearly + medicare_taxes_yearly
        total_taxes_monthly = total_taxes_yearly / 12.0
        percentage = total_taxes_yearly / self.total_income_monthly
        return percentage, total_taxes_yearly, total_taxes_monthly

    def compare_rent_to_mortgage(self, house_cost, down_payment, interest_rate, rent, upkeep=0.04):
        """
        This method will compare a long term mortgage payment to rent.
        With respect to a mortgage, the interest payment is essentially waste, where as with respect to a rent
        payment, the rent is essentially waste.
        :param interest_rate: The interest rate you are paying on the loan.
        :param down_payment: The down payment made on the house.
        :param upkeep: The upkeep costs for maintanence on the house yearly.
        :param house_cost: The house value.
        :param rent: The comparative rent value.
        :return:
        """

    def calculate_mortgate_payment(self, house_cost, principal, interest_rate, property_tax_rate=0.018, insurance_monthly=250.0):
        """
        This will calculate the monthly payment for a mortgage.
        :param house_cost: The total property cost - used for property taxes.
        :param principal: The principal value left on the loan.
        :param interest_rate: The interest rate of the loan.
        :param property_tax_rate: The property tax rate.
        :param insurance_monthly: The monthly insurance cost.
        :return: returns the total monthly payment
        """
        n = 30 * 12
        temp = math.pow((1 + interest_rate / 12), n)
        payment_monthly = principal * (interest_rate * temp / 12) / (temp - 1)
        self.log("Monthly mortgage cost: {0:.2f}".format(payment_monthly))
        property_taxes_monthly = house_cost * property_tax_rate / 12.0
        self.log("Monthly property taxes cost: {0:.2f}".format(property_taxes_monthly))
        self.log("Monthly insurance cost: {0:.2f}".format(insurance_monthly))
        total = payment_monthly + property_taxes_monthly + insurance_monthly
        self.log("Total monthly mortgage cost: {0:.2f}".format(total))
        return total

    def generate_inflation_model(self):
        """
        This will generate a monthly inflation model. Rates returned are percentage increases from the previous month.
        :return:
        """
        # Starting values.
        inflation_low = []
        inflation_base = []
        inflation_high = []
        inflation_low.append(self.inflation_starting)
        inflation_base.append(self.inflation_starting)
        inflation_high.append(self.inflation_starting)

        # Calculate monthly values.
        for i in range(1, int(self.timeframe_months)):
            inflation_base.append(inflation_base[i - 1])
            inflation_low.append(inflation_low[i - 1] * (1 - self.inflation_variable))
            inflation_high.append(inflation_high[i - 1] * (1 + self.inflation_variable))


if __name__ == '__main__':
    print("\n-- Starting finance calculator --")
    finance = Finance()

    percentage, total_taxes_yearly, total_taxes_monthly = finance.get_total_taxes()
    income_yearly = finance.taxable_income_yearly - total_taxes_yearly
    income_monthly = income_yearly / 12.0
    net_savings_monthly = income_monthly + finance.total_expenses_monthly

    finance.log("\n-- Finance Information --")
    finance.log("Total income from all sources: {0:.2f}".format(finance.total_income_monthly))
    finance.log("Adjusted income after pre-tax deductions: {0:.2f}".format(finance.taxable_income_yearly))
    finance.log("Total Taxes: Yearly = {0:.2f}, Monthly = {1:.2f}".format(total_taxes_yearly, total_taxes_monthly))
    finance.log("Percent of income paid to taxes: {0:.4f}".format(percentage))
    finance.log("Pre-tax/deduction monthly income: {0:.2f}".format(finance.total_income_monthly / 12.0))
    finance.log("Post-tax monthly income: {0:.2f}".format(income_monthly))
    finance.log("Total monthly expenses: {0:.2f}".format(finance.total_expenses_monthly))
    finance.log("Net monthly savings: {0:.2f}".format(net_savings_monthly))

    finance.calculate_mortgate_payment(350000, 280000, 0.059)
