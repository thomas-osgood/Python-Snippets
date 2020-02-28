#!/usr/bin/python3

import time
import interesting_number
import missing_letter
import move_zeros
import pig_latin
import valid_ip

def main():
    # Init Variables Used To Test
    letter_test = ["a", "b", "c", "e", "f"]
    zeros_test = ['a', 3, 5, 0, 1, 1, 3, 5, 0, 0, 0, 7, 9]
    interesting_test = [39, 400, 12345, 1329, 8769, 4135]
    awesome_numbers = [4135]
    latin_test = "This will become pig latin."
    latin_result = None
    ip_test = "127.0.0.1"
    ip_result = None
    res = -1
    missing = None
    zeros_end = None

    # Missing Letter Test
    print("--- Missing Letter Test ---\n")
    missing = missing_letter.find_missing_letter(letter_test)
    if (missing is None):
        print("[!] No Missing Letter Found\n")
    else:
        print("[+] {0} Is The Missing Letter In {1}\n".format(missing, letter_test))

    # Move Zeros Test
    zeros_end = move_zeros.move_zeros(zeros_test)
    print("--- Move Zeros Test ---\n\nOld: {0}\nNew: {1}\n".format(zeros_test, zeros_end))

    # Pig Latin Test
    print("--- Pig Latin Test ---\n")
    latin_result = pig_latin.pig_it(latin_test)
    print("Old: {0}\nNew: {1}\n".format(latin_test, latin_result))

    # Valid IP Test
    print("--- IP Validation Test ---\n")
    ip_result = valid_ip.is_valid_IP(ip_test)
    if (ip_result):
        print("[+] {0} Is A Valid IP Address\n".format(ip_test))
    else:
        print("[-] {0} Is Not A Valid IP Address\n".format(ip_test))

    # Interesting Number Test
    print("--- Interesting Number Test ---\n")
    print("Awesome Number List: {0}\n".format(awesome_numbers))
    for number in interesting_test:
        res = interesting_number.is_interesting(number, awesome_numbers)

        if (res == 2):
            print("[+] {0} Is An Interesting Number\n".format(number))
        elif (res == 1):
            print("[!] {0} Is Within Two Miles From An Interesting Number\n".format(number))
        else:
            print("[-] {0} Is Not An Interesting Number\n".format(number))

    return

if __name__ == "__main__":
    s = time.time()
    main()
    e = time.time()
    exec_time = e - s
    print("\n[INFO] Program Took {0} Seconds To Execute ...\n".format(exec_time))
