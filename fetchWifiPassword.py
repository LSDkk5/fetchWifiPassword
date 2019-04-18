import subprocess


class checkPassword:
    def __init__(self):
        self.data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles',]).decode('utf-8').split('\n')
        self.data = [i.split(':')[1][1:-1] for i in self.data if 'All User Profile' in i]

        for i in self.data:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear',]).decode('utf-8').split('\n')
            results = [b.split(':')[1][1:-1] for b in results if 'Key Content' in b]
            try:
                print("{:<30}|  {:<}".format(i, results[0]))
            except IndexError:
                print("{:<30}|  {:<}".format(i, ""))
        print(f'\n[{len(results)}] passwords found!')


cp = checkPassword()
