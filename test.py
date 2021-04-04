import subprocess
passwd="Pling123"
out=""
stderr=subprocess.STDOUT
process=subprocess.run(["7z", "x","test.7z","-p"+passwd],capture_output=True)
print(process.returncode)
