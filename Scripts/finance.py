##################################################################################
## Program: finance.py
## Author: Antonius Torode
## Date: 8/4/2022
## Purpose: For calculating various finance related things.
##################################################################################

import argparse
import math


class Finance:
    """
    The main class containing any finance related information.
    """

    def log(self, text):
        """
        Writes information to a log, optionally prints the data if verbose is enabled.
        :param: text is the text to log.
        :return:
        """
        # TODO - log to a file.
        if self.verbose:
            print(text)

    def __init__(self):
        self.parser = argparse.ArgumentParser()

        # Adds arguments that can be passed with program.
        self.parser.add_argument('-c',
                                 '--config',
                                 help='Config File to use.',
                                 type=str,
                                 required=False,
                                 default='None')
        self.parser.add_argument('-C',
                                 '--config-help',
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

    def get_taxes_from_gross_income(self, gross_income, deduction=0.00, single=True, head_of_household=False):
        """
        Calculates taxes on a gross_income. Optimizes deductible based on input vs standard.
        :param gross_income: The income to calculate taxes from.
        :param deduction: A deductible to use.
        :param single: True if filing as single, False if filing as a joint married couple.
        :param head_of_household: True if filing as head of household, False if not.
        :return: The percent tax rate and total taxes [percent, taxes]
        """
        self.log("\nCalculating taxes with get_taxes_from_gross_income({0:.2f}, {1:.2f})".format(gross_income, single))
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
        gross_income -= deductible
        self.log("...Using gross taxable income as {0:.2f} with deductible of {1:.2f}".format(gross_income, deductible))

        bracket = 1
        while True:
            if gross_income > tax_bracket[bracket]:
                # Calculate the taxable income between brackets.
                taxable_income = tax_bracket[bracket] - tax_bracket[bracket - 1]
                total += tax_rate_bracket[bracket] * taxable_income
            else:
                # Calculate the taxable income left until next bracket cap.
                taxable_income = gross_income - tax_bracket[bracket - 1]
                total += tax_rate_bracket[bracket] * taxable_income

                # Print this since it will be skipped for the last one.
                taxable_income -= tax_rate_bracket[bracket]
                self.log("...bracket[{0}] = {1} -> total: {2:.2f}, temp_income: {3:.2f}".format(bracket, tax_bracket[bracket], total, taxable_income))

                break  # There's no more money to tax after this.

            taxable_income -= tax_rate_bracket[bracket]
            self.log("...bracket[{0}] = {1} -> total: {2:.2f}, temp_income: {3:.2f}".format(bracket, tax_bracket[bracket], total, taxable_income))
            bracket += 1

        percent = total / gross_income
        self.log("Finished calculation - percent: {0:.4f}, total: {1:.2f})".format(percent, total))
        return percent, total


if __name__ == '__main__':
    print("-- Starting finance calculator --")
    finance = Finance()
    finance.get_taxes_from_gross_income(107000.00, True)
