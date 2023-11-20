import subprocess

# subprocess.run(['ls', '-al'])

# shell injection のため，推奨されていない．
# ls | rm -rf　などを入れられてしまう可能性があるため．
# subprocess.run('ls -al | grep test', shell=True)