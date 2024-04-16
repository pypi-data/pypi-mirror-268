# stringutils.py

def reverse_string(string):
    """
    문자열을 뒤집어 반환합니다.
    """
    return string[::-1]

def is_palindrome(string):
    """
    주어진 문자열이 팰린드롬인지 확인합니다.
    """
    string = string.lower().replace(" ", "")
    return string == string[::-1]

def count_vowels(string):
    """
    문자열에 포함된 모음의 개수를 세어 반환합니다.
    """
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

def capitalize_first_letter(string):
    """
    문자열의 첫 글자를 대문자로 변환합니다.
    """
    return string.capitalize()

def count_occurrences(string, substring):
    """
    문자열에서 특정 부분 문자열의 출현 횟수를 세어 반환합니다.
    """
    return string.count(substring)

def remove_duplicates(string):
    """
    문자열에서 중복된 문자를 제거하고 유일한 문자로 이루어진 문자열을 반환합니다.
    """
    return ''.join(set(string))

def is_anagram(string1, string2):
    """
    두 문자열이 아나그램인지 확인합니다.
    """
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")
    return sorted(string1) == sorted(string2)

def longest_common_prefix(strings):
    """
    여러 문자열에서 가장 긴 공통 접두사를 찾아 반환합니다.
    """
    if not strings:
        return ""
    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

def is_valid_parentheses(string):
    """
    주어진 문자열의 괄호가 유효한지 확인합니다.
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in string:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        elif char in mapping.values():
            stack.append(char)
    return not stack

def longest_palindromic_substring(string):
    """
    문자열에서 가장 긴 팰린드롬 부분 문자열을 찾아 반환합니다.
    """
    if not string:
        return ""
    longest = string[0]
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if len(substring) > len(longest) and is_palindrome(substring):
                longest = substring
    return longest