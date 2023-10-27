{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "33f25830",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#1. Define a function named is_two\n",
    "\n",
    "def is_two(x):\n",
    "    if x == 2 or x == \"2\":\n",
    "        return True\n",
    "    else: \n",
    "        return False\n",
    "    \n",
    "is_two(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5de4be95",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0239fad4",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2. Define a function is_vowel\n",
    "\n",
    "def is_vowel(vowel):\n",
    "    vowels = \"aeiouAEIOU\"\n",
    "    if vowel in vowels:\n",
    "        return True\n",
    "    else:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ca7fe00d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def is_vowel(vowel):\n",
    "    vowels = \"aeiou\" or \"aeiuo\".upper()\n",
    "    if vowel in vowels:\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "\n",
    "is_vowel(\"A\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25f0ffa3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "f2d2446e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Vowel'"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#. Define function named is_consonant\n",
    "\n",
    "def is_consonant(consonant):\n",
    "    vowels = \"aeiouAEIOU\"\n",
    "    if consonant in vowels:\n",
    "        return \"Vowel\"\n",
    "    else:\n",
    "        return \"Consanant\"\n",
    "        print(\"Consonant\")\n",
    "    \n",
    "is_consonant(\"a\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bf44626",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "86c43974",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n"
     ]
    }
   ],
   "source": [
    "def cap_if_consonant(x):\n",
    "    vowels = 'aeiouAEIUO'   #Setting the standard\n",
    "    for element in vowels:  #Setting the variable involved in the 'if' condition\n",
    "        if x[0] not in vowels: #Setting the condition of the 'if' condition\n",
    "             return x[0].capitalize()  #Return the outcome of the 'if' condition\n",
    "        else:\n",
    "            return x\n",
    "    \n",
    "    \n",
    "print(cap_if_consonant(\"apple\"))    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "596e5d82",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0f5fb44",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Define functoin which should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.\n",
    "\n",
    "def calculate_tip(x, y):\n",
    "    bill_total = x\n",
    "    tip_percentage = y\n",
    "    tip = bill_total * tip_percentage\n",
    "    return (f\"${tip}\")\n",
    "\n",
    "#print(calculate_tip(20, 0.10))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb1c6327",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54787b7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Define function named apply discount\n",
    "\n",
    "def apply_discount(x, y):\n",
    "    original_price = x\n",
    "    discount_percentage = y\n",
    "    total = original_price - (original_price * discount_percentage)\n",
    "    return (f\"${total}\")\n",
    "\n",
    "#print(apply_discount(40, 0.25))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a40b296d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f588e4d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Define a function named handle_commas\n",
    "\n",
    "def handle_commas(x):\n",
    "    no_commas = int(x.replace(\",\" , \"\"))  \n",
    "    return no_commas  \n",
    "\n",
    "#print(handle_commas('4,000,025'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7603614b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8492b4ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "82 is a B\n"
     ]
    }
   ],
   "source": [
    "#Define a function called letter_grade\n",
    "\n",
    "def get_letter_grade(grade):\n",
    "    if grade >= 100:\n",
    "        print('Please enter a grade between 0-100')\n",
    "    elif grade >= 90 :\n",
    "        print(f'{grade} is an A')\n",
    "    elif grade >= 80:\n",
    "        print(f'{grade} is a B')\n",
    "    elif grade >= 70:\n",
    "        print(f'{grade} is a C')\n",
    "    elif grade >= 60:\n",
    "        print(f'{grade} is a D')\n",
    "    elif grade <= 59 and grade >=0:\n",
    "        print(f'{grade} is an F')\n",
    "    else: \n",
    "        print('No negative numbers')\n",
    "        \n",
    "get_letter_grade(82)       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f60ff3ff",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c93997d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Define a function called remove_vowels\n",
    "\n",
    "def remove_vowels(string):\n",
    "    vowels = ('a', 'e', 'i', 'o', 'u')\n",
    "    for x in string.lower():\n",
    "        if x in vowels:\n",
    "            string = string.replace(x,\"\")\n",
    "    return string\n",
    "\n",
    "#print(remove_vowels(\"Archer is the greatest spy\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8abbe254",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "534ecfd0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "me+you is NOT a valid identifier\n",
      "\n",
      "john_wick is a valid identifier\n",
      "john_wick\n"
     ]
    }
   ],
   "source": [
    "#Define function named normalize_name. It should accept a string and return a valid python identifier, that is:\n",
    "#anything that is not a valid python identifier should be removed\n",
    "#leading and trailing whitespace should be removed\n",
    "#everything should be lowercase\n",
    "#spaces should be replaced with underscores\n",
    "\n",
    "#for example:\n",
    "#Name will become name\n",
    "#First Name will become first_name\n",
    "#Completed will become completed\n",
    "\n",
    "def normalize_name(text):\n",
    "    new_string = (text.strip(\"0123456789 \").lower().replace(\" \", \"_\"))\n",
    "    output = \"\"\n",
    "    if new_string.isidentifier() == True:\n",
    "        print(new_string, 'is a valid identifier')\n",
    "        for i in new_string:\n",
    "            if i not in \"!@#$%^&*()+=-[]{}\\/|?.<>,`~\":\n",
    "                output += i\n",
    "    else: \n",
    "        print(new_string, 'is NOT a valid identifier')\n",
    "    return print(output)\n",
    "\n",
    "normalize_name(\"me+you\")\n",
    "normalize_name(\" John Wick \") "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "337e8544",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9eb66373",
   "metadata": {},
   "outputs": [],
   "source": [
    "#11 Write a function named cumulative_sum\n",
    "\n",
    "list=[10,20,30,40,50]\n",
    "new_list=[] \n",
    "j=0\n",
    "for i in range(0,len(list)):\n",
    "    j+=list[i]\n",
    "    new_list.append(j) \n",
    "     \n",
    "print(new_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0572a232",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "28207a8a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[10, 30, 60, 100, 150]\n"
     ]
    }
   ],
   "source": [
    "# Problem 11 using numpy\n",
    "import numpy as np\n",
    " \n",
    "def cumulative_sum(input_list):\n",
    "    # Convert the list to a NumPy array\n",
    "    input_array = np.array(input_list)\n",
    "    # Compute the cumulative sum along the first axis of the array\n",
    "    cumulative_sum_array = np.cumsum(input_array)\n",
    "    # Convert the NumPy array back to a list and return it\n",
    "    return cumulative_sum_array.tolist()\n",
    " \n",
    "#input_list = [10, 20, 30, 40, 50]\n",
    "print(output_list)\n",
    "output_list = cumulative_sum([10,20,30,40,50])\n",
    "#print(output_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6707118",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "4b88328e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "14:35\n"
     ]
    }
   ],
   "source": [
    "#Bonus\n",
    "\n",
    "from datetime import datetime\n",
    "\n",
    "m1 = '2:35 PM'\n",
    "m1 = datetime.strptime(m1, '%I:%M %p')\n",
    "out_time = datetime.strftime(m1, \"%H:%M\")  #if commented out will return daya nd month as well\n",
    "#print(m1)\n",
    "print(out_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4758bb4f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b61db69",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73156626",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab69381c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5261cfa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11289e9c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77f39988",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35337970",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
