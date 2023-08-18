{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "66d0d531",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, What's your name?lubna\n",
      "okay! lubna I am Guessing a number between 1 and 10:\n",
      "4\n",
      "You guessed the number in 1 tries!\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "number = random.randint(1, 10)\n",
    "\n",
    "player_name = input(\"Hello, What's your name?\")\n",
    "number_of_guesses = 0\n",
    "print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')\n",
    "\n",
    "while number_of_guesses < 5:\n",
    "    guess = int(input())\n",
    "    number_of_guesses += 1\n",
    "    if guess < number:\n",
    "        print('Your guess is too low')\n",
    "    if guess > number:\n",
    "        print('Your guess is too high')\n",
    "    if guess == number:\n",
    "        break\n",
    "if guess == number:\n",
    "    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')\n",
    "else:\n",
    "    print('You did not guess the number, The number was ' + str(number))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
