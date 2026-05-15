def gen_parentheses(pairs):
    if not isinstance(pairs, int):
        return 'The number of pairs should be an integer'
    if pairs < 1:
        return 'The number of pairs should be at least 1'
    
    queue = [('', 0, 0)]
    result = []
    while queue:
        #print(f'{queue}')
        current, opens_used, closes_used = queue.pop(0)
        if len(current) == 2 * pairs:
            result.append(current)
            print(f'the current is {current} and len({len(current)}), added to result\t{result}'.expandtabs(30))
        else:
            if opens_used < pairs:
                queue.append((current + '(', opens_used + 1, closes_used))
                print(f"{(current + '(', opens_used + 1, closes_used)}\topen parenthesis added to queue")
            if closes_used < opens_used:
                queue.append((current + ')', opens_used, closes_used + 1))
                print(f"{(current + ')', opens_used, closes_used + 1)}\tclose parenthesis added to queue")

    return (result, f"the total combinations is {len(result)}")
print(gen_parentheses(30))