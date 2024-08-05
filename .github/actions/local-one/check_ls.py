import argparse
import os
import sys

WALK_FILES = "files"
WALK_DIRS = "dirs"

def walking_type(file_type: bool,dir_type: bool) -> str:
    if file_type and dir_type:
        raise Exception("both are vaalid")

    if not file_type and not dir_type:
        raise Exception("both are invalid")

    if file_type:
        return WALK_FILES
    
    return WALK_DIRS

def main():
    parser = argparse.ArgumentParser(
                    prog='llist',
                    description='to list files/dir',
                    epilog='Text at the bottom of help')    

    parser.add_argument('--root-path', type=str, default=os.getcwd(),help='for root')
    parser.add_argument('--dir-pattern', type=str, default='',help='for root')
    parser.add_argument('--delim', type=str, default=',',help='for root')
    parser.add_argument('--file_exlude_regex', type=str, default='',help='for root')
    parser.add_argument('--dir_exclude_regex', type=str, default='',help='for root')
    parser.add_argument('--return-files',action='store_true',help='for root')
    parser.add_argument('--return-dirs',action='store_true',help='for root')

    args = parser.parse_args()
    print(f"args are:{args}: the end>>>>")
    if not os.path.isdir(args.root_path):
        raise Exception("not a valid root")
    
    ttype = walking_type(args.return_files, args.return_dirs)
    #print(args.accumulate(args.integers))
    #print(sys.argv)

if __name__=='__main__':
    main()