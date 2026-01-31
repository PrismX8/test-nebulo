with open('Nebulearn-School/index.html', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 854 <= i <= 930:
            print(f"{i}: {line.rstrip()}" )
