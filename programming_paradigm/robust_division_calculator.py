def safe_divide(numerator, denominator):

    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den

        return f"the result of the division is {result:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: cannot divide by zero."