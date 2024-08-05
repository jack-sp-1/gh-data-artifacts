import argparse
import os
import sys



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
    #print(args.accumulate(args.integers))
    print(sys.argv)

if __name__=='__main__':
    main()