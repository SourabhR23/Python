from moviepy.editor import *
import os
import pandas as pd
from pandas.io.parsers import ParserError
import soundfile as sf
import pyloudnorm as pyln

def csv_file_open():
    '''
    This function take CSV file from user.
    '''
    while True:
        csv_input = input("Enter the path of CSV/Excel file: ")
        print('----------------------------------------------------------------------')
        if csv_input == "":
            print(">>> An empty input is not valid.\n")
        else:    
            try:
                if not (os.path.exists(csv_input) and csv_input.endswith(".csv")):
                    raise FileNotFoundError
            except (OSError, FileNotFoundError):
                print(">>> File not found." + "\nPlease try again...\n")
            except ParserError:
                print(">>> File with wrong Extension." + "\nPlease try again...\n")
            else:
                return csv_input

def video_file_open():
    '''
    This function takes input video file from user.
    '''
    while True:
        video_file = input("\nEnter path of Video File: ")
        print('----------------------------------------------------------------------')
        if video_file == "":
            print(">>> An empty input is not valid.\n")
        try:
            if not (os.path.exists(video_file) and video_file.endswith(".mp4")):
                raise FileNotFoundError
        except (FileNotFoundError, OSError, IOError):
            print("Not Valid ! Please check that you entered the correct path\n")
        else:
            return video_file
            break
            
def no_of_highlights():
    '''
    This function take number of highlight that user want.
    '''
    while True:
        tp = input("\nHow many top moments do you want? ")
        print('----------------------------------------------------------------------')
        if tp == "":
            print(">>> An empty input is not valid\n")
        elif tp == '0':
            print(">>> 0 is not accepted" + "\nPlease try again...\n")
        else:
            try:
                tp = int(tp)
                return tp
                break
            except ValueError:
                print(">>> No valid integer!" + "\nPlease try again ...\n")

def output_path():
    '''
    This  function takes output path from user.
    '''
    while True:
        final_save_path = input("\nEnter path of Folder to save video: ")
        print('----------------------------------------------------------------------')
        if final_save_path == "":
            print(">>> An empty input is not valid")
        elif os.path.isdir(final_save_path):
            return final_save_path
            break
        else:
            print(">>> Directory not found" + "\nPlease try again...")  
            
def name_video():
    '''
    This function takes name from user for the video.
    '''
    while True:
        video_name = input("\nEnter name you want for your video: ")
        print('----------------------------------------------------------------------')
        if video_name == "":
            print(">>> An empty input is not valid")
        else:
            return video_name
            break
            
def break_video_files(csv_input, video_file, final_save_path):
    
    # Open CSV/Excel File
    file = pd.read_csv(csv_input)
    l1 = []
    l2 = []
    num = 0
    
    for i in file.index:

        # Open Video file
        clip = VideoFileClip(video_file).subclip(file['start time'][i], file['end time'][i])

        # Breaking Video file into small video files
        clip.write_videofile(final_save_path + "\\" + "output_%s.mp4"% num)
        
        # Convert into Audio file 
        clip.audio.write_audiofile(final_save_path + "\\" + "output_%s.wav"% num)

        clip.close()

        # Calculate loudness
        data, rate = sf.read(final_save_path + "\\" + "output_%s.wav"% num)
        meter = pyln.Meter(rate) 
        loudness = meter.integrated_loudness(data)

        l1.append(loudness)
        l3 = str(num) + ".wav"
        l2.append(l3) 

        num += 1
    
    # Creating list of all broken videos and their corresponding loudness
    # returns tuple combinations [(wav file, loudness)] in list
    l4 = list(zip(l2, l1))
     
    sort_list = list(sorted(l4, key = lambda i:i[1], reverse = True))
    
    # List sorted based on loudness (descending order)
    final_list = sorted(sort_list[0:tp])
    print(final_list)
    print()
    
    new_list =[] 
    for j in range(len(final_list)):
        new_list.append(final_list[j][0])
    
    vid_num_list = []
    for i in new_list:
        wav_file = i.split(('.'))
        for nums in wav_file:
            if nums.isdigit():
                vid_num_list.append(nums)
    
    # Listing out videos from sorted list as per user's no. of highlights
    new_video_list = []
    for i in vid_num_list:
        new_video_list.append(VideoFileClip(os.path.join(final_save_path, "output_%s.mp4"%i)))
        
    # Concatenates all the highlights 
    final_clip = concatenate_videoclips(new_video_list)
    return final_clip

def final_output(final_clip, video_name):
    """
    This  function gives final video path
    """
    # creates final highlights video
    final_clip.write_videofile(os.path.join(final_save_path, (video_name + ".mp4")))
    # get path of video file
    final_clip_path = os.path.abspath(final_save_path)
    # checking if directory is valid or not
    clip_dir_path = os.path.dirname(final_clip_path)
    # if directory is valid
    # returns path of folder and name of highlights video
    if os.path.isdir(clip_dir_path):
        print("Your highlights video is located in {0} with name {1} ".format(final_clip_path, video_name))

def clean_files(final_save_path):
    """
    This function removes the generated output.mp4 and output.wav files from our directory.
    """
    dir_files = os.listdir(final_save_path)
    for dir_file in dir_files:
        # reomves the temporary files which are created for project
        if dir_file.startswith("output_"):
            os.remove(os.path.join(final_save_path, dir_file))
    print("**Thanks For Using Application**")
    return

if __name__ == "__main__":
    
    print("Welcome\n")
    
    # Runs function to take and open CSV/Excel file
    csv_input = csv_file_open()
    # Runs function to take and open video file
    video_file = video_file_open()
    # Take number of highlights from user
    tp = no_of_highlights()
    # Runs function to ask user for path to save final video
    final_save_path = output_path()
    # Enter name for final highlights video
    video_name = name_video()
    # Breaking of videos and converting them into audios and calculating loudness
    final_clip = break_video_files(csv_input, video_file, final_save_path)
    # Runs to show output to user
    final_output(final_clip, video_name)
    # Runs to clean our temporary files in output folder
    clean_files(final_save_path)
