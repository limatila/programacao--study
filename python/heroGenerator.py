def heroPosesCycle(characterPrefix: str = 'hero_'):
    i = 0
    while(True):
        i = 1 if i == 0 else 0
        yield f"{characterPrefix}{i}"
