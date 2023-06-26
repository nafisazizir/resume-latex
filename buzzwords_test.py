def find_missing_buzzwords(buzzwords_file, resume_file, output_file):
    # Read the buzzwords from the file
    with open(buzzwords_file, 'r') as buzzwords:
        buzzwords_list = [buzzword.strip() for buzzword in buzzwords.read().splitlines()]

    # Read the resume content
    with open(resume_file, 'r') as resume:
        resume_content = resume.read().lower()

    # Find missing buzzwords
    missing_buzzwords = [buzzword for buzzword in buzzwords_list if buzzword.lower() not in resume_content]
    included = [buzzword for buzzword in buzzwords_list if buzzword.lower() in resume_content]
    print(included)

    # Write missing buzzwords to the output file
    with open(output_file, 'w') as output:
        output.write('\n'.join(missing_buzzwords))

# Usage example
buzzwords_file = 'buzzwords.txt'
resume_file = 'resume_raw.txt'
output_file = 'missing_buzzwords.txt'

find_missing_buzzwords(buzzwords_file, resume_file, output_file)
print(f"Missing buzzwords have been saved in '{output_file}' file.")
