import os

def run():
    print("[*] In environment module.")
    return bytes(os.environ, 'utf-8')
