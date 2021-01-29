import os
import sys

if __name__ == '__main__':
    if len(sys.argv)  == 4:

        parent_folder_path = sys.argv[1]
        tv_show_name = sys.argv[2]
        number_of_seasons = sys.argv[3]

        try:
            if os.path.isdir(parent_folder_path):
                tv_show_folder = os.path.join(parent_folder_path, tv_show_name)

                os.mkdir(tv_show_folder)
                os.chdir(path=tv_show_folder)

                if number_of_seasons.isnumeric():
                #Creates folders for x seasons.
                    for i in range(0, int(number_of_seasons)):
                        os.mkdir(os.path.join(os.getcwd(), f'Season { i + 1 }'))

                    with open(os.path.join(tv_show_folder, 'README.txt'), 'w') as f:
                        f.write(f'Enjoy watching {tv_show_name}!\nNote: In case you\'re still wondering, yes, you can delete this file.')
                    


        #Just in case something goes wrong.
        except FileExistsError as e: 
            print("Woah, woah, woah... You attempted to create a folder that already exists...\nBe careful next time.")

    else:
        print('WRONG USAGE!')
        print('The correct usage is: python3 autoshow.py [PARENT FOLDER PATH] [TV SHOW NAME] [NUMBER OF SEASONS].')

