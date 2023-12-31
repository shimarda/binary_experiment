#! /usr/bin/python3
import subprocess

def code_info(binary_file):

    try:
            res = subprocess.check_output(['objdump','-d', binary_file], universal_newlines=True)
            
            lines = res.splitlines()

            for line in lines:
                 ll = line.split('\t')

                 if len(ll) > 2:
                      instruction = ll[2]
                      lis = instruction.split()
                      if len(lis) > 1:
                           cpu = lis[1].split(',')
                           count=0
                           for c in cpu:
                                if '%' in c:
                                     count +=1
                           print(f"{lis[0]},{count}")
                      else:
                           print(f"{lis[0]}, 0")
                     
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    binary_file = input("ファイルのパスを入力して下さい")
    code_info(binary_file)