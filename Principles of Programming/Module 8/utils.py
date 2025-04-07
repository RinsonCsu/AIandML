def aligned_input(text: str):
    return input(f"{text:^100}")

def aligned_print_withline(text: str):
    print()
    aligned_print(text)

def aligned_print(text: str):
    print(f"{text:^100}")
