from sys import byteorder
import binascii

def dump_pe(file_path):
    try:
        with open(file_path,'rb') as f:

            #DOS_HEADER
            dos_header = f.read(64)
            e_magic = dos_header[0:2]#マジックナンバーの確認

            e_lfanew = dos_header[60:64]
            e_lfanew = int.from_bytes(e_lfanew, 'little')

            #COFF_Headerへの移動
            f.seek(e_lfanew)

            signature = f.read(4)#マジックナンバー
            print("signature")
            print(signature.hex())   #OK

            machine = f.read(2)
            machine = int.from_bytes(machine,'little')
            print("machine")
            print(hex(machine))

            num_section = f.read(2)
            print("NumberOfSections")
            print(int.from_bytes(num_section,'little'))

            f.seek(12,1)
            size_op_header = f.read(2)
            size_op_header = int.from_bytes(size_op_header, 'little')



            #addressofentrypoint
            f.seek(18,1)
            add_entry_point = f.read(4)
            add_entry_point = int.from_bytes(add_entry_point, 'little')
            print("AddresOfEntryPoint")
            print(hex(add_entry_point))


            #section_table
            goto_sec_table = size_op_header + e_lfanew + 64

            f.seek(goto_sec_table,0)
            for n in range(int.from_bytes(num_section,'little') - 1):
                name = f.read(6)
                f.seek(2,1)
                name.decode().split('\x00')
                virtual_size = f.read(4)
                virtual_size = int.from_bytes(virtual_size, 'little')
                virtual_add = f.read(4)
                virtual_add = int.from_bytes(virtual_add, 'little')
                size_raw_data = f.read(4)
                size_raw_data = int.from_bytes(size_raw_data, 'little')
                pointer_raw = f.read(4)
                pointer_raw = int.from_bytes(pointer_raw, 'little')
                print("name::")
                print(name)
                print("virtual size")
                print(hex(virtual_size))
                print("virtual_add")
                print(hex(virtual_add))
                print("size_raw_data")
                print(hex(size_raw_data))
                print("pointer_raw")
                print(hex(pointer_raw))
                f.seek(16,1)

    except FileNotFoundError:
        print("File not found")

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == '__main__':
    file_path = input('ファイルパスを入力してください>>>')
    dump_pe(file_path)