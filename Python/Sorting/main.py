from random import randint
from timeit import repeat


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array


ARRAY_LENGTH = 10000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    run_sorting_algorithm(algorithm="bubble_sort", array=array)
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~/Algorithm_Fundamentals/Python/Sorting/main.py [+]                                                                      1,5            All
-- INSERT --
from
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~/Algorithm_Fundamentals/Python/Sorting/main.py [+]                                                                      1,5            All
-- INSERT --
vagrant@vagrant-ubuntu-trusty-64:~$ ls
Algorithm_Fundamentals  Facebook  Linear_Algebra_SMU
vagrant@vagrant-ubuntu-trusty-64:~$ cd Algorithm_Fundamentals/
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ ls
 C   PP   foobar  'Icon'$'\r'   Python   README.md   Stanford
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ nvim
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ ls
 C   CPP   foobar  'Icon'$'\r'   Python   README.md   Stanford
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ cd Python/ls
-bash: cd: Python/ls: No such file or directory
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ cd Python/
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python$ ls
BinaryGap  Functions  Gambler  Gaussian_Distribution  Harmonic  Leap_Year  Linear_Regression  main.py
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python$ cd ..
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ ls
 C   CPP   foobar  'Icon'$'\r'   Python   README.md   Stanford
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ ls
 C   CPP   foobar  'Icon'$'\r'   Python   README.md   Stanford
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ cd Python/
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python$ ls
BinaryGap  Functions  Gambler  Gaussian_Distribution  Harmonic  Leap_Year  Linear_Regression  main.py
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python$ mkdir Sorting
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python$ nvim
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python$ ls
BinaryGap  Functions  Gambler  Gaussian_Distribution  Harmonic  Leap_Year  Linear_Regression  main.py  Sorting
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python$ cd Sorting/
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$ touch main.py
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$ cd ..
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python$ cd ..
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ git init
Reinitialized existing Git repository in /home/vagrant/Algorithm_Fundamentals/.git/
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ git add .
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ git commit -m 'add sorting algorithm'
[master c3858b2] add sorting algorithm
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 Python/Sorting/main.py
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ git push
Username for 'https://github.com': davestroud
Password for 'https://davestroud@github.com':
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 374 bytes | 374.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/davestroud/Algorithm_Fundamentals.git
   72cfcc2..c3858b2  master -> master
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ ls
 C   CPP   foobar  'Icon'$'\r'   Python   README.md   Stanford
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ nvim
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ ls
 C   CPP   foobar  'Icon'$'\r'   Python   README.md   Stanford
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ git init
Reinitialized existing Git repository in /home/vagrant/Algorithm_Fundamentals/.git/
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ git add .
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ git commit -m 'add to sorting algorithm'
[master e096a40] add to sorting algorithm
 1 file changed, 20 insertions(+)
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ git push
Username for 'https://github.com': davestroud
Password for 'https://davestroud@github.com':
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 765 bytes | 765.00 KiB/s, done.
Total 5 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/davestroud/Algorithm_Fundamentals.git
   c3858b2..e096a40  master -> master
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ ls
 C   CPP   foobar  'Icon'$'\r'   Python   README.md   Stanford
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ nvim
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ nvim
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals$ cd Python/
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python$ ls
BinaryGap  Functions  Gambler  Gaussian_Distribution  Harmonic  Leap_Year  Linear_Regression  main.py  Sorting
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python$ cd Sorting/
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$ ls
main.py
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$ python main.py
  File "main.py", line 8
    setup_code = f"from __main__ import {algorithm}" \
                                                   ^
SyntaxError: invalid syntax
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$ nvim
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$ ls
main.py
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$ python main.py
  File "main.py", line 8
    setup_code = f"from __main__ import {algorithm}" \
                                                   ^
SyntaxError: invalid syntax
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$ nvim main.py
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$ python main.py
  File "main.py", line 8
    setup_code = f"from __main__ import {algorithm}"
                                                   ^
SyntaxError: invalid syntax
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$ nvim main.py
vagrant@vagrant-ubuntu-trusty-64:~/Algorithm_Fundamentals/Python/Sorting$
from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
~
main.py                                                                                                                  8,54           All
C
