import os

def run(**args):
    print("[*] In environment module.")
    return bytes(os.environ, 'utf-8')
