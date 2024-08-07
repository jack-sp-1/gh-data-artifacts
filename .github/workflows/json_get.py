import json
import sys

def main():
    print("json script has started") 
    input_path = sys.argv[1]
    add_include = sys.argv[2]
    add_filter = sys.argv[3]
    print(f"values given are: {input_path} and {add_include} and {add_filter}")
    with (input_path) as f:
        abc = json.load(f)
        print(abc)

        if add_filter=='' and add_include=='':
            with open(os.environ['GITHUB_OUTPUT'],'a') as output_file:
                print(f'matrix={abc}',file=output_file)

main()