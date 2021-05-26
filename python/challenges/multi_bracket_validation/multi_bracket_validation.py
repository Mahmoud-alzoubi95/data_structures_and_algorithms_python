def multi_bracket_validation(input):
    """unction should take a string as its only argument, and should return a 
        boolean representing whether or not the 
         brackets in the string are balanced."""
    
    curly_open = input.count('{')
    curly_close = input.count('}')
    round_open = input.count('(')
    round_close = input.count(')')
    sqr_open = input.count('[')
    sqr_close = input.count(']')
    open_list = [curly_open,round_open,sqr_open]
    close_list = [curly_close,round_close,sqr_close]
    merged_list = zip(open_list,close_list)

    if (curly_open == curly_close) and (round_open == round_close) and (sqr_open == sqr_close):
        return True
    else:
        count = 0
        for i,j in merged_list:
            if count == 0:
                if i < j:
                    return "error unmatched opening { remaining."
                elif j < i:
                    return "error closing }"
            elif count == 1:
                if i < j:
                    return "error unmatched opening ( remaining."
                elif j < i:
                    return "error closing )"
            elif count == 2:
                if i < j:
                    return "error unmatched opening [ remaining."
                elif j < i:
                    return "error closing ]"

            count+=1


if __name__ == "__main__":
    call = multi_bracket_validation("(")
    print(call)
