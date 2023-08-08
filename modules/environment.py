import os

def run(**args):
    print("[*] In environment module.")
    return str(os.environ)


def main():
    run()
    os.environ=str(os.environ)
    print(os.environ)
main()
