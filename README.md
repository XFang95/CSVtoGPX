This project converts the CSV files exported by Footprint to GPX files that can be imported to Fog of World.

To get the CSV files, go to files -> 一生足迹 -> backup, and copy the backUpData.csv file from the folder.

The csvtogpx.py script will convert the individual points as separate "segments" and will show as dots in Fog of World.

The csvtogpxseg.py script will connect the adjacent dots based on time series based on time (within 60s with adjacent dots) and space (within 1.0 km with adjacent dots). The criteria can be adjusted based on your setting in the Footprint app.

This code is built by ChatGPT and the full conversation can be found in the following link
https://chatgpt.com/share/9327f9d6-103c-4bde-bd1b-63bf77553052 

Here is a comparison between Footprint, the point format from csvtogpx.py, and the segment format from csvtogpxseg.py.


![IMG_8574](https://github.com/user-attachments/assets/881634f1-0650-42b0-835a-211e95b7a954)

![IMG_8572](https://github.com/user-attachments/assets/d5b5e6c5-6492-439f-bc94-bfc6d15f16b3)

![IMG_8571](https://github.com/user-attachments/assets/a6e72016-e2dc-46b9-90f9-3ea63d71915e)
