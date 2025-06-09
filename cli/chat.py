def chat_loop():
    while True:
        question = input('> ')
        if question.lower() in ('exit', 'quit'): break
        print('[Placeholder] Answering...')