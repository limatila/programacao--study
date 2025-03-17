
def write_output_local(entry: any, and_print: bool = False, reset_output_file: bool = False):
    #If user also want to see log in console runtime
    if and_print:
        print(entry)
    
    #If user want's a clean output.txt
    if reset_output_file:
        with open('output-tests.txt', 'w') as file:
            file.write('')
            print("Output.txt file was reseted!")

    with open('output-tests.txt', 'a') as file:
        file.write(f"{str(entry)}\n")

