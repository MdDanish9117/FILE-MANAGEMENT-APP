import os


def Create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"file name {filename}: created successfully!")
    except FileExistsError:
        print(f"file name {filename} already exists!")
    except Exception as E:
        print('An error occured')


def View_all_files():
    files = os.listdir()
    if not files:
        print('file  not found!')
    else:
        print('files in directory!')
        for file in files:
            print(file)


def Delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully!')
    except FileNotFoundError as e:
        print('file not found!')
    except Exception as e:
        print('An error occured!')


def Read_file(filename):
    try:
        with open('danish.txt','r') as f:
            content=f.read()
            print(f"content of '{filename}' :\n{content}")

    except FileNotFoundError:
        print(f"{filename} does not exists!")
    except Exception as e:
        print('An error occured!')

def Edit_file(filename):
    try:
        with open('danish.txt','a') as f:
            content=input('Enter data to add = ')
            f.write(content + "\n")
            print('content added to {filename} successfully!')
    except FileNotFoundError:
        print(f"{filename} doest exists!")

    except Exception as e:
        print("An error occured!") 



def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1: Create file')
        print('2: View all file')
        print('3: Delete file')
        print('4: Read file')
        print('5: Edit file')
        print('6: Exists')

        choice= input('Enter your choice(1-6) =')


        if choice=='1':
            filename=input('Enter the file-name to create =')
            Create_file(filename)

        elif choice =='2':
            View_all_files()

        elif choice=='3':
            filename=input('Enter the name of file you want to delete!')
            Delete_file(filename)
            
        elif choice=='4':
            filename=input('Enter the file name to read =')
            Read_file(filename)

        elif choice=='5':
            filename=input('Enter file name to edit =')
            Edit_file(filename)

        elif choice=='6':
            print('Thanks')
            print('Closing the app.....')
            break

        else:
            print('Invalid syntax')
if __name__=="__main__":
    main()










        
        

