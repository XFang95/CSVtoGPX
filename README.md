This project convert the CSV files exported by Footprint to GPX files that can be imported to Fog of World.

To get the CSV files, go to files -> 一生足迹, and copy the backUpData.csv file from the folder.

The csvtogpx.py script will convert the indivisual points as sperate "segments" and will show as dots in Fog of World.

The csvtogpxseg.py script will connect the adjacent dots based on time series based on time (within 60s with adjacent dots) and space (within 1.0 km with adjacent dots). The criteria can be adjusted based on your setting in the Footprint app.
