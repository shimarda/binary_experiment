#! /usr/bin/python3
import subprocess, re

def ana_binary(binary_file):
    
    try:
        #cmd = "objdump -d {}".format(binary_file) 
        res = subprocess.check_output(['objdump', '-d', binary_file], universal_newlines=True)
        lines = res.splitlines()

        func = []

        for line in lines:
            l = line.split('\t')

            if '<' in l[0]:
                tmp = re.findall('<.*>', l[0])
                if len(func) != 0:
                    print(f"{f}>>{func}")
                    func.clear()
                f = tmp
                
                
        
            if '<' in l[-1]:
                if len(l) != 1:
                    a = re.findall("<.*>",l[-1])
                    func.append(a)
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    binary_file = input()
    ana_binary(binary_file)