"""`1195. Fizz Buzz Multithreaded <https://leetcode.com/problems/fizz-buzz-multithreaded/>`_

>>> from threading import Thread

>>> answer, fb = [], FizzBuzz(15)
>>> a = Thread(target=lambda: fb.fizz(lambda: answer.append("Fizz")))
>>> b = Thread(target=lambda: fb.buzz(lambda: answer.append("Buzz")))
>>> c = Thread(target=lambda: fb.fizzbuzz(lambda: answer.append("FizzBuzz")))
>>> d = Thread(target=lambda: fb.number(lambda x: answer.append(x)))
>>> a.start();  b.start(); c.start(); d.start(); a.join(); b.join(); c.join(); d.join()
>>> answer
[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
"""

from threading import Condition
from typing import Callable


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.task = 0
        self.condition = Condition()

    def fizz(self, printFizz: Callable[[], None]):
        """Outputs 'fizz'."""
        for i in range(1, self.n + 1):
            with self.condition:
                while self.task % 4 != 0:
                    self.condition.wait()

                self.task += 1
                if i % 3 == 0 and i % 5 != 0:
                    printFizz()

                self.condition.notify_all()

    def buzz(self, printBuzz: Callable[[], None]):
        """Outputs 'buzz'"""
        for x in range(1, self.n + 1):
            with self.condition:
                while self.task % 4 != 1:
                    self.condition.wait()

                self.task += 1
                if x % 3 != 0 and x % 5 == 0:
                    printBuzz()

                self.condition.notify_all()

    def fizzbuzz(self, printFizzBuzz: Callable[[], None]):
        """Outputs 'fizzbuzz"""
        for x in range(1, self.n + 1):
            with self.condition:
                while self.task % 4 != 2:
                    self.condition.wait()

                self.task += 1
                if x % 3 == 0 and x % 5 == 0:
                    printFizzBuzz()

                self.condition.notify_all()

    def number(self, printNumber: Callable[[int], None]):
        """Outputs 'x', where x is an integer."""
        for x in range(1, self.n + 1):
            with self.condition:
                while self.task % 4 != 3:
                    self.condition.wait()

                self.task += 1
                if x % 3 != 0 and x % 5 != 0:
                    printNumber(x)

                self.condition.notify_all()
