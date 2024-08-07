import argparse
import os
import sys
import re

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

def walk_from_root(root_path, dir_pattern, file_exclude_regex, dir_exclude_regex, ttype) ->list:

    finale=[]
    if not os.path.exists(root_path):
        raise Exception("invalid path of root")

    for (root,dirs,files) in os.walk(root_path):

        print(f"root is:{root}")
        
        rel_dir_from_root = os.path.relpath(root,root_path)

        if dir_exclude_regex=='' and re.search(dir_exclude_regex,rel_dir_from_root):
            print("not required")
            continue
            
        print(f"checking path :{rel_dir_from_root}")

        if re.search(dir_pattern, rel_dir_from_root):
            if ttype == WALK_DIRS:
                finale.append(rel_dir_from_root)

            else:
                for filename in files:
                    if not re.search(file_exclude_regex, filename):
                        finale.append(os.path.join(rel_dir_from_root,filename))
    return finale


        
        


        

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

    data = walk_from_root(args.root_path, args.dir_pattern,  args.file_exclude_regex, args.dir_exclude_regex, ttype)
    #print(args.accumulate(args.integers))
    #print(sys.argv)

if __name__=='__main__':
    main()