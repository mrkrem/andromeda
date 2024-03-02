import cowsay
from colorama import Fore, Back, Style
from progress.spinner import MoonSpinner
import time


bar = MoonSpinner('Загрузка: ', max=100)
for i in range(20):
    # Do some work
    time.sleep(0.5)
    bar.next()
bar.finish()
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
cowsay.cow('Hello World')
print(cowsay.get_output_string('tux', 'Hello World'))
print(Fore.RED + '[]')
print(Fore.YELLOW + '[]')
print(Fore.GREEN + '[]')


