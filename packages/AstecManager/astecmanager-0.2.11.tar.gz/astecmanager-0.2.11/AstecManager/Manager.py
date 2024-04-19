from datetime import datetime
import os, sys
from threading import Thread
from dataclasses import dataclass
from collections import defaultdict
import time
import copy
import traceback
import AstecManager.omerotools as omerolib
from multiprocessing import cpu_count
import numpy as np
from AstecManager.libs.analyze import apply_analysis,plotsignaltonoise,plotsignaltonoise_tofolder
from AstecManager.libs.data import imread
from AstecManager.libs.jsonlib import addDictToMetadata,printMetadata
from AstecManager.libs.lineage_distance import generate_lineage_comparison
import subprocess
from AstecManager.libs.contourlib import compute_contour
import xml.etree.ElementTree as ET
xml_metadata = "metadata.xml"


def compute_atlas():
    """ """
    from importlib_resources import files
    path = []
    path.append(str(files("AstecManager.atlas").joinpath("pm1.xml")))
    path.append(str(files("AstecManager.atlas").joinpath("pm3.xml")))
    path.append(str(files("AstecManager.atlas").joinpath("pm4.xml")))
    path.append(str(files("AstecManager.atlas").joinpath("pm5.xml")))
    path.append(str(files("AstecManager.atlas").joinpath("pm7.xml")))
    path.append(str(files("AstecManager.atlas").joinpath("pm8.xml")))
    path.append(str(files("AstecManager.atlas").joinpath("pm9.xml")))
    return path

def get_omero_config(parameters):
    """Search for omero_config_file in parameters, format it and return it. 2 keys are possible "omero_config_file" or "omero_authentication_file"

    :param parameters: list of parameters given to the AstecManager step
    :type parameters: dict

    
    """
    omero_config_file = None
    if "omero_config_file" in parameters:
        if parameters["omero_config_file"] is not None and parameters["omero_config_file"] != "None":
            omero_config_file = parameters["omero_config_file"].replace('"', '').replace("'", "")
        if omero_config_file is not None and not os.path.isfile(omero_config_file):
            return None
    else:
        if "omero_authentication_file" in parameters:
            if parameters["omero_authentication_file"] is not None and parameters["omero_authentication_file"] != "None":
                omero_config_file = parameters["omero_authentication_file"].replace('"', '').replace("'", "")
            if omero_config_file is not None and not os.path.isfile(omero_config_file):
                return None
    return omero_config_file

def Fiji_autocontrast(path_in):
    """

    :param path_in: 

    """
    import cv2
    import numpy as np
    im = cv2.imread(path_in, -1)
    im_type = im.dtype
    # minimum and maximum of image
    im_min = np.min(im)
    im_max = np.max(im)

    # converting image =================================================================================================

    # case of color image : contrast is computed on image cast to grayscale
    if len(im.shape) == 3 and im.shape[2] == 3:
        # depending on the options you chose in ImageJ, conversion can be done either in a weighted or unweighted way
        # go to Edit > Options > Conversion to verify if the "Weighted RGB conversion" box is checked.
        # if it's not checked, use this line
        # im = np.mean(im, axis = -1)
        # instead of the following
        im = 0.3 * im[:, :, 2] + 0.59 * im[:, :, 1] + 0.11 * im[:, :, 0]
        im = im.astype(im_type)

    # histogram computation =============================================================================================

    # parameters of histogram computation depend on image dtype.
    # following https://imagej.nih.gov/ij/developer/macro/functions.html#getStatistics
    # 'The histogram is returned as a 256 element array. For 8-bit and RGB images, the histogram bin width is one.
    # for 16-bit and 32-bit images, the bin width is (max-min)/256.'
    if im_type == np.uint8:
        hist_min = 0
        hist_max = 256
    elif im_type in (np.uint16, np.int32):
        hist_min = im_min
        hist_max = im_max
    else:
        raise NotImplementedError(f"Not implemented for dtype {im_type}")

    # compute histogram
    histogram = np.histogram(im, bins=256, range=(hist_min, hist_max))[0]
    bin_size = (hist_max - hist_min) / 256

    # compute output min and max bins =================================================================================

    # various algorithm parameters
    h, w = im.shape[:2]
    pixel_count = h * w
    # the following values are taken directly from the ImageJ file.
    limit = pixel_count / 10
    const_auto_threshold = 5000
    auto_threshold = 0

    auto_threshold = const_auto_threshold if auto_threshold <= 10 else auto_threshold / 2
    threshold = int(pixel_count / auto_threshold)

    # setting the output min bin
    i = -1
    found = False
    # going through all bins of the histogram in increasing order until you reach one where the count if more than
    # pixel_count/auto_threshold
    while not found and i <= 255:
        i += 1
        count = histogram[i]
        if count > limit:
            count = 0
        found = count > threshold
    hmin = i
    found = False

    # setting the output max bin : same thing but starting from the highest bin.
    i = 256
    while not found and i > 0:
        i -= 1
        count = histogram[i]
        if count > limit:
            count = 0
        found = count > threshold
    hmax = i

    # compute output min and max pixel values from output min and max bins ===============================================
    if hmax >= hmin:
        min_ = hist_min + hmin * bin_size
        max_ = hist_min + hmax * bin_size
        # bad case number one, just return the min and max of the histogram
        if min_ == max_:
            min_ = hist_min
            max_ = hist_max
    # bad case number two, same
    else:
        min_ = hist_min
        max_ = hist_max

    # apply the contrast ================================================================================================
    imr = (im - min_) / (max_ - min_) * 255
    cv2.imwrite(path_in, imr)
def compute_images_from_movie(image, embryo_name):
    """

    :param image: 
    :param embryo_name: 

    """
    from PIL import Image
    from os.path import join
    print("-> Reading image")
    image_movie = imread(image)

    shape = image_movie.shape
    z_stack_count = shape[2]
    img_array = []
    for i in range(0, z_stack_count):
        img_array.append(image_movie[:, :, i])
    shape = image_movie[:, :, i].shape
    image_list = []
    image_folder = "./images/"
    if not os.path.isdir(image_folder):
        os.makedirs(image_folder)
    print("-> Writing video file")
    for i in range(len(img_array)):
        print("Frame : " + str(i))
        PIL_image = Image.fromarray(img_array[i])
        image_link = join(image_folder, 'frame' + str(i) + '.png')
        image_list.append(image_link)
        PIL_image.save(image_link)
        Fiji_autocontrast(image_link)
        height, width = img_array[i].shape
    return image_list, height, width

def compute_video_from_movie(embryo_name, intrareg_folder, fuse_folder):
    """

    :param embryo_name: 
    :param intrareg_folder: 
    :param fuse_folder: 

    """
    import cv2
    print("Creating video")
    from os.path import join, isfile
    from os import listdir
    path = "."
    fuse_exp = fuse_folder
    if isinstance(fuse_folder,list):
        fuse_exp = fuse_folder[0]
    else :
        if "[" in fuse_folder:
            fuse_exp = fuse_folder.replace("'", "").replace('"', '').replace("[", "").replace("]", "").split(
                ",")[0]
    path_intrareg = join(join(path, "INTRAREG"), "INTRAREG_" + str(intrareg_folder) + "/MOVIES/")
    path_fuse = join(path_intrareg, join("FUSE", "FUSE_" + str(fuse_exp))).replace('"', '').replace("'", "")
    final_path = join(join(path, "analysis").replace("'", "").replace('"', ''), "fusion")
    if not os.path.exists(final_path):
        os.makedirs(final_path)
    image_files = [f for f in listdir(path_fuse) if isfile(join(path_fuse, f)) and (".nii" in f or ".mha" in f)]
    image_list, height, width = compute_images_from_movie(os.path.join(path_fuse, image_files[0]), embryo_name)
    ouputname = join(final_path, 'fusion_movie.avi')
    framerate = int(len(image_list) / 15)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter(ouputname, fourcc, framerate, (width, height))
    if not video.isOpened():
        print('Error cannot create ' + 'fusion_movie.avi')
        quit()

    for image in image_list:
        img = cv2.imread(image)
        video.write(img)
        os.system("rm " + str(image))
    cv2.destroyAllWindows()
    video.release()
    os.system('ffmpeg -i ' + ouputname + '  ' + ouputname.replace('.avi', '.mp4'))
    os.system('rm -f ' + ouputname)
    return final_path

def plot_fusion_intensity_profile(embryo_name,fuse_exp="01"):
    """

    :param embryo_name: 
    :param fuse_exp:  (Default value = "01")

    """
    import matplotlib.pyplot as plt
    fuse_files = []
    fuse_folder ="./FUSE/FUSE_"+fuse_exp
    if isinstance(fuse_folder,list):
        fuse_folder = "./FUSE/FUSE_"+fuse_exp[0]
    else :
        if "[" in fuse_exp:
            fuse_folder = "./FUSE/FUSE_"+fuse_exp.replace("'", "").replace('"', '').replace("[", "").replace("]", "").split(
                ",")[0]
    for file in os.listdir(fuse_folder):
        # check only text files
        if "_fuse" in file:
            fuse_files.append(file)
    means_by_t = {}
    std_by_t = {}
    neg_std_by_t = {}

    means_by_t_b = {}
    std_by_t_b = {}
    neg_std_by_t_b = {}
    print("=> Analyzing images")
    for fuse_file in fuse_files:
        print("     -> " + str(fuse_file))
        time = int(fuse_file.split("_fuse_t")[1].split(".")[0])
        print("Time : " + str(time))
        image_path = os.path.join(fuse_folder, fuse_file)
        npimage = imread(image_path)
        mean_intensities = np.mean(npimage)
        std_intensities = np.std(npimage)
        means_by_t[time] = mean_intensities
        std_by_t[time] = std_intensities + mean_intensities
        neg_std_by_t[time] = mean_intensities - std_intensities
        min_im = np.min(npimage)
        nobackground = npimage[npimage != min_im]
        mean_intensities = np.mean(nobackground)
        std_intensities = np.std(nobackground)
        means_by_t_b[time] = mean_intensities
        std_by_t_b[time] = std_intensities + mean_intensities
        neg_std_by_t_b[time] = mean_intensities - std_intensities

    print("=> Saving result plot")
    sorted_means = dict(sorted(means_by_t.items()))
    sorted_std = dict(sorted(std_by_t.items()))
    sorted_neg_std = dict(sorted(neg_std_by_t.items()))
    sorted_means_b = dict(sorted(means_by_t_b.items()))
    sorted_std_b = dict(sorted(std_by_t_b.items()))
    sorted_neg_std_b = dict(sorted(neg_std_by_t_b.items()))
    plt.title("$\mu$ and $\pm \sigma$ in fused images for embryo " + str(embryo_name))
    times = sorted_means.keys()
    plt.plot(times, list(sorted_means.values()), label="intensities with background")
    plt.plot(times, list(sorted_means_b.values()), label="intensities without background")
    plt.fill_between(times, list(sorted_std.values()), list(sorted_neg_std.values()), alpha=0.5)
    plt.fill_between(times, list(sorted_std_b.values()), list(sorted_neg_std_b.values()), alpha=0.5)
    plt.legend(loc="upper left")
    plt.xlabel("Time points sequence")
    plt.ylabel("Intensities")

    path = "."
    folder_out = os.path.join(os.path.join(path,"analysis"), "fusion")
    if not os.path.isdir(folder_out):
        os.makedirs(folder_out)
    plt.savefig(os.path.join(folder_out, "fusion_images_intensities.png"))
def compute_user(parameters):
    """

    :param parameters: 

    """
    user = "KB"
    if "user" in parameters:
        user = parameters["user"]
    return user



def compute_astec_command(astec_command):
    """

    :param astec_command: 

    """
    final_command_arg0 = ""
    if "fuse" in astec_command.lower():
        final_command_arg0 = "astec_fusion"
    if "mars" in astec_command.lower():
        final_command_arg0 = "astec_mars"
    if "seg" in astec_command.lower() or astec_command.lower() == "astec_astec":
        final_command_arg0 = "astec_astec"
    if "post" in astec_command.lower():
        final_command_arg0 = "astec_postcorrection"
    if "properties" in astec_command.lower():
        final_command_arg0 = "astec_embryoproperties"
    if "intra" in astec_command.lower():
        final_command_arg0 = "astec_intraregistration"
    return final_command_arg0



def compute_astec_dir(astec_command, params_dict):
    """

    :param astec_command: 
    :param params_dict: 

    """
    dir_to_create = []
    if "fuse" in astec_command.lower():
        if "EXP_FUSE" in params_dict:
            if isinstance(params_dict["EXP_FUSE"], list):
                splitted_fuse = params_dict["EXP_FUSE"]
            else:
                splitted_fuse = params_dict["EXP_FUSE"].replace("'", "").replace('"', '').replace("[", "").replace("]", "").split(",")
            for fuse in splitted_fuse:
                dir_to_create.append("FUSE/FUSE_" + fuse)
        else:
            dir_to_create.append("FUSE/FUSE_RELEASE")
    if "mars" in astec_command.lower():
        if "EXP_SEG" in params_dict:
            dir_to_create.append("SEG/SEG_" + params_dict["EXP_SEG"].replace("'", "").replace('"',''))
        else:
            dir_to_create.append("SEG/SEG_RELEASE")
    if "seg" in astec_command.lower() or astec_command.lower() == "astec_astec":
        if "EXP_SEG" in params_dict:
            dir_to_create.append("SEG/SEG_" + params_dict["EXP_SEG"].replace("'", "").replace('"',''))
        else:
            dir_to_create.append("SEG/SEG_RELEASE")
    if "post" in astec_command.lower():
        if "EXP_POST" in params_dict:
            dir_to_create.append("POST/POST_" + params_dict["EXP_POST"].replace("'", "").replace('"',''))
        else:
            dir_to_create.append("POST/POST_RELEASE")
    if "properties" in astec_command.lower():
        if "EXP_INTRAREG" in params_dict:
            dir_to_create.append("INTRAREG/INTRAREG_" + params_dict["EXP_INTRAREG"].replace("'", "").replace('"',''))
        else:
            dir_to_create = "INTRAREG/INTRAREG_RELEASE"
    if "intra" in astec_command.lower():
        if "EXP_INTRAREG" in params_dict:
            dir_to_create.append("INTRAREG/INTRAREG_" + params_dict["EXP_INTRAREG"].replace("'", "").replace('"',''))
        else:
            dir_to_create.append("INTRAREG/INTRAREG_RELEASE")
    return dir_to_create


def compute_astec_tag(astec_command):
    """

    :param astec_command: 

    """
    tag = ""
    if "fuse" in astec_command.lower():
        tag = "fuse"
    elif "mars" in astec_command.lower() or "seg" in astec_command.lower() or astec_command.lower() == "astec_astec":
        tag = "seg"
    elif "post" in astec_command.lower():
        tag = "post"
    elif "intra" in astec_command.lower():
        tag = "intrareg"
    elif "properties" in astec_command.lower():
        tag = "embryoproperties"
    return tag



def is_file_image(file):
    """

    :param file: 

    """
    return file.endswith('.mha') or file.endswith('nii') or file.endswith(".inr")


def is_file_image_or_compressed(file):
    """

    :param file: 

    """
    return file.endswith('.mha') or file.endswith('nii') or file.endswith('.mha.gz') or file.endswith(
        'nii.gz') or file.endswith(".inr") or file.endswith(".inr.gz")


@dataclass
class astec_instance:
    """ """
    astec_command: str
    folder_embryo: str
    embryo_name: str
    mars_path: str = None
    compress_result: bool = True
    params_dict: dict = defaultdict
    begin_time: int = -1
    end_time: int = -1
    omero_result: bool = True
    omero_config_file: str = ""
    tag_list: list = None
    keep_temp: bool = False
    envastec: str = "astec-dev"
    paramsuffix: str = ""
    omero_input: bool = False
    input_project: str = ""
    input_set: str = ""



class start_astec_cleaner(Thread):
    """ """
    def __init__(self, astec_command, params_dict, name_embryo, send_to_omero, begin, end, compress_result=True,
                 omero_config_file="", tag_list=None, keep_temp=False):
        Thread.__init__(self)
        self.cleaner_folder = ""
        self.astec_command = astec_command
        self.name_embryo = name_embryo
        self.params_dict = params_dict
        self.stop_signal = False
        self.omero_result = send_to_omero
        self.compress_result = compress_result
        self.omero_files = []
        self.omero_files_reconstruction = []
        self.omero_config_file = omero_config_file
        self.omero_project_name = ""
        self.omero_dataset_name = []
        self.dataset_ids = []
        self.begin = int(begin)
        self.end = int(end)
        self.project_id = -1
        self.tag_list = tag_list
        self.keep_temp = keep_temp

    def stop_cleaning(self):
        """ """
        self.stop_signal = True

    def list_images(self, folder):
        """

        :param folder: 

        """
        images = []
        onlyfiles = [f for f in os.listdir(folder) if
                     os.path.isfile(os.path.join(folder, f))]
        for file in onlyfiles:
            if is_file_image(file):
                images.append(file)
        return images

    def get_images_at_t(self, time, folder):
        """

        :param time: 
        :param folder: 

        """
        images = self.list_images(folder)
        result = []
        for image in images:
            if "_t{:03d}".format(time) in image:
                result.append(image)
        return result

    def image_t_exists(self, time, folder):
        """

        :param time: 
        :param folder: 

        """
        images = self.list_images(folder)
        flag = False
        for image in images:
            if "_t{:03d}".format(time) in image:
                flag = True
        return flag

    def compress_and_delete(self, file):
        """

        :param file: 

        """
        subprocess.run(["gzip", "-f", file])
        subprocess.run(["rm", file])
    def copy_mha_to_nii(self,imagepath):
        """

        :param imagepath: 

        """
        new_path = imagepath.replace(".mha", ".nii")
        os.system("conda run -n astec copy " + imagepath + " " + new_path)
        if os.path.isfile(new_path):
            os.system("rm " + imagepath)
            return new_path
        return None
    def clean_at_t(self, time, pyom):
        """

        :param time: 
        :param pyom: 

        """

        print("Cleaning embryo : " + str(self.name_embryo) + " at t = " + str(time))
        print("finding "+str(len(self.cleaner_folder))+" folder to clean at t = " + str(time))
        for i  in range(0,len(self.cleaner_folder)):
            if not i in self.omero_files:
                self.omero_files.insert(i,[])
            list_images = pyom.get_images_filename(self.dataset_ids[i])
            for image_name in list_images:
                if not image_name in self.omero_files[i]:
                    self.omero_files[i].append(image_name)
            clean = self.cleaner_folder[i]
            print("Cleaning folder : " + clean)
            images = self.get_images_at_t(time, clean)
            for image in images:
                if image is not None and is_file_image(image):
                    imagepath = os.path.join(clean, image)
                    if imagepath.endswith(".mha"):
                        new_path = self.copy_mha_to_nii(imagepath)
                        if new_path is not None:
                            imagepath = new_path
                    if self.omero_result:
                        if not image in self.omero_files[i]:
                            print("Uploading image : " + str(imagepath)+ " to dataset with id : "+str(self.dataset_ids[i]))
                            pyom.add_image_to_dataset_java(imagepath, self.dataset_ids[i])
                            self.omero_files[i].append(image)
                            if self.compress_result:
                                print("Compressing image : " + str(imagepath))
                                self.compress_and_delete(str(imagepath))
                    elif self.compress_result:
                        print("Compressing image : " + str(imagepath))
                        self.compress_and_delete(imagepath)

        for recon in self.reconstructions_folder:
            print("Reconstruction : " + str(recon))
            if os.path.isdir(recon):
                images_reconstruction = self.get_images_at_t(time, recon)
                for image_reconstruction in images_reconstruction:
                    if image_reconstruction is not None:
                        recon_path = os.path.join(recon, image_reconstruction)
                        if self.omero_result and "REC-MEMBRANE" in recon:
                            if self.reco_dataset_id is not None:
                                if not image_reconstruction in self.omero_files_reconstruction:
                                    if image_reconstruction.endswith(".mha"):
                                        new_path = self.copy_mha_to_nii(recon_path)
                                        if new_path is not None:
                                            recon_path = new_path
                                    print("Uploading image : " + str(recon_path))
                                    pyom.add_image_to_dataset_java(recon_path, self.reco_dataset_id)
                                    self.omero_files_reconstruction.append(image_reconstruction)
                        if is_file_image(recon_path) and not ".gz" in images_reconstruction:
                            print("Compressing reconstruction : " + str(recon_path))
                            self.compress_and_delete(recon_path)
        if self.keep_temp:
            print("temp")
            for clean in self.cleaner_folder:
                temp_folder = clean + "/TEMP_{:03d}/".format(time)
                if os.path.isdir(temp_folder):
                    images = []
                    onlyfiles = [f for f in os.listdir(temp_folder) if
                                 os.path.isfile(os.path.join(temp_folder, f))]
                    print("Compressing TEMP : " + "/TEMP_{:03d}/".format(time))
                    for file2 in onlyfiles:
                        self.compress_and_delete(os.path.join(temp_folder, file2))

    def compute_recon_dir(self, params_dict):
        """

        :param params_dict: 

        """
        reconstruction_dir = []
        for dir in self.cleaner_folder:
            reconstruction_dir.append(dir + "/RECONSTRUCTION/")
        if "EXP_RECONSTRUCTION" in params_dict:
            reconstruction_dir.append("REC-MEMBRANE/REC_" + params_dict["EXP_RECONSTRUCTION"].replace('"', '').replace("'", ""))
            reconstruction_dir.append("REC-SEED/REC_" + params_dict["EXP_RECONSTRUCTION"].replace('"','').replace("'", ""))
            reconstruction_dir.append("REC-MORPHOSNAKE/REC_" + params_dict["EXP_RECONSTRUCTION"].replace('"','').replace("'", ""))
        else:
            if "EXP_SEG" in params_dict:
                reconstruction_dir.append("REC-MEMBRANE/REC_" + params_dict["EXP_SEG"].replace('"','').replace( "'", ""))
                reconstruction_dir.append("REC-SEED/REC_" + params_dict["EXP_SEG"].replace('"', '').replace("'", ""))
                reconstruction_dir.append("REC-MORPHOSNAKE/REC_" + params_dict["EXP_SEG"].replace('"','').replace("'", ""))
        return reconstruction_dir

    def copy_logs_files(self, source_folder, target_folder):
        """

        :param source_folder: 
        :param target_folder: 

        """
        range_t = len(source_folder)
        for i in range(0, range_t):
            source = source_folder[i]
            target = target_folder[i]
            if os.path.isdir(source):
                if not os.path.isdir(target):
                    os.makedirs(target)
                onlyfiles = [f for f in os.listdir(source) if
                             os.path.isfile(os.path.join(source, f)) and (".py" in f or ".log" in f)]
                for file in onlyfiles:
                    print("copy " + str(file) + " to " + str(target))
                    subprocess.run(["cp", os.path.join(source, file), target])

    def run(self):
        """ """
        dirs = compute_astec_dir(self.astec_command, self.params_dict)
        self.cleaner_folder = []
        input_folder = []
        target_logs = []
        source_logs = []
        for dir in dirs:
            self.cleaner_folder.append(dir.replace('"', '').replace("'", ""))
            input_folder = dir.replace('"', '').replace("'", "")
        for clean in self.cleaner_folder:
            target_logs = os.path.join(clean, "LOGS")
        for input in input_folder:
            source_logs = os.path.join(input, "LOGS")
        for clean in self.cleaner_folder:
            while not os.path.isdir(clean):
                time.sleep(5)

        self.reconstructions_folder = self.compute_recon_dir(self.params_dict)

        pyom = None
        tag_step = compute_astec_tag(self.astec_command)
        if self.omero_result:
            # Connect to OMERO
            pyom = omerolib.connect(file_path=self.omero_config_file)
            # Determine ASTEC folder depending on the step
            astec_dir = compute_astec_dir(self.astec_command, self.params_dict)
            # OMERO Dataset depending of ASTEC parameters
            for i in range(0, len(astec_dir)):
                self.omero_dataset_name.append(astec_dir[i].replace("POST/", "").replace("SEG/", "").replace("FUSE/", "").replace(
                '"', '').replace("'", ""))
            self.omero_dataset_recon_name = None
            for recon in self.reconstructions_folder:
                if "REC-MEMBRANE" in recon:
                    self.omero_dataset_recon_name = recon.replace("REC-MEMBRANE/","").replace('"', '').replace("'", "")

            # Project = embryo name
            self.omero_project_name = self.name_embryo
            # GET or CREATE project
            if pyom.get_project_by_name(self.omero_project_name) is None:
                pyom.create_project(self.omero_project_name)
            self.o_project = pyom.get_project_by_name(self.omero_project_name)
            self.project_id = self.o_project.getId()
            # GET or CREATE dataset
            for omero_name in self.omero_dataset_name:
                if pyom.get_dataset_by_name(omero_name, self.project_id) is None:
                    pyom.create_dataset(omero_name, self.project_id)
            if  self.omero_dataset_recon_name is not None and pyom.get_dataset_by_name(self.omero_dataset_recon_name, self.project_id) is None:
                pyom.create_dataset(self.omero_dataset_recon_name, self.project_id)
                self.reco_dataset_id = pyom.get_dataset_by_name(self.omero_dataset_recon_name, self.project_id).getId()
            for omero_name in self.omero_dataset_name:
                self.dataset_ids.append(pyom.get_dataset_by_name(omero_name, self.project_id).getId())
        for i in range(0, len(self.cleaner_folder)):
            if not i in self.omero_files:
                self.omero_files.insert(i,[])
            list_images = pyom.get_images_filename(self.dataset_ids[i])
            for image_name in list_images:
                if not image_name in self.omero_files[i]:
                    self.omero_files[i].append(image_name)
        # Manage time points at runtime
        for current_time in range(self.begin, self.end + 1):
            if current_time < self.end:
                for dir in self.cleaner_folder:
                    while not self.image_t_exists(current_time + 1, dir):
                        time.sleep(10)
                    self.clean_at_t(current_time, pyom)
            else:
                for dir in self.cleaner_folder:
                    while not self.image_t_exists(self.end, dir):
                        time.sleep(10)
                    self.clean_at_t(current_time, pyom)
        if self.astec_command == "astec_fusion" and len(self.cleaner_folder) > 1:
            for current_time in range(self.begin, self.end + 1):
                self.clean_at_t(current_time, pyom) # Upload what hasn't been uploaded after while

        # upload xml and attachements at the end
        if self.omero_result:
            onlyfiles = []
            for dir in self.cleaner_folder:
               for f in os.listdir(dir):
                   if os.path.isfile(os.path.join(dir, f)):
                       onlyfiles.append(os.path.join(dir, f))
            for file in onlyfiles:
                if not is_file_image_or_compressed(file):
                    if pyom is not None:
                        print("Upload attachment file")
                        pyom.add_file_to_dataset(self.dataset_ids[0], file)
            if self.tag_list is not None and len(self.tag_list) > 0:
                dataset = pyom.get_dataset_by_id(self.dataset_ids[0], project=self.project_id)
                if dataset is not None:
                    for tag in self.tag_list:
                        pyom.add_tag(dataset, tag)
                    if tag_step != "":
                        pyom.add_tag(dataset, tag_step)
                else:
                    print("could not find dataset : " + str(self.dataset_ids[0]))
        self.copy_logs_files(source_logs, target_logs)
        if self.omero_result:
            if os.path.isfile(xml_metadata):
                pyom.add_file_to_dataset(self.dataset_ids[0],xml_metadata)
        if pyom is not None:
            pyom.o_close()
        # omero the non images files and non gz files


def compute_input_folder(astec_command, params_dict):
    """

    :param astec_command: 
    :param params_dict: 

    """
    dir_to_create = ""
    if "seg" in astec_command.lower() or astec_command.lower() == "astec_astec":
        if "EXP_FUSE" in params_dict:
            dir_to_create = "FUSE/FUSE_" + params_dict["EXP_FUSE"].replace("'", "").replace('"','')
        else:
            dir_to_create = "FUSE/FUSE_RELEASE"
    elif "post" in astec_command.lower():
        if "EXP_SEG" in params_dict:
            dir_to_create = "SEG/SEG_" + params_dict["EXP_SEG"].replace("'", "").replace('"','')
        else:
            dir_to_create = "SEG/SEG_RELEASE"
    else:
        return None
    return dir_to_create


class start_astec_command(Thread):
    """ """
    def __init__(self, astec_instance):
        Thread.__init__(self)
        self.astec_command = astec_instance.astec_command
        self.embryo_folder = astec_instance.folder_embryo
        self.name_embryo = astec_instance.embryo_name
        self.begin = astec_instance.begin_time
        self.end = astec_instance.end_time
        self.mars_path = astec_instance.mars_path
        self.params_dict = astec_instance.params_dict
        self.keep_temp = astec_instance.keep_temp
        self.use_omero_input = astec_instance.omero_input
        self.omero_config_file = astec_instance.omero_config_file
        self.omero_project_name = astec_instance.input_project
        self.omero_dataset_name = astec_instance.input_set
        self.astecenv = astec_instance.envastec
        self.paramsuffix = astec_instance.paramsuffix
        self.running_dir = ""
    def copy_logs_files(self, source_folder, target_folder):
        """

        :param source_folder: 
        :param target_folder: 

        """
        range_t = len(source_folder)
        for i in range(0, range_t):
            source = source_folder[i]
            target = target_folder[i]
            if os.path.isdir(source):
                if not os.path.isdir(target):
                    os.makedirs(target)
                onlyfiles = [f for f in os.listdir(source) if
                             os.path.isfile(os.path.join(source, f)) and (".py" in f or ".log" in f)]
                for file in onlyfiles:
                    print("copy " + str(file) + " to " + str(target))
                    subprocess.run(["cp", os.path.join(source, file), target])

    def run(self):
        """ """
        print("Managining data for " + self.astec_command + " on embryo " + self.embryo_folder)
        final_command_arg0 = compute_astec_command(self.astec_command)
        self.running_dir = compute_astec_dir(self.astec_command, self.params_dict)
        if self.use_omero_input:
            folder_target = compute_input_folder(self.astec_command, self.params_dict)
            if folder_target is None:
                print("Unable to comput input files folders , exiting")
                return
            os.makedirs(folder_target)
            pyom = omerolib.connect(file_path=self.omero_config_file)
            pyom.download_omero_set(self.omero_project_name, self.omero_project_name, folder_target)
        if final_command_arg0 != "astec_embryoproperties":
            for dir in self.running_dir:
                if dir != "":
                    final_dir = dir.replace('"', '').replace("'", "").replace("[", "").replace("]", "")
                    if not os.path.isdir(final_dir):
                        os.makedirs(final_dir, mode=0o777)
            if self.mars_path is not None and final_command_arg0 == "astec_astec":
                if not os.path.isdir(self.running_dir[0].replace("'", "").replace('"', '')):
                    os.makedirs(self.running_dir[0].replace("'", "").replace('"', ''), mode=0o777)
                print("Copying mars for " + self.astec_command + " on embryo " + self.embryo_folder)
                os.system("cp " + str(self.mars_path).replace("'", "").replace('"', '') + " " + str(
                    self.running_dir[0]).replace("'", "").replace('"', '') + "/")
        print("Generating parameters for " + self.astec_command + " on embryo " + self.embryo_folder)
        parameters_name = self.astec_command + "_" + self.running_dir[0].replace("/", "_").replace("\\",
                                                                                                   "_").replace(
            '"', '') + "_" + self.paramsuffix + ".py"
        parameter_content = ""
        parameter_content += 'PATH_EMBRYO = "."\n'
        parameter_content += 'EN = "' + str(self.name_embryo).replace("'","").replace('"','') + '"\n'
        parameter_content += 'begin = ' + str(int(self.begin)) + '\n'
        if self.end != -1:
            parameter_content += 'end = ' + str(int(self.end)) + '\n'
        for dict_key in self.params_dict:
            if not dict_key == "mars_path" and not dict_key == "begin" and not dict_key == "end" and not dict_key == "raw_delay" and not dict_key == "delta":
                value_param = self.params_dict[dict_key]
                #print("working on param "+dict_key+" -> "+str(value_param))
                if not isinstance(self.params_dict[dict_key], bool) and isinstance(self.params_dict[dict_key], str) and not isinstance(self.params_dict[dict_key],list):
                    #print("need to add the quotes")
                    if not '"' in self.params_dict[dict_key] and not "'" in self.params_dict[dict_key]:
                        value_param = "'"+self.params_dict[dict_key]+"'"
                parameter_content += str(dict_key) + ' = ' + str(value_param) + '\n'
        print("Writing parameters file for " + self.astec_command)
        f = open(parameters_name, "w+")
        f.write(parameter_content)
        f.close()
        commandrun = ""
        if self.keep_temp:
            commandrun = " conda run -n " + self.astecenv + " " + final_command_arg0 + " -k -p " + parameters_name
        else:
            commandrun = " conda run -n " + self.astecenv + " " + final_command_arg0 + " -p " + parameters_name
        os.system(commandrun)
        print("Command finished for " + self.astec_command)
        inputf = compute_input_folder(self.astec_command,self.params_dict)
        if inputf is not None:
            source_logs = []
            target_logs = []
            source_logs.append(os.path.join(inputf, "LOGS"))
            for inputfold in self.running_dir:
                target_logs.append(os.path.join(inputfold, "LOGS"))
            self.copy_logs_files(source_logs, target_logs)
        os.system("rm " + parameters_name)


class Manager:
    """ """
    def __init__(self,astec_env="astec"):
        self.running_sessions = []
        self.running_cleaners = []
        self.to_run_list = []
        self.stop_run = False
        self.astec_instance = astec_env

    def add_to_run(self, astec_command, folder_embryo, embryo_name, begin_time, params_dict=None, end_time=-1,
                   mars_path=None, compress_result=True, omero_result=False, omero_config_file="", tag_list=None,
                   keep_temp=False, paramsuffix="", omeroinput=False, inputproject=None,
                   inputset=None):
        """

        :param astec_command: 
        :param folder_embryo: 
        :param embryo_name: 
        :param begin_time: 
        :param params_dict:  (Default value = None)
        :param end_time:  (Default value = -1)
        :param mars_path:  (Default value = None)
        :param compress_result:  (Default value = True)
        :param omero_result:  (Default value = False)
        :param omero_config_file:  (Default value = "")
        :param tag_list:  (Default value = None)
        :param keep_temp:  (Default value = False)
        :param paramsuffix:  (Default value = "")
        :param omeroinput:  (Default value = False)
        :param inputproject:  (Default value = None)
        :param inputset:  (Default value = None)

        """
        ai = astec_instance(astec_command, folder_embryo, embryo_name, mars_path, compress_result,
                            copy.deepcopy(params_dict),
                            begin_time, end_time, omero_result, omero_config_file, tag_list, keep_temp, self.astec_instance,
                            paramsuffix, omeroinput, inputproject, inputset)
        self.to_run_list.append(ai)


    def start_running(self, thread_number=-1):
        """

        :param thread_number:  (Default value = -1)

        """
        cpuCount = cpu_count()
        thread_count = cpuCount * 2 / 6
        if thread_number != -1:
            thread_count = thread_number
        for param in self.to_run_list:
            if len(self.running_sessions) >= thread_count:
                tc = self.running_sessions.pop(0)
                tc.join()
            tc = start_astec_command(param)
            tc.start()
            if param.compress_result or param.omero_result:
                tc2 = start_astec_cleaner(param.astec_command, param.params_dict, param.embryo_name, param.omero_result,
                                          param.begin_time, param.end_time,
                                          param.compress_result, param.omero_config_file, param.tag_list,
                                          param.keep_temp)
                tc2.start()
            self.running_sessions.append(tc)
            if param.compress_result or param.omero_result:
                self.running_cleaners.append(tc2)
        while len(self.running_sessions) > 0:
            tc = self.running_sessions.pop(0)
            if param.compress_result or param.omero_result:
                tc2 = self.running_cleaners.pop(0)
            if tc is not None:
                tc.join()
            if (param.compress_result or param.omero_result) and tc2 is not None:
                tc2.stop_cleaning()
                tc2.join()
        self.running_sessions = []
        self.running_cleaners = []
        self.to_run_list = []

    def compute_graphs_test_segmentation(self, embryo_name, begin, end,added_lineages=None):
        """

        :param embryo_name: 
        :param begin: 
        :param end: 
        :param added_lineages:  (Default value = None)

        """
        #atlas_path = self.compute_atlas()
        #ref_lineage = atlas_path[0]
        mincells_test = 64
        maxcells_test = 500

        folder_out = os.path.join("analysis/", "test_segmentation")
        lineages = [
            "POST/POST_test_maximum_gace/" + embryo_name + "_post_lineage.xml",
            "POST/POST_test_maximum_glace/" + embryo_name + "_post_lineage.xml",
            "POST/POST_test_addition_gace/" + embryo_name + "_post_lineage.xml",
            "POST/POST_test_addition_glace/" + embryo_name + "_post_lineage.xml"]
        names = ["POST_test_maximum_gace", "POST_test_maximum_glace", "POST_test_addition_gace", "POST_test_addition_glace"]
        if added_lineages is not None:
            for lineage in added_lineages:
                lineages.append("POST/POST_"+str(lineage)+"/"+ embryo_name + "_post_lineage.xml")
                names.append("POST_"+str(lineage))
        apply_analysis(lineages, names, folder_out, embryo_name, begin, end,
                        ref_lineage=None, data_path=folder_out)
        if os.path.isfile("histogram_branch_data.csv"):
            os.system("rm histogram_branch_data.csv")

    def compute_graphs_post(self, embryo_name, begin, end,post_list):
        """

        :param embryo_name: 
        :param begin: 
        :param end: 
        :param post_list: 

        """
        #atlas_path = self.compute_atlas()
        #ref_lineage = atlas_path[0]
        mincells_test = 64
        maxcells_test = 500
        folder_out = os.path.join("analysis/", "post_segmentation")
        lineages = []
        names = []
        for exp_post in post_list:
            lineages.append( "."+ "/POST/POST_" + str(exp_post) + "/" + embryo_name + "_post_lineage.xml")
            names.append("POST_"+str(exp_post))

        apply_analysis(lineages, names, folder_out, embryo_name, begin, end,
                        is_post=True, ref_lineage=None,
                       data_path=folder_out)
        if os.path.isfile("histogram_branch_data.csv"):
            os.system("rm histogram_branch_data.csv")

    def compute_graphs_post(self, embryo_name, begin, end,post_list):
        """

        :param embryo_name: 
        :param begin: 
        :param end: 
        :param post_list: 

        """
        #atlas_path = self.compute_atlas()
        #ref_lineage = atlas_path[0]
        mincells_test = 64
        maxcells_test = 500
        folder_out = os.path.join("analysis/", "post_segmentation")
        lineages = []
        names = []
        for exp_post in post_list:
            lineages.append( "."+ "/POST/POST_" + str(exp_post) + "/" + embryo_name + "_post_lineage.xml")
            names.append("POST_"+str(exp_post))

        apply_analysis(lineages, names, folder_out, embryo_name, begin, end,
                        is_post=True, ref_lineage=None,
                       data_path=folder_out)
        if os.path.isfile("histogram_branch_data.csv"):
            os.system("rm histogram_branch_data.csv")


    def compute_folder_graphs_post(self, embryo_folder,embryo_name, begin, end,post_list):
        """

        :param embryo_folder: 
        :param embryo_name: 
        :param begin: 
        :param end: 
        :param post_list: 

        """
        #atlas_path = self.compute_atlas()
        #ref_lineage = atlas_path[0]
        mincells_test = 64
        maxcells_test = 500
        folder_out = os.path.join(".", os.path.join("analysis/", "post_segmentation"))
        lineages = []
        names = []
        for exp_post in post_list:
            lineages.append( "."+ "/POST/POST_" + str(exp_post) + "/" + embryo_name + "_post_lineage.xml")
            names.append("POST_"+str(exp_post))

        apply_analysis(lineages, names, folder_out, embryo_name, begin, end,
                        is_post=True, ref_lineage=None,
                       data_path=folder_out)
        if os.path.isfile("histogram_branch_data.csv"):
            os.system("rm histogram_branch_data.csv")


    def plot_signal_to_noise(self, embryo_name, parameters,one_stack_only=False,stack_chosen=0):
        """

        :param embryo_name: 
        :param parameters: 
        :param one_stack_only:  (Default value = False)
        :param stack_chosen:  (Default value = 0)

        """
        print("-> Analyzing raw data intensities, this step may be long (you can continue the pipeline , please do not delete Raw Images)")
        plotsignaltonoise(embryo_name, parameters,one_stack_only=one_stack_only,stack_chosen=stack_chosen)



    def plot_signal_to_noise_tofolder(self, folder,embryo_name,one_stack_only=False,stack_chosen=0):
        """

        :param folder: 
        :param embryo_name: 
        :param one_stack_only:  (Default value = False)
        :param stack_chosen:  (Default value = 0)

        """
        plotsignaltonoise_tofolder(folder,one_stack_only=one_stack_only,stack_chosen=stack_chosen)


    def generate_surface(self, exp_fuse, exp_post, begin, end, xmloutput, embryo_name, exp_intrareg):
        """

        :param exp_fuse: 
        :param exp_post: 
        :param begin: 
        :param end: 
        :param xmloutput: 
        :param embryo_name: 
        :param exp_intrareg: 

        """
        fuse_path =  "./"+embryo_name+"/INTRAREG/INTRAREG_" + str(exp_intrareg) + "/FUSE/FUSE_" + str(exp_fuse)
        fuse_template = os.path.join(fuse_path, embryo_name + "_intrareg_fuse_t%03d.nii").replace("'", "").replace('"', '')
        post_path = "./"+embryo_name+"/INTRAREG/INTRAREG_" + str(exp_intrareg) + "/POST/POST_" + str(exp_post)
        post_template = os.path.join(post_path, embryo_name + "_intrareg_post_t%03d.nii").replace("'", "").replace('"', '')
        os.system("conda run -n astec mc-cellProperties  -fusion-format " + str(
                fuse_template) + " -segmentation-format " + str(post_template) + " -first " + str(
                begin) + " -last " + str(end) + " -o " + str(
                xmloutput) + " -feature contact-surface -feature barycenter -v -v -v -v -v")



    def generate_prop_naming_parameters(self, xml_folder, xml_file, embryo_name):
        """

        :param xml_folder: 
        :param xml_file: 
        :param embryo_name: 

        """
        atlas_path = compute_atlas()
        atlases_files = []
        now = datetime.now()
        parameters_name = "prop_naming" + str(now.timestamp()).replace('.', '') + ".py"
        txt = ""
        final_file = os.path.join(xml_folder.replace(str(embryo_name) + "/", ""), xml_file)
        txt += "inputFile = '" + str(final_file) + "'" + "\n"
        txt += "outputFile = '" + str(final_file) + "'" + "\n"
        txt += "confidence_atlases_nmin = 2" + "\n"
        txt += "write_selection = False" + "\n"
        txt += "confidence_atlases_percentage = 0" + "\n"
        txt += 'atlasFiles = '+str(atlas_path) + "\n"
        atlases_files.append("pm9.xml")
        f = open(parameters_name, "w+")
        f.write(txt)
        f.close()
        return parameters_name,atlas_path

    def backup_xml(self, xml_file):
        """

        :param xml_file: 

        """
        split_name = xml_file[1:len(xml_file)].split(".")
        backup_name = split_name[0] + "_backup." + split_name[1]
        os.system("cp " + str(xml_file) + " ." + str(backup_name))

    def compute_cell_count(self, mars_path):
        """

        :param mars_path: 

        """
        count = -1
        image_first = imread(mars_path)
        if mars_path is not None:
            count = len(np.unique(image_first)) - 1
        return count

    def generate_init_naming(self, xml_folder, xml_file, begin_time_name, embryo_name, exp_fuse, exp_post, begin, end,
                             exp_intrareg):
        """

        :param xml_folder: 
        :param xml_file: 
        :param begin_time_name: 
        :param embryo_name: 
        :param exp_fuse: 
        :param exp_post: 
        :param begin: 
        :param end: 
        :param exp_intrareg: 

        """

        print(" -> Generate init naming")
        xml_path = os.path.join(xml_folder, xml_file)
        mars_path = os.path.join(xml_folder, begin_time_name)
        source = open(xml_path)
        tree = ET.parse(source)
        tree = tree.getroot()
        lineage_elem = tree.find("cell_contact_surface")
        print("     - backup xml")
        self.backup_xml(xml_path)
        surface_xml = xml_path.replace("lineage", "lineage_surfaces")
        if lineage_elem is None:
            print("     - generate surfaces in side xml")
            self.generate_surface(exp_fuse, exp_post, begin, end, surface_xml, embryo_name, exp_intrareg)
            print("     - merging 2 xml")
            os.system(
                "conda run -n astec astec_embryoproperties -i " + xml_path + " " + surface_xml + " -o " + xml_path)
            print("     - cleaning temp xml")
            os.system("rm " + str(surface_xml))
        print("     - compute cell count from mars")
        cell_count = self.compute_cell_count(mars_path)
        print("     - generate naming parameter file")
        parameter_file = self.generate_init_naming_parameters(cell_count, xml_folder, xml_file, embryo_name)
        print("     - running naming")
        os.system("conda run -n ascidian-dev ascidian_atlas_init_naming -v -v -v -p " + str(
            parameter_file))
        os.system("rm " + str(parameter_file))

    def propagate_naming(self, xml_folder, xml_file, embryo_name):
        """

        :param xml_folder: 
        :param xml_file: 
        :param embryo_name: 

        """
        print(" -> Propagate naming")
        print("     - generate parameters")
        parameter_file,atlases_files = self.generate_prop_naming_parameters(xml_folder, xml_file, embryo_name)
        print("     - propagation of naming")
        os.system("conda run -n ascidian-dev ascidian_atlas_naming -v -v -v -p " + str(
            parameter_file))
        print("     - cleaning")
        os.system("rm " + str(parameter_file))
        return atlases_files

    def writeStepToJson(self, parameters,step,embryo_folder=".",logFolder=None):
        """

        :param parameters: 
        :param step: 
        :param embryo_folder:  (Default value = ".")
        :param logFolder:  (Default value = None)

        """
        parameters["step"] = step
        addDictToMetadata(embryo_folder,parameters,addDate=True,logFolder=logFolder)
    def downscale_folder(self, parameters):
        """

        :param parameters: 

        """
        embryo_name = parameters["embryo_name"].replace('"','').replace("'","")
        omero_config_file = get_omero_config(parameters)
        voxel_size = float(parameters["resolution"])
        input_voxel_size = 0.3
        if not "input_resolution" in parameters:
            parameters["input_resolution"] = input_voxel_size
        else :
            input_voxel_size = float(parameters["input_resolution"])
        embryo_folder = "."
        input_folder = os.path.join(embryo_folder, "FUSE/FUSE_" + str(parameters["EXP_FUSE"]))
        output_folder = os.path.join(embryo_folder, "FUSE/FUSE_" + str(parameters["EXP_FUSE"]) + "_down0"+str(voxel_size).split(".")[1])
        files = os.listdir(input_folder)
        files.sort()
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)

        for file in files:
            img_path = os.path.join(input_folder, file)
            # make sure file is an image
            if file.endswith(('.mha', '.nii', '.mha.gz', '.nii.gz', '.inr', '.inr.gz')):
                os.system("conda run -n astec setVoxelSize " + str(img_path) + " " + str(
                    input_voxel_size) + " " + str(input_voxel_size) + " " + str(input_voxel_size))
                print("     -> " + str(img_path))
                img_t = os.path.join(output_folder, file)
                os.system("conda run -n astec applyTrsf -iso " + str(voxel_size) + " " + img_path + " " + img_t)

        if omero_config_file is not None:
            self.upload_on_omero(omero_config_file, embryo_name, "FUSE_" + str(parameters["EXP_FUSE"]) + "_down0"+str(voxel_size).split(".")[1],
                                 output_folder)


    def downscale_contour_folder(self, parameters):
        """

        :param parameters: 

        """
        voxel_size = float(parameters["resolution"])
        embryo_folder = "."
        input_folder = os.path.join(embryo_folder, "CONTOUR/CONTOUR_" + str(parameters["EXP_CONTOUR"]))
        output_folder = os.path.join(embryo_folder, "CONTOUR/CONTOUR_" + str(parameters["EXP_CONTOUR_DOWNSCALED"]))
        template_format = parameters["template_file"]
        input_voxel_size = 0.3
        if not "input_resolution" in parameters:
            parameters["input_resolution"] = input_voxel_size
        else:
            input_voxel_size = float(parameters["input_resolution"])
        files = os.listdir(input_folder)
        files.sort()
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)
        for file in files:
            # make sure file is an image
            if file.endswith(('.mha', '.nii', '.mha.gz', '.nii.gz', '.inr', '.inr.gz')):
                img_path = os.path.join(input_folder, file)
                time = int(file.split("_t")[1].split(".")[0])
                print("     -> " + str(img_path))
                img_t = os.path.join(output_folder, file)
                img_template = template_format.format(time)
                os.system("conda run -n astec setVoxelSize " + str(img_path) + " " + str(
                    input_voxel_size) + " " + str(input_voxel_size) + " " + str(input_voxel_size))
                os.system("conda run -n astec applyTrsf -ref " + str(img_template) + " -iso " + str(voxel_size) + " " + img_path + " " + img_t)
    def save_upload_parameters(self, omero_project_name, omero_dataset_name, embryo_folder,user=None):
        """

        :param omero_project_name: 
        :param omero_dataset_name: 
        :param embryo_folder: 
        :param user:  (Default value = None)

        """
        parameters = {}
        parameters["user"] = user
        parameters["omero_project"] = omero_project_name
        parameters["omero_dataset"] = omero_dataset_name
        parameters["input_folder"] = embryo_folder
        self.writeStepToJson(parameters, "upload_to_omero", embryo_folder=".")
    def upload_on_omero(self, config_file, omero_project_name, omero_dataset_name, input_folder, include_logs=False,embryo_name=None,user=None):
        """

        :param config_file: 
        :param omero_project_name: 
        :param omero_dataset_name: 
        :param input_folder: 
        :param include_logs:  (Default value = False)
        :param embryo_name:  (Default value = None)
        :param user:  (Default value = None)

        """
        config_array = omerolib.parse_parameters_file(config_file)
        om_login = config_array['login']
        om_pw = config_array['password']
        om_host = config_array['host']
        om_port = int(config_array['port'])
        om_group = config_array['group']
        om_secure = config_array['secure']
        embryo_folder = "."

        pyom = omerolib.connect(login=om_login, passwd=om_pw, server=om_host, port=om_port, group=om_group,
                                secure=om_secure)
        pyom.upload_omero_set(omero_project_name.replace("'", "").replace('"', ''),
                              omero_dataset_name.replace("'", "").replace('"', ''),
                              input_folder.replace("'", "").replace('"', ''), include_logs=include_logs)
        self.save_upload_parameters(omero_project_name, omero_dataset_name,embryo_folder,user)

    def download_from_omero_all(self,dataset,project,output_folder,om_login,om_pw,om_host,om_port,om_group="",om_secure=False):
        """

        :param dataset: 
        :param project: 
        :param output_folder: 
        :param om_login: 
        :param om_pw: 
        :param om_host: 
        :param om_port: 
        :param om_group:  (Default value = "")
        :param om_secure:  (Default value = False)

        """
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)

        pyom = omerolib.connect(login=om_login, passwd=om_pw, server=om_host, port=om_port, group=om_group,
                                secure=om_secure)
        pyom.download_omero_set(project.replace("'", "").replace('"', ''),
                                dataset.replace("'", "").replace('"', ''),
                                output_folder.replace("'", "").replace('"', ''))

    def parse_no_suffix(self,dataset_name):
        """

        :param dataset_name: 

        """
        if dataset_name.lower() == "mars":
            return "SEG/MARS"
        if dataset_name.lower() == "seg":
            return "SEG/SEG_RELEASE"
        if dataset_name.lower() == "post":
            return "POST/POST_RELEASE"
        if dataset_name.lower() == "fuse":
            return "FUSE/FUSE_RELEASE"
        if dataset_name.lower() == "background":
            return "BACKGROUND/BACKGROUND_RELEASE"
        if dataset_name.lower() == "contour":
            return "CONTOUR/CONTOUR_RELEASE"
        return None
    def parse_subfolder(self,dataset_subname):
        """

        :param dataset_subname: 

        """
        if dataset_subname.lower() in ["fuse","fusion"]:
            return "FUSE"
        if dataset_subname.lower() in ["seg","segmentation","astec"]:
            return "SEG"
        if dataset_subname.lower() in ["post","postcorr"]:
            return "POST"
        if dataset_subname.lower() == "background":
            return "BACKGROUND"
        if dataset_subname.lower() == "contour":
            return "CONTOUR"
        return None

    def compute_dataset_path(self,dataset_name):
        """

        :param dataset_name: 

        """
        moved_corr = False
        splitted_name = dataset_name.split("_")
        print(splitted_name)
        if splitted_name[0].lower() in ["corr", "curated"]:  # Moving CORR to the end
            elem = splitted_name.pop(0)
            splitted_name.insert(len(splitted_name), elem)
            moved_corr = True
            print(splitted_name)
        if not "_" in dataset_name:
            return self.parse_no_suffix(dataset_name)
        elif len(splitted_name) == 2 and moved_corr:
            parsed = self.parse_no_suffix(splitted_name[0])
            if parsed is None:
                return None
            return parsed+"_"+splitted_name[-1]
        else:
            no_intra_name = False
            if splitted_name[0].lower() in ["int","intrareg"]:
                path = "INTRAREG/INTRAREG_"
                if len(splitted_name) > 1:
                    if splitted_name[1].lower() not in ["fuse","post","seg"]:
                        path += splitted_name[1]
                    else:
                        path+= "RELEASE"
                        no_intra_name = True
                if len(splitted_name) == 2 and no_intra_name:
                    suffix = self.parse_no_suffix(splitted_name[1])
                    if suffix is None:
                        return None
                    path += "/" + suffix + "/" + suffix + "_RELEASE/"
                    return path
                if len(splitted_name) > 2:
                    if (len(splitted_name) == 3 and not no_intra_name) or (len(splitted_name) == 4 and moved_corr and not no_intra_name) or (len(splitted_name) == 4 and not moved_corr and no_intra_name) and (len(splitted_name) == 5 and moved_corr and no_intra_name):
                        suffix = self.parse_no_suffix(splitted_name[1])
                        if suffix is None:
                            return None
                        if len(splitted_name) == 3:
                            path += "/"+suffix+"/"
                        if len(splitted_name) == 4 and moved_corr:
                            path += "/"+suffix+ splitted_name[-1]+"/"
                    else :
                        if no_intra_name:
                            subfolder = self.parse_subfolder(splitted_name[1])
                            if subfolder is None:
                                return None
                            path += "/"+subfolder+"/"
                            path += subfolder
                            for i in range(2,len(splitted_name)):
                                path+="_"+splitted_name[i]
                            path += "/"
                        else :
                            subfolder = self.parse_subfolder(splitted_name[2])
                            if subfolder is None:
                                return None
                            path += "/" + subfolder + "/"
                            path += subfolder
                            for i in range(3, len(splitted_name)):
                                path += "_" + splitted_name[i]
                            path += "/"
                return path
            else:
                path = ""
                if len(splitted_name) > 1:
                        subfolder = self.parse_subfolder(splitted_name[0])
                        if subfolder is None:
                            return None
                        path += subfolder+"/"
                        path += subfolder
                        for i in range(1,len(splitted_name)):
                            path+="_"+splitted_name[i]
                        path += "/"
                else:
                    return None
                return path
        return None


    def download_whole_embryo(self,parameters):
        """

        :param parameters: 

        """
        config_file = get_omero_config(parameters)
        omero_project_name = parameters["project_name"].replace('"','').replace("'","")
        output_folder = parameters["output_folder"]
        if config_file is None:
            print("OMERO config file is not bound, unable to upload")
            return
        if not os.path.isfile(config_file):
            print("Unable to find OMERO config file , unable to upload")
            return
        embryo_dir = os.path.join(output_folder,omero_project_name)
        if not os.path.isdir(embryo_dir):
            os.makedirs(embryo_dir)
        if not os.path.isdir(embryo_dir):
            print("Unable to create embryo directory")
            return
        config_array = omerolib.parse_parameters_file(config_file)
        om_login = config_array['login']
        om_pw = config_array['password']
        om_host = config_array['host']
        om_port = int(config_array['port'])
        om_group = ""
        if 'group' in config_array:
            om_group = config_array['group']
        om_secure = config_array['secure']
        pyom = omerolib.connect(login=om_login, passwd=om_pw, server=om_host, port=om_port, group=om_group,
                                secure=om_secure)
        datasets = []
        project = None
        for p in pyom.list_projects():
            if p.getName().lower() == omero_project_name.lower():
                project = p
                datasets = list(p.listChildren())
                break
        if project is None:
            print("Embryo not found on OMERO")
            return
        if len(datasets) < 1:
            print("No datasets in embryo on OMERO")
            return
        print("Downloading project : "+project.getName())
        for dataset in datasets:
            # Compute outputfolder
            print("Downloading dataset : "+dataset.getName())
            dataset_subfolder = self.compute_dataset_path(dataset.getName())
            if dataset_subfolder is not None:
                dataset_ouput_folder = os.path.join(embryo_dir,dataset_subfolder)
                print(" - in : "+dataset_ouput_folder)
                pyom.download_omero_set_by_id(dataset.getId(),dataset_ouput_folder) # TESTS ONLY
            else :
                print("Unable to compute path for dataset : "+dataset.getName())

    def upload_step_dir(self,project_name,step_folder,pyom,prefix=""):
        """

        :param project_name: 
        :param step_folder: 
        :param pyom: 
        :param prefix:  (Default value = "")

        """
        step_subdirs = [f for f in os.listdir(step_folder) if os.path.isdir(os.path.join(step_folder, f))]
        current_step = step_folder.split("/")[-1]
        for subdir in step_subdirs:
            if subdir.lower().startswith(current_step.lower()): # Only upload data folders, not system ones
                pyom.upload_omero_set(project_name,prefix+subdir,os.path.join(step_folder,subdir),include_logs=(os.path.isdir(os.path.join(os.path.join(step_folder,subdir),"LOGS"))))

    def upload_intrareg_dir(self, project_name, step_folder, pyom):
        """

        :param project_name: 
        :param step_folder: 
        :param pyom: 

        """
        step_subdirs = [f for f in os.listdir(step_folder) if os.path.isdir(os.path.join(step_folder, f))]
        for subdir in step_subdirs:
            final_prefix = subdir+"_"
            intra_subdirs = [f for f in os.listdir(os.path.join(step_folder,subdir)) if
                            os.path.isdir(os.path.join(os.path.join(step_folder,subdir), f)) and f.lower() in ["fuse","seg","post","background","contour","rec-membrane"]]
            for isd in intra_subdirs:
                self.upload_step_dir(project_name,os.path.join(os.path.join(step_folder,subdir),isd),pyom,prefix=final_prefix)


    def upload_whole_embryo(self,parameters):
        """

        :param parameters: 

        """
        config_file = get_omero_config(parameters)
        embryo_name = parameters["project_name"].replace('"','').replace("'","")
        input_folder = parameters["embryo_folder"]
        if config_file is None:
            print("OMERO config file is not bound, unable to upload")
            return
        if not os.path.isfile(config_file):
            print("Unable to find OMERO config file , unable to upload")
            return
        embryo_dir = input_folder
        if not os.path.isdir(embryo_dir):
            print("Embryo dir does not exist")
            return
        config_array = omerolib.parse_parameters_file(config_file)
        om_login = config_array['login']
        om_pw = config_array['password']
        om_host = config_array['host']
        om_port = int(config_array['port'])
        om_group = ""
        if 'group' in config_array:
            om_group = config_array['group']
        om_secure = config_array['secure']
        pyom = omerolib.connect(login=om_login, passwd=om_pw, server=om_host, port=om_port, group=om_group,
                                secure=om_secure)
        #upload_omero_set(self,project_name,dataset_name,input_folder,mintime=None,maxtime=None,tag_list=None,include_logs=False)
        project = None
        project_name = None
        for p in pyom.list_projects():
            if p.getName().lower() == embryo_name.lower():
                project = p.getName()
                project_name = p.getName()
                break
        if project is None:
            print("Embryo not found on OMERO")
            # create it
            project = pyom.create_project(embryo_name)
            project_name = embryo_name
        if project is None:
            print("Unable to create OMERO project")
            return
        step_subdirs = [f for f in os.listdir(embryo_dir) if os.path.isdir(os.path.join(embryo_dir, f)) and f.lower() in ["fuse","seg","post","background","contour","rec-membrane"]]
        for step_subdir in step_subdirs:
            self.upload_step_dir(project_name,os.path.join(embryo_dir,step_subdir),pyom)
        intra_subdirs = [f for f in os.listdir(embryo_dir) if os.path.isdir(os.path.join(embryo_dir, f)) and f.lower() == "intrareg"]
        for intra in intra_subdirs:
            self.upload_intrareg_dir(project_name,os.path.join(embryo_dir, intra),pyom)


    def download_from_omero(self, parameters):
        """

        :param parameters: 

        """
        config_file = get_omero_config(parameters)
        omero_project_name = parameters["project_name"].replace('"','').replace("'","")
        omero_dataset_name = parameters["dataset_name"]
        output_folder = parameters["destination_folder"]
        if config_file is None:
            print("OMERO config file is not bound, unable to upload")
            exit()
        if not os.path.isfile(config_file):
            print("Unable to find OMERO config file , unable to upload")
            exit()
        config_array = omerolib.parse_parameters_file(config_file)
        om_login = config_array['login']
        om_pw = config_array['password']
        om_host = config_array['host']
        om_port = int(config_array['port'])
        om_group = ""
        if 'group' in config_array:
            om_group = config_array['group']
        om_secure = config_array['secure']
        self.download_from_omero_all(omero_dataset_name,omero_project_name,output_folder,om_login,om_pw,om_host,om_port,om_group,om_secure)


    def compute_contours(self, parameters):
        """

        :param parameters: 

        """

        omero_config_file = get_omero_config(parameters)
        normalisation = parameters["normalisation"]
        background_folder_name = parameters["EXP_BACKGROUND"]
        voxel_size = parameters["resolution"]
        embryo_name = parameters["embryo_name"].replace('"','').replace("'","")
        user = compute_user(parameters)
        embryo_folder ="./"
        compute_contour(embryo_folder, background_folder_name, reducvoxelsize=float(voxel_size),
                        target_normalization_max=normalisation, correction_vsize=True)
        contour_folder = "CONTOUR/CONTOUR_RELEASE_" + str(voxel_size).split(".")[1]
        if omero_config_file is not None:
            self.upload_on_omero(omero_config_file, embryo_name, "CONTOUR_RELEASE_" + str(voxel_size).split(".")[1],
                                 contour_folder)
        parameters["contour_folder"] = contour_folder
        self.writeStepToJson(parameters, "compute_contour", embryo_folder=".")

    def name_embryo(self, parameters):
        """

        :param parameters: 

        """
        embryo_name = parameters["embryo_name"].replace('"','').replace("'","")
        begin = parameters["begin"]
        end = parameters["end"]
        lineage_path = "./INTRAREG/INTRAREG_" + str(parameters["EXP_INTRAREG"])+"/POST/POST_" + parameters["EXP_POST"] + "/"
        mars_prefix = "_intrareg_post_t{:03d}.nii"
        lineage_name = embryo_name + "_intrareg_post_lineage.xml"
        mars_filename = embryo_name + mars_prefix.format(begin)
        if not os.path.isfile(mars_filename):
            mars_filename = mars_filename+".gz"
        self.generate_init_naming(lineage_path.replace('"', '').replace("'", ""),
                                  lineage_name.replace('"', '').replace("'", ""),
                                  mars_filename.replace('"', '').replace("'", ""),
                                  embryo_name.replace('"', '').replace("'", ""),
                                  str(parameters["EXP_FUSE"]).replace('"', '').replace("'", ""),
                                  str(parameters["EXP_POST"]).replace('"', '').replace("'", ""), begin, end,
                                  str(parameters["EXP_INTRAREG"]).replace('"', '').replace("'", ""))
        self.propagate_naming(lineage_path.replace('"', '').replace("'", ""),
                              lineage_name.replace('"', '').replace("'", ""),
                              embryo_name.replace('"', '').replace("'", ""))
        parameters["atlas"] = compute_atlas()
        logFolder = "./INTRAREG/INTRAREG_"+ str(parameters["EXP_INTRAREG"]).replace('"', '').replace("'", "")+"/LOGS/"
        self.writeStepToJson(parameters, "name_embryo", embryo_folder=".", logFolder=logFolder)


    def copy_raw_data(self, parameters):
        """

        :param parameters: 

        """

        searcher = compute_user(parameters)
        if not "embryo_name" in parameters:
            print("Embryo name is not provided in parameters ")
            exit()
        if not "distant_folder" in parameters:
            print("Distant raw data folder path is not provided in parameters")
            exit()
        input_folder = parameters["distant_folder"]
        delay_before_copy = 0
        if "delay_before_copy" in parameters:
            delay_before_copy = int(parameters["delay_before_copy"])
        embryo_dir = "."
        if not os.path.isdir(embryo_dir):
            os.makedirs(embryo_dir)
        raw_data_output = os.path.join(embryo_dir, "RAWDATA")
        if not os.path.isdir(raw_data_output):
            os.makedirs(raw_data_output)
        try:
            if delay_before_copy > 0:
                print("Sleeping "+str(delay_before_copy)+" minutes before copying RAW DATA")
                time.sleep(delay_before_copy*60) #delay is given in minutes, transform in seconds
            subprocess.run(['rsync', '-avzr', str(input_folder), raw_data_output + "/"], check=True)
            self.writeStepToJson(parameters, "copy_rawdata", embryo_folder=".")
        except subprocess.CalledProcessError:
            print('Error during the copy of the data , please verify the parameters and try again')


    def downscale_mars(self, parameters):
        """

        :param parameters: 

        """
        voxel_size = parameters["resolution"]
        if not "mars_file" in parameters:
            print("Please specify a MARS file path")
            exit()
        if not "output_folder" in parameters:
            print("Please specify the folder for the downscaled file")
            exit()
        if not "template_file" in parameters:
            print("Please specify the corresponding fusion image (downscaled version)")
            exit()
        mars = parameters["mars_file"]
        if not os.path.isfile(mars):
            print(str(mars))
            print("MARS file does not exist")
            exit()
        fusion = parameters["template_file"]
        if not os.path.isfile(fusion):
            print("template file does not exist")
            exit()
        output_folder = parameters["output_folder"]
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)
        marsname = mars.replace("\\", "/").split("/")[-1]
        output_file = os.path.join(output_folder, marsname)
        input_voxel_size = 0.3
        if not "input_resolution" in parameters:
            parameters["input_resolution"] = input_voxel_size
        else:
            input_voxel_size = float(parameters["input_resolution"])
        os.system("conda run -n astec setVoxelSize " + str(mars) + " " + str(
            input_voxel_size) + " " + str(input_voxel_size) + " " + str(input_voxel_size))
        os.system("conda run -n astec applyTrsf -ref " + str(fusion) + " -interpolation nearest -iso " + str(
            voxel_size) + " " + str(mars) + " " + str(output_file))
        self.writeStepToJson(parameters, "downscale_mars", embryo_folder=".")

    def apply_downscaling(self,parameters):
        """

        :param parameters: 

        """
        downscale_contour = bool(parameters["apply_on_contour"])
        if not "embryo_name" in parameters:
            print("Please specify a embryo name")
            exit()
        if not "begin" in parameters:
            print("Please specify a begin point")
            exit()
        if not "EXP_FUSE" in parameters:
            print("Please specify a fuse exp")
            exit()
        if downscale_contour and not "EXP_CONTOUR" in parameters:
            print("Please specify a contour exp")
            exit()
        if downscale_contour and not "EXP_CONTOUR_DOWNSCALED" in parameters:
            print("Please specify a contour exp downscaled")
            exit()
        embryo_name = parameters["embryo_name"].replace('"', '').replace("'", "")
        embryo_folder = "."
        voxel_size = 0.6
        input_voxel_size = 0.3
        time_point = 0
        if "begin" in parameters:
            time_point = int(parameters["begin"])
        if not "resolution" in parameters:
            parameters["resolution"] = voxel_size
        else :
            voxel_size = float(parameters["resolution"])
        if not "input_resolution" in parameters:
            parameters["input_resolution"] = input_voxel_size
        else :
            input_voxel_size = float(parameters["input_resolution"])
        mars_path = os.path.join(embryo_folder,"MARS/"+embryo_name+"_mars_t{:03d}.nii".format(time_point))
        parameters["mars_file"] = mars_path
        mars_output_path = os.path.join(embryo_folder,"MARS0"+str(voxel_size).split(".")[1]+"/")
        parameters["output_folder"] = mars_output_path

        embryo_folder = "."
        input_folder = os.path.join(embryo_folder, "FUSE/FUSE_" + str(parameters["EXP_FUSE"]))
        fusion_output_dir = os.path.join(embryo_folder, "FUSE/FUSE_" + str(parameters["EXP_FUSE"]) + "_down0"+str(voxel_size).split(".")[1])
        input_fuse_template = os.path.join(fusion_output_dir,embryo_name+"_fuse_t{:03d}.nii".format(time_point))
        parameters["template_file"] = input_fuse_template
        print("     > Downscaling Fusion")
        self.downscale_folder(parameters)
        print("     > Downscaling Mars")
        self.downscale_mars(parameters)
        input_fuse_template = os.path.join(fusion_output_dir, embryo_name + "_fuse_t{:03d}.nii")
        parameters["template_file"] = input_fuse_template
        #Create function that downscale countours
        if downscale_contour:
            print("     > Downscaling Contours")
            self.downscale_contour_folder(parameters)

    def generate_init_naming_parameters(self, cell_count, xml_folder, xml_file, embryo_name):
        atlas_path = compute_atlas()
        now = datetime.now()
        parameters_name = "init_naming" + str(now.timestamp()).replace('.', '') + ".py"
        final_file = os.path.join(xml_folder.replace(str(embryo_name) + "/", ""), xml_file)
        txt = ""
        txt += "inputFile = '" + str(final_file) + "'" + "\n"
        txt += "outputFile = '" + str(final_file) + "'" + "\n"
        txt += "cell_number = " + str(cell_count) + "\n"
        txt += 'atlasFiles = '+str(atlas_path) + "\n"
        txt += "check_volume=False" + "\n"
        f = open(parameters_name, "w+")
        f.write(txt)
        f.close()
        return parameters_name

    def test_fusion(self,parameters,parameter_exploration=False,rerun=False,one_stack_only=False,stack_chosen=0):
        """

        :param parameters: 
        :param parameter_exploration:  (Default value = False)
        :param rerun:  (Default value = False)
        :param one_stack_only:  (Default value = False)
        :param stack_chosen:  (Default value = 0)

        """
        embryo_name = parameters["embryo_name"].replace('"', '').replace("'", "")
        parameters["fusion_xzsection_extraction"] = True
        # TESTS DEPENDENT PARAMETERS, DO NOT CHANGE
        #
        #
        #
        if rerun or parameter_exploration:
            parameters["fusion_strategy"] = "hierarchical-fusion"
            parameters["EXP_FUSE"] = "01_right_hierarchical"
            parameters["acquisition_orientation"] = "right"
            self.start_fusion(parameters,run_now=False, keep_temp=False,one_stack_only=one_stack_only,stack_chosen=stack_chosen)

            parameters["fusion_strategy"] = "direct-fusion"
            parameters["EXP_FUSE"] = "01_right_direct"
            parameters["acquisition_orientation"] = "right"
            self.start_fusion(parameters,run_now=False, keep_temp=False,one_stack_only=one_stack_only,stack_chosen=stack_chosen)

            parameters["fusion_strategy"] = "hierarchical-fusion"
            parameters["EXP_FUSE"] = "01_left_hierarchical"
            parameters["acquisition_orientation"] = "left"

            self.start_fusion(parameters,run_now=False, keep_temp=False,one_stack_only=one_stack_only,stack_chosen=stack_chosen)

            parameters["fusion_strategy"] = "direct-fusion"
            parameters["EXP_FUSE"] = "01_left_direct"
            parameters["acquisition_orientation"] = "left"

            self.start_fusion(parameters,run_now=False, keep_temp=False,one_stack_only=one_stack_only,stack_chosen=stack_chosen)
            self.start_running(thread_number=4)
        else :
            parameters["fusion_strategy"] = "hierarchical-fusion"
            parameters["EXP_FUSE"] = "01_test"
            parameters["acquisition_orientation"] = "right"
            self.start_fusion(parameters, keep_temp=False,one_stack_only=one_stack_only,stack_chosen=stack_chosen)


    def start_fusion(self,parameters,run_now=True,keep_temp=False,channel_count=1,one_stack_only=False,stack_chosen=0):
        """

        :param parameters: 
        :param run_now:  (Default value = True)
        :param keep_temp:  (Default value = False)
        :param channel_count:  (Default value = 1)
        :param one_stack_only:  (Default value = False)
        :param stack_chosen:  (Default value = 0)

        """
        omero_config_file = get_omero_config(parameters)
        embryo_name = parameters["embryo_name"].replace('"','').replace("'","")

        begin = parameters["begin"]
        end = parameters["end"]
        real_parameters = {}
        real_parameters["acquisition_resolution"] = (.195, .195, 1.)
        real_parameters["target_resolution"] = .3
        real_parameters["result_image_suffix"] = 'nii'
        real_parameters["acquisition_slit_line_correction"] = True
        real_parameters["acquisition_cropping_opening"] = 2
        real_parameters["acquisition_cropping"] = False
        real_parameters["raw_crop"] = True
        real_parameters["fusion_crop"] = True

        real_parameters["fusion_preregistration_compute_registration"] = True
        real_parameters["fusion_preregistration_normalization"] = False
        real_parameters["fusion_registration_normalization"] = False
        real_parameters["fusion_stack_preregistration_normalization"] = False
        real_parameters["fusion_stack_registration_normalization"] = False
        real_parameters["fusion_xzsection_extraction"] = False

        # DATA DEPENDENT PARAMETERS , SHOUD NOT CHANGE IF UPDATED ONCE
        #
        #
        #

        real_parameters["DIR_RAWDATA"] = "RAWDATA"
        if (one_stack_only and stack_chosen == 0) or not one_stack_only:
            real_parameters["DIR_LEFTCAM_STACKZERO"] = "stack_0_channel_0_obj_left"
            real_parameters["DIR_RIGHTCAM_STACKZERO"] = "stack_0_channel_0_obj_right"
        if (one_stack_only and stack_chosen == 1) or not one_stack_only:
            real_parameters["DIR_LEFTCAM_STACKONE"] = "stack_1_channel_0_obj_left"
            real_parameters["DIR_RIGHTCAM_STACKONE"] = "stack_1_channel_0_obj_right"
        if channel_count > 1:
            if (one_stack_only and stack_chosen == 0) or not one_stack_only:
                real_parameters["DIR_LEFTCAM_STACKZERO_CHANNEL_1"] = "stack_0_channel_1_obj_left"
                real_parameters["DIR_RIGHTCAM_STACKZERO_CHANNEL_1"] = "stack_0_channel_1_obj_right"
            if (one_stack_only and stack_chosen == 1) or not one_stack_only:
                real_parameters["DIR_LEFTCAM_STACKONE_CHANNEL_1"] = "stack_1_channel_1_obj_left"
                real_parameters["DIR_RIGHTCAM_STACKONE_CHANNEL_1"] = "stack_1_channel_1_obj_right"
        if channel_count > 2:
            if (one_stack_only and stack_chosen == 0) or not one_stack_only:
                real_parameters["DIR_LEFTCAM_STACKZERO_CHANNEL_2"] = "stack_0_channel_2_obj_left"
                real_parameters["DIR_RIGHTCAM_STACKZERO_CHANNEL_2"] = "stack_0_channel_2_obj_right"
            if (one_stack_only and stack_chosen == 1) or not one_stack_only:
                real_parameters["DIR_LEFTCAM_STACKONE_CHANNEL_2"] = "stack_1_channel_2_obj_left"
                real_parameters["DIR_RIGHTCAM_STACKONE_CHANNEL_2"] = "stack_1_channel_2_obj_right"
        if channel_count > 3:
            if (one_stack_only and stack_chosen == 0) or not one_stack_only:
                real_parameters["DIR_LEFTCAM_STACKZERO_CHANNEL_3"] = "stack_0_channel_3_obj_left"
                real_parameters["DIR_RIGHTCAM_STACKZERO_CHANNEL_3"] = "stack_0_channel_3_obj_right"
            if (one_stack_only and stack_chosen == 1) or not one_stack_only:
                real_parameters["DIR_LEFTCAM_STACKONE_CHANNEL_3"] = "stack_1_channel_3_obj_left"
                real_parameters["DIR_RIGHTCAM_STACKONE_CHANNEL_3"] = "stack_1_channel_3_obj_right"
        real_parameters["acquisition_leftcam_image_prefix"] = "Cam_Left_000"
        real_parameters["acquisition_rightcam_image_prefix"] = "Cam_Right_000"
        real_parameters["fusion_weighting"] = "guignard"
        real_parameters["fusion_strategy"] = 'hierarchical-fusion'


        real_parameters["acquisition_orientation"] = 'right'
        real_parameters["acquisition_mirrors"] = False
        real_parameters["acquisition_leftcamera_z_stacking"] = 'direct'
        for key_param in parameters:
            real_parameters[key_param] = parameters[key_param]
        if not "EXP_FUSE" in real_parameters:
            real_parameters["EXP_FUSE"] = "01"
            if channel_count == 2:
                real_parameters["EXP_FUSE"] = ['01','02']
            if channel_count == 3:
                real_parameters["EXP_FUSE"] = ['01','02','03']
            if channel_count > 3:
                print("Can't fuse more than 3 channels ! ")
                exit()
        self.add_to_run("FUSE", ".", embryo_name, begin, real_parameters, end_time=end, compress_result=False,omero_result=(omero_config_file is not None),omero_config_file=omero_config_file,keep_temp=keep_temp)
        if run_now:
            self.start_running(thread_number=1)
            if isinstance(real_parameters["EXP_FUSE"],list):
                splitted_fuse = real_parameters["EXP_FUSE"]
            else :
                splitted_fuse = real_parameters["EXP_FUSE"].replace("'", "").replace('"', '').replace("[", "").replace("]",
                                                                                                                   "").split(
                    ",")
            logFolder = "./FUSE/FUSE_" + splitted_fuse[0] + "/LOGS/"
            self.writeStepToJson(real_parameters, "fusion", ".", logFolder=logFolder)
        return real_parameters

    def compute_fusion_movie(self,parameters):
        """

        :param parameters: 

        """
        real_parameters = {}
        real_parameters["EXP_INTRAREG"] = '01_TEST'
        real_parameters["intra_registration_movie_fusion_images"] = True
        embryo_name = parameters["embryo_name"].replace('"','').replace("'","")

        begin = parameters["begin"]
        end = parameters["end"]
        for key in parameters:
            real_parameters[key] = parameters[key]

        try:
            self.add_to_run("INTRAREG", ".", embryo_name, begin, real_parameters, end_time=end, compress_result=False)

            self.start_running(thread_number=1)
            logFolder = "./INTRAREG/INTRAREG_" + str(real_parameters["EXP_INTRAREG"]).replace("'", "").replace('"', '') + "/LOGS/"
            self.writeStepToJson(real_parameters,"intrareg_movie",".",logFolder=logFolder)

            compute_video_from_movie(embryo_name, real_parameters["EXP_INTRAREG"], real_parameters["EXP_FUSE"])
        except Exception as e:
            strlog = traceback.format_exc()
            print("Error fusion movie : " + str(strlog))
    def final_fusion(self, parameters,one_stack_only=False,stack_chosen=0):
        """

        :param parameters: 
        :param one_stack_only:  (Default value = False)
        :param stack_chosen:  (Default value = 0)

        """
        embryo_name = parameters["embryo_name"].replace('"','').replace("'","")
        number_of_channels = 1
        if "number_of_channels" in parameters:
            try :
                number_of_channels = int(parameters["number_of_channels"])
            except Exception as e:
                strlog = traceback.format_exc()
                print("Error number of channel is not an integer: " + str(strlog))
        if not "EXP_FUSE" in parameters:
            parameters["EXP_FUSE"] = "01"
            if number_of_channels == 2:
                parameters["EXP_FUSE"] = ['01','02']
            if number_of_channels == 3:
                parameters["EXP_FUSE"] = ['01','02','03']
            if number_of_channels > 3:
                print("Can't fuse more than 3 channels ! ")
                exit()
        real_parameters = self.start_fusion(parameters,channel_count=number_of_channels,one_stack_only=one_stack_only,stack_chosen=stack_chosen)
        try :
            self.compute_fusion_movie(real_parameters)
        except Exception as e:
            strlog = traceback.format_exc()
            print("Error during movie computation : "+str(strlog))
        try :
            plot_fusion_intensity_profile(embryo_name,str(real_parameters["EXP_FUSE"]))

        except Exception as e:
            strlog = traceback.format_exc()
            print("Error during fusion signal plot: "+str(strlog))

        try:
            print("PLotting intensities"
                  "")
            self.plot_signal_to_noise(embryo_name, real_parameters,one_stack_only=one_stack_only,stack_chosen=stack_chosen)
        except Exception as e:
            strlog = traceback.format_exc()
            print("Error during signal plot: "+str(strlog))


    def start_mars(self,parameters):
        """

        :param parameters: 

        """
        use_contour = parameters["use_contour"]
        normalize_images = parameters["apply_normalisation"]
        omero_config_file = get_omero_config(parameters)
        embryo_name = parameters["embryo_name"].replace('"','').replace("'","")
        embryo_dir ="."
        begin = int(parameters["begin"])
        end = int(parameters["end"])

        voxel_size = parameters["resolution"]
        real_parameters = {}

        real_parameters["sigma_TV"] = 4.5
        real_parameters["result_image_suffix"] = "nii"
        real_parameters["intensity_enhancement"] = 'gace'

        if use_contour:
            real_parameters["EXP_CONTOUR"] = "RELEASE_" + str(voxel_size).split(".")[1]
            real_parameters["outer_contour_enhancement"] = 'from_contour_image'
        if normalize_images:
            normalisation = 1000
            if "normalisation" in parameters:
                normalisation = parameters["normalisation"]
            real_parameters["enhancement_normalization_max_value"] = normalisation
            real_parameters["enhancement_transformation"] = "normalization_to_u16"
            real_parameters["normalization_max_value"] = normalisation
            real_parameters["intensity_transformation"] = "normalization_to_u16"
        user = None
        if "user" in parameters:
            user = parameters["user"]
        for key_param in parameters:
            real_parameters[key_param] = parameters[key_param]
        self.add_to_run("MARS", ".", embryo_name, begin, real_parameters, end_time=end, compress_result=False,omero_result=(omero_config_file is not None),omero_config_file=omero_config_file,keep_temp=True)
        self.start_running(thread_number=1)
        real_parameters["uploaded_to_omero"] = (omero_config_file is not None)
        logFolder = "./SEG/SEG_" + str(real_parameters["EXP_SEG"]).replace("'", "").replace('"', '') + "/LOGS/"
        self.writeStepToJson(real_parameters,"mars",".",logFolder=logFolder)

        return real_parameters

    def test_mars(self,parameters):
        """

        :param parameters: 

        """
        parameters["EXP_SEG"] = "mars_add"
        parameters["reconstruction_images_combination"] = "addition"
        real_parameters = self.start_mars(parameters)

        real_parameters["EXP_SEG"] = "mars_max"
        real_parameters["reconstruction_images_combination"] = "maximum"
        self.start_mars(real_parameters)

    def test_segmentation(self,parameters):
        """

        :param parameters: 

        """
        # TESTS DEPENDENT PARAMETERS, DO NOT CHANGE
        #
        #
        #
        if True:
            parameters["EXP_SEG"] = "test_addition_glace"
            parameters["reconstruction_images_combination"] = "addition"
            parameters["intensity_enhancement"] = "glace"
            self.start_segmentation(parameters,run_now=True)
        if True:
            logFolder = "./SEG/SEG_" + str(parameters["EXP_SEG"]).replace("'", "").replace('"', '') + "/LOGS/"
            parameters2 = parameters
            parameters2["EXP_SEG"] = "test_addition_gace"
            parameters2["reconstruction_images_combination"] = "addition"
            parameters2["intensity_enhancement"] = "gace"
            self.start_segmentation(parameters2,run_now=False)
            logFolder2 = "./SEG/SEG_" + str(parameters2["EXP_SEG"]).replace("'", "").replace('"', '') + "/LOGS/"

            parameters3 = parameters
            parameters3["EXP_SEG"] = "test_maximum_glace"
            parameters3["reconstruction_images_combination"] = "maximum"
            parameters3["intensity_enhancement"] = "glace"
            logFolder3 = "./SEG/SEG_" + str(parameters3["EXP_SEG"]).replace("'", "").replace('"', '') + "/LOGS/"
            self.start_segmentation(parameters3,run_now=False)
            parameters4 = parameters
            parameters4["EXP_SEG"] = "test_maximum_gace"
            parameters4["reconstruction_images_combination"] = "maximum"
            parameters4["intensity_enhancement"] = "gace"

            self.start_segmentation(parameters4,run_now=False)
            logFolder4 = "./SEG/SEG_" + str(parameters4["EXP_SEG"]).replace("'", "").replace('"', '') + "/LOGS/"

            self.start_running(thread_number=4)
            self.writeStepToJson(parameters,"segmentation_test",".",logFolder=logFolder)
            self.writeStepToJson(parameters2,"segmentation_test",".",logFolder=logFolder2)
            self.writeStepToJson(parameters3,"segmentation_test",".",logFolder=logFolder3)
            self.writeStepToJson(parameters4,"segmentation_test",".",logFolder=logFolder4)

        # Embryo dependant parameters

        parameters["EXP_SEG"] = 'test_maximum_gace'
        parameters["EXP_POST"] = 'test_maximum_gace'

        self.start_post_correction(parameters,run_now=False)
        parameters2 = parameters
        parameters2["EXP_SEG"] = 'test_addition_glace'
        parameters2["EXP_POST"] = 'test_addition_glace'

        self.start_post_correction(parameters2,run_now=False)
        parameters3 = parameters
        parameters3["EXP_SEG"] = 'test_addition_gace'
        parameters3["EXP_POST"] = 'test_addition_gace'

        self.start_post_correction(parameters3,run_now=False)

        parameters4 = parameters
        parameters4["EXP_SEG"] = 'test_maximum_glace'
        parameters4["EXP_POST"] = 'test_maximum_glace'

        self.start_post_correction(parameters4,run_now=False)


        if True:
            self.start_running(thread_number=4)
        self.compute_graphs_test_segmentation(parameters["embryo_name"], parameters["begin"], parameters["end"])
        logFolder = "./POST/POST_" + str(parameters["EXP_POST"]).replace("'", "").replace('"', '') + "/LOGS/"
        self.writeStepToJson(parameters, "post_correction_test", ".", logFolder=logFolder)
        logFolder2 = "./POST/POST_" + str(parameters2["EXP_POST"]).replace("'", "").replace('"', '') + "/LOGS/"
        self.writeStepToJson(parameters2,"post_correction_test",".",logFolder=logFolder2)
        logFolder3 = "./POST/POST_" + str(parameters3["EXP_POST"]).replace("'", "").replace('"', '') + "/LOGS/"
        self.writeStepToJson(parameters3,"post_correction_test",".",logFolder=logFolder3)
        logFolder4 = "./POST/POST_" + str(parameters4["EXP_POST"]).replace("'", "").replace('"', '') + "/LOGS/"
        self.writeStepToJson(parameters4,"post_correction_test",".",logFolder4)


    def start_segmentation(self,parameters,run_now=True):
        """

        :param parameters: 
        :param run_now:  (Default value = True)

        """
        use_contour = parameters["use_contour"]
        normalize_images = parameters["apply_normalisation"]
        omero_config_file = get_omero_config(parameters)
        voxel_size = parameters["resolution"]

        MARS_PATH = parameters["mars_path"]
        embryo_name = parameters["embryo_name"].replace("'","").replace('"','')
        begin = int(parameters["begin"])
        end = int(parameters["end"])

        real_parameters = {}

        real_parameters["sigma_TV"] = 4.5
        real_parameters["result_image_suffix"] = "nii"
        real_parameters["intensity_enhancement"] = 'gace'
        real_parameters["EXP_FUSE"] = "01"
        if use_contour:
            real_parameters["EXP_CONTOUR"] = "RELEASE_" + str(voxel_size).split(".")[1]
            real_parameters["outer_contour_enhancement"] = "from_contour_image"
        if normalize_images:
            normalisation = 1000
            if "normalisation" in parameters:
                normalisation = parameters["normalisation"]
            real_parameters["enhancement_normalization_max_value"] = normalisation
            real_parameters["enhancement_transformation"] = "normalization_to_u16"
            real_parameters["normalization_max_value"] = normalisation
            real_parameters["intensity_transformation"] = "normalization_to_u16"

        for key_param in parameters:
            real_parameters[key_param] = parameters[key_param]
        self.add_to_run("SEG", ".", embryo_name, begin, real_parameters, end_time=end, compress_result=False,
                           mars_path=MARS_PATH,omero_result=(omero_config_file is not None),omero_config_file=omero_config_file)
        if run_now:
            self.start_running(thread_number=1)
            real_parameters["uploaded_on_omero"] = (omero_config_file is not None)
            logFolder = "./SEG/SEG_" + str(parameters["EXP_SEG"]).replace("'", "").replace('"', '') + "/LOGS/"
            self.writeStepToJson(real_parameters,"segmentation",".",logFolder=logFolder)
            #self.segmentation_parameters(real_parameters)
        return real_parameters

    def start_post_correction(self,parameters,run_now=True):
        """

        :param parameters: 
        :param run_now:  (Default value = True)

        """
        embryo_name = parameters["embryo_name"].replace('"','').replace("'","")
        omero_config_file = get_omero_config(parameters)
        begin = int(parameters["begin"])
        end = int(parameters["end"])
        voxel_size = parameters["resolution"]
        real_parameters = {}
        real_parameters["EXP_POST"] = '01'
        real_parameters["intra_registration_resolution"] = voxel_size
        real_parameters["test_branch_length"] = True
        real_parameters["test_early_division"] = True
        real_parameters["test_volume_correlation"] = True
        real_parameters["test_postponing_division"] = True
        real_parameters["result_image_suffix"] = 'nii'
        for key_param in parameters:
            real_parameters[key_param] = parameters[key_param]
        self.add_to_run("POST", ".", embryo_name, begin, real_parameters, end_time=end, compress_result=False,omero_result=(omero_config_file is not None),omero_config_file=omero_config_file)
        if run_now:
            self.start_running(thread_number=1)
            real_parameters["uploaded_on_omero"] = (omero_config_file is not None)
            logFolder = "./POST/POST_" + str(parameters["EXP_POST"]).replace("'", "").replace('"', '') + "/LOGS/"
            self.writeStepToJson(real_parameters,"post_correction",".",logFolder=logFolder)
            #self.post_correction_parameters(parameters)
            try :
                self.compute_graphs_post(embryo_name, begin, end , [parameters["EXP_POST"]])
            except :
                strlog = traceback.format_exc()
                print("Error during computation of the Post correction graphs"+ str(strlog))
        return real_parameters


    def apply_intrareg(self,parameters):
        """

        :param parameters: 

        """
        omero_config_file = get_omero_config(parameters)
        embryo_name = parameters["embryo_name"].replace("'","").replace('','"')
        begin = parameters["begin"]
        end = parameters["end"]
        real_parameters = {}
        real_parameters["EXP_INTRAREG"] = "01"
        real_parameters["delta"] = 1
        real_parameters["raw_delay"] = 0
        real_parameters["intra_registration_template_type"] = 'POST-SEGMENTATION'
        real_parameters["intra_registration_template_threshold"] = 2
        real_parameters["intra_registration_margin"] = 20
        real_parameters["intra_registration_resample_post_segmentation_images"] = True
        real_parameters["intra_registration_resample_segmentation_images"] = False
        real_parameters["intra_registration_movie_post_segmentation_images"] = True
        real_parameters["intra_registration_movie_segmentation_images"] = False
        real_parameters["intra_registration_rebuild_template"] = True
        for key_param in parameters:
            real_parameters[key_param] = parameters[key_param]

        # PRODUCTION PARAMETERS, UPDATE WITH THE TEST CHOSEN PREVIOUSLY
        #
        #
        #

        try:
            self.add_to_run("INTRAREG", ".", embryo_name, begin, real_parameters, end_time=end, compress_result=False)

            self.start_running(thread_number=1)
            real_parameters["uploaded_on_omero"] = (omero_config_file is not None)
            logFolder = "./INTRAREG/INTRAREG_" + str(real_parameters["EXP_INTRAREG"]).replace("'", "").replace('"', '') + "/LOGS/"
            self.writeStepToJson(real_parameters, "intraregistration", ".",logFolder=logFolder)
        except Exception as e:
            strlog = traceback.format_exc()
            print("Error during seg intrareg: " + str(strlog))
        if omero_config_file is not None:
            try:
                intra_folder = "INTRAREG/INTRAREG_" + str(parameters["EXP_INTRAREG"]) + "/POST/POST_" + str(
                                                parameters["EXP_POST"])
                self.upload_on_omero(omero_config_file, embryo_name, "INT_POST_" + str(parameters["EXP_POST"]),
                                        intra_folder, include_logs=True)
            except Exception as e:
                strlog = traceback.format_exc()
                print("Error during intrareg upload: " + str(strlog))
            try:
                intra_fuse_folder = "INTRAREG/INTRAREG_" + str(
                    parameters["EXP_INTRAREG"]) + "/FUSE/FUSE_" + str(parameters["EXP_FUSE"])
                self.upload_on_omero(omero_config_file, embryo_name, "INT_FUSE_" + str(parameters["EXP_FUSE"]),
                                        intra_fuse_folder, include_logs=True)
            except Exception as e:
                strlog = traceback.format_exc()
                print("Error during fuse upload: " + str(strlog))
            try:
                rec = None
                if "EXP_RECONSTRUCTION" in real_parameters:
                    rec = "REC_" + real_parameters["EXP_RECONSTRUCTION"].replace('"', '').replace("'", "")
                else:
                    if "EXP_SEG" in real_parameters:
                        rec = "REC_" + real_parameters["EXP_SEG"].replace('"', '').replace("'", "")
                intra_rec_folder = "INTRAREG/INTRAREG_" + str(
                    parameters["EXP_INTRAREG"]) + "/REC-MEMBRANE/"+rec
                self.upload_on_omero(omero_config_file, embryo_name, "INT_"+rec,intra_rec_folder, include_logs=False)
            except Exception as e:
                strlog = traceback.format_exc()
                print("Error during fuse upload: " + str(strlog))
        return real_parameters

    def compute_properties(self,parameters):
        """

        :param parameters: 

        """
        embryo_name = parameters["embryo_name"]
        begin = parameters["begin"]
        end = parameters["end"]
        try:
            self.add_to_run("PROPERTIES", ".", embryo_name, begin, parameters, end_time=end, compress_result=False)
            self.start_running(thread_number=1)
            logFolder = "./INTRAREG/INTRAREG_" + str(parameters["EXP_INTRAREG"]).replace("'", "").replace('"', '') + "/LOGS/"
            self.writeStepToJson(parameters,"embryo_properties",".",logFolder=logFolder)
        except Exception as e:
            strlog = traceback.format_exc()
            print("Error during seg properties: " + str(strlog))
        try :
            self.name_embryo(parameters)
        except Exception as e:
            strlog = traceback.format_exc()
            print("Error during naming : " + str(strlog))
        try :
            embryo_name = embryo_name.replace('"', '').replace("'", "")
            lineage_path = "./INTRAREG/INTRAREG_" + str(parameters["EXP_INTRAREG"]) + "/POST/POST_" + parameters[
                "EXP_POST"] + "/"
            lineage_name = embryo_name + "_intrareg_post_lineage.xml"
            lineage_complete_path = os.path.join(lineage_path,lineage_name)
            generate_lineage_comparison(lineage_complete_path,begin)
        except Exception as e:
            strlog = traceback.format_exc()
            print("Error during lineage distance : " + str(strlog))

    def prod_segmentation(self,parameters):
        """

        :param parameters: 

        """
        parameters["embryo_name"] = parameters["embryo_name"].replace('"','').replace("'","")
        if "begin" in parameters:
            parameters["begin"] = int(parameters["begin"])
        if "end" in parameters:
            parameters["end"] = int(parameters["end"])
        if not "EXP_SEG" in parameters:
            parameters["EXP_SEG"] = '01'
        real_parameters = self.start_segmentation(parameters)

        # Embryo dependant parameters
        if not "EXP_POST" in real_parameters:
            real_parameters["EXP_POST"] = '01'
        real_parameters = self.start_post_correction(real_parameters)
        if not "EXP_INTRAREG" in real_parameters:
            real_parameters["EXP_INTRAREG"] = '01'
        real_parameters = self.apply_intrareg(real_parameters)

        self.compute_properties(real_parameters)

    def upload_data(self,parameters):
        """

        :param parameters: 

        """
        omero_config_file = get_omero_config(parameters)
        project_name = parameters["project_name"]
        dataset_name = parameters["dataset_name"]
        input_folder = parameters["input_folder"]
        if omero_config_file is None:
            print("OMERO config file is not bound, unable to upload")
            exit()
        if not os.path.isfile(omero_config_file):
            print("Unable to find OMERO config file , unable to upload")
            exit()
        self.upload_on_omero(omero_config_file, project_name, dataset_name, input_folder,
                                include_logs=True)
    def printEmbryoMetadata(self):
        """ """
        printMetadata("./")