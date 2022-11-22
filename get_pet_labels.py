from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = dict()
    in_files=listdir(image_dir)
    
    for idx in range(0,len(in_files),1):
        if in_files[idx][0] !='.':
            if in_files[idx] not in results_dic:
                pet_label = in_files[idx].split('.')[0].lower().replace('_',' ')
                pet_label = ''.join([i for i in pet_label if not i.isdigit()])
                results_dic[in_files[idx]]=[pet_label]
            else:
                print("** Warning: Duplicate files exist in directory:", in_files[idx])
        print(results_dic[in_files[idx]])
    
    return results_dic
