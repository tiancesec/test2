import os

def run(**args):
    print("[*] In environment module.")
    return os.environ


def main():
    run()
    os.environ=str(os.environ)
    print(os.environ)
main()

