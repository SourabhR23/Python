<h1>Match Highlights Maker</h1>

In this project, <br>
Libraries/modules used: Pandas, moviepy, pyloudnorm.
1. Pandas is used to read .CSV file.
2. moviepy is used to break videos and to convert them into audio(.WAV file) and concatenate the broken videos.
3. pyloudnorm is used to measure the loudness of each broken videos.

Project Description:<br>
The general idea of the project is to create the hightlights video from a particular match.
For this project, a Tennis match was taken under consideration.

Procedure:<br>
1. The tennis match video was selected.
2. A .CSV file containing the start and end minutes of each set was noted.
3. Depending on entries from .CSV file, by using moviepy library, the main match video was broken into number of videos i.e the start and end minutes of each set and was saved into output folder.
4. These broken videos was then converted into audio file i.e .WAV file.
5. By using pyloudnorm library, loudness of each broken video was calculated. (Loudness created by clapping of hands after each set won was taken under considerations)
6. Videos were arranged in descending order of their loudness.
7. The input was taken from user, of total number of videos user wants in the highlights video and according to that those many videos were considered and then they were 
concatenated using moviepy and final highlights video was created.
9. The broken video files and audio files are deleted from output folder and final highlights video is saved in output folder.
