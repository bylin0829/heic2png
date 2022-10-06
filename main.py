import secrets
from heic2png import HEIC2PNG
import os
import glob

if __name__ == '__main__':
    src_folder = input('Source folder:')
    # src_folder = 'D:\Fork\HEIC_convertor'
    # dst_folder = os.path.join(src_folder, 'output')

    # Check folder
    if os.path.exists(src_folder) is False:
        print('Source folder does not exist.')
        raise

    # if os.path.exists(dst_folder) is False:
    #     try:
    #         os.makedirs(dst_folder, exist_ok=True)
    #     except Exception as err:
    #         print('Create destination path failure.')

    # Image process
    os.chdir(src_folder)

    for i in glob.glob('*.heic'):
        try:
            heic_img = HEIC2PNG(i)
            heic_img.save()
            print('Export: [{file}] success.'.format(file=i))
        except FileExistsError:
            print('[{file}] exist. Pass this file.'.format(file=i))
        except Exception as err:
            print('Export: [{file}] failure. Error msg: {err}'.format(
                file=i, err=err))
