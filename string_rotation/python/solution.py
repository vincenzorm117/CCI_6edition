#!/usr/local/bin/python3


def isSubstring(s1,s2):
	return s1 in s2


def string_rotation(s1,s2):
	if len(s1) != len(s2):
		return False
	return isSubstring(s2,s1+s1)


print(string_rotation(input(),input()))


