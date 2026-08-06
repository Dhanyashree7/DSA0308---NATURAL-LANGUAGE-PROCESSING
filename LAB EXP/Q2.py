def finite_state_automaton(string):
    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    if state == 2:
        print(string, "-> Accepted (Ends with 'ab')")
    else:
        print(string, "-> Rejected")
strings = ["ab", "aab", "aaab", "abab", "abc", "baa", "cab"]

for s in strings:
    finite_state_automaton(s)
