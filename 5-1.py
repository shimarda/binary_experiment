import os
import hashlib


def signatures_open(file):
    database = input("使用するデータベースのパスを入力")

    lis = os.listdir(file)

    try:

        num_data = len(open(database).readlines())

        for file_name in lis:

            file_path = file + str('/') + str(file_name)

            with open(file_path, 'rb') as f:

                with open(database, 'rb') as data:

                    for l in range(num_data-1):
                        hash_line = data.readline().rstrip(b'\r\n')
                        hash_line_str = str(hash_line, 'utf-8')
                        b_data = f.read()
                        hash_md5 = hashlib.md5(b_data).hexdigest()
                        #print(hash_md5)

                        if hash_md5 in hash_line_str:
                            print(file_name + ":Found")
                    
        
    except Exception as e:
         print(f"エラー : {e}")




if __name__ == "__main__":
    
    file = input("検索するフォルダのパスを入力")
    signatures_open(file)