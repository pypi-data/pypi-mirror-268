

'''
	from biotech.topics.process_on.p_expect.parse_records import parse_p_expect_records
	parsed_records = parse_p_expect_records (
		records = [],
		format = "UTF8",
		
		remove_ASCII_escape_characters = True
	)
'''

'''
[{
	"UTF8": {
		"parsed": "yes",
		"line": UTF8_line
	},
	"hexadecimal": {
		"parsed": hexadecimal_parsed,
		"line": hexadecimal_line
	}
}]
'''

import re

def remove_escape_characters(text):
	# Define a regular expression pattern to match escape sequences
	pattern = re.compile(r'\x1b\[([0-9]{1,2}(;[0-9]{1,2})?)?[m|K]')

	# Use the pattern to replace escape sequences with an empty string
	return pattern.sub('', text)



def parse_p_expect_records (
	records = [],
	format = "UTF8",
	
	remove_ASCII_escape_characters = True
):
	parsed = []

	for record in records:
		if (remove_ASCII_escape_characters):
			the_record = remove_escape_characters (record [ format ] ["line"])
		else:
			the_record = record [ format ] ["line"]
	
		parsed.append (the_record)

	return parsed;