import random

def riddle_factory(data):
    """Factory function to create stateful get_riddle and get_riddles functions."""
    cache = []
    cache_index = 0

    def get_riddle():
        nonlocal cache, cache_index
        if cache_index < len(cache):
            riddle = cache[cache_index]
            cache_index += 1
            return riddle
        else:
            question, answers = random.choice(list(data.items()))
            riddle = {'question': question, 'answer': answers[0]}
            return riddle

    def get_riddles(count=1):
        nonlocal cache, cache_index
        if count > len(data):
            raise ValueError("Requested count exceeds available number of unique riddles.")

        if cache_index + count <= len(cache):
            riddles = cache[cache_index:cache_index + count]
            cache_index += count
            return riddles
        else:
            selected_items = random.sample(list(data.items()), k=min(2 * count, len(data)))
            cache[:] = [{'question': q, 'answer': a[0]} for q, a in selected_items]
            cache_index = 0
            return get_riddles(count)

    return get_riddle, get_riddles

