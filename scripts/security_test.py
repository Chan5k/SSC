import subprocess

def test_security():
    print("Running security test...")
    cmd = "sudo openvas-scanner"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
