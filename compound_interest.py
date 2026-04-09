# This script calculates yearly compound interest given principal, annual rate of interest and time period in years.
# Do not use this in production. Sample purpose only.

# Author: Upkar Lidder (IBM)

# Input:
# p, principal amount
# t, time period in years
# r, annual rate of interest

# Output:
# compound interest = p * (1 + r/100)^t


def compound_interest(p: float, t: float, r: float) -> float:
    """Return the final amount after compounding."""
    return p * (pow((1 + r / 100), t))


if __name__ == "__main__":
    p = float(input("Enter the principal amount: "))
    t = float(input("Enter the time period (years): "))
    r = float(input("Enter the annual rate of interest (%): "))

    final_amount = compound_interest(p, t, r)
    interest_earned = final_amount - p

    print("Final amount: {:.2f}".format(final_amount))
    print("Interest earned: {:.2f}".format(interest_earned))
