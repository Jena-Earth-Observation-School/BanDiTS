#import os
import numpy as np
from GEO419_South_Africa import import_arr
from pathos import multiprocessing as mp


# def main():
#     # Input Folder Marlin:
#     input_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/Input_Files/"
#     # Input Folder Jonas:
#     # input_folder = "C:/Users/jz199/Documents/Studium/Master/1. Semester/Vorlesungsmitschriften/GEO419 - Pythonprogrammierung Habermeyer/GEO402_Testdaten/"
#
#     # Input file name
#     input_filename = "S1_A_VH_agulhas_full_study_site_50m"
#
#     # Output Folder Marlin:
#     output_folder = "C:/Users/marli/Desktop/GEO402_Testdaten/AAA_output/"
#     # Output Folder Jonas:
#     #output_folder = ""
#
#     # Output File Name:
#     output_file = "test_original_all_bands_mean1.tif"
#
#     ######################   NO USER INPUT BEYOND THIS POINT   ###############################
#
#     # example of changeble output names
#         # basename = 'out{}.tif'
#         # tuning = 3
#         # outname = os.path.join(input_folder, basename.format(tuning))
#
#     # example of new sub directory creation
#         # subdir = os.path.join(input_folder, 'sub')
#         # os.makedirs(subdir, exist_ok=True)
#
#     input_file = input_folder + input_filename
#     outname = output_folder + output_file
#
#     # arr: full size numpy array 3D XxYxZ 200x300x100
#     arr = import_arr.rio_array(input_file)
#
#     preprocessing(arr=arr)
#
#     ######## delete old array from memory to save some #######
#
#     #arr[arr == -99.        ] = np.nan ## converting -99 values to NaN values -> produces warnings, but works
#     #result = apply_along_axis.parallel_apply_along_axis(func1d=mean, arr=arr, axis=0, cores=mp.cpu_count())
#     #export_arr.out_array(outname=outname, arr=result, input_file = input_file)


def preprocessing(input_file):
    import numpy as np
    rotate_arr = import_arr.rio_array(input_file)
    rotate_arr = np.rollaxis(rotate_arr, 2)
    rotate_arr = np.rollaxis(rotate_arr, 2)
    rotate_arr = rotate_arr[1100][900]
    #print(rotate_arr)
    #print(rotate_arr.shape)
    #print(arr.shape)
    no_data = np.where(rotate_arr == -99.        )
    #print(no_data[0])
    #new_arr2 = arr
    #new_arr2 = np.delete(new_arr2, no_data[0], 0)
    arr = np.delete(arr, no_data[0], 0)
    return arr
    #print(arr.shape)



# main func
if __name__ == '__main__':
    main()