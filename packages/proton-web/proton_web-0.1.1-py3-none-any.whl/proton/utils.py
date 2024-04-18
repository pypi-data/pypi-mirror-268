def remove_indentation(text):
    lines = text.split('\n')  # Split the text into lines
    if lines:
        first_line_indent = len(lines[1]) - len(lines[1].lstrip())  # Get the amount of indentation in the first line
        modified_lines = [line[first_line_indent:] for line in lines]  # Remove indentation from each line
        result = '\n'.join(modified_lines)  # Join the modified lines back together
        return result
    return text  # Return the original text if it's empty