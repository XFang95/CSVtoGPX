import pandas as pd
from xml.etree.ElementTree import Element, SubElement, ElementTree
from math import radians, sin, cos, sqrt, atan2


def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in meters
    R = 6371000
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance / 1000  # Return distance in kilometers


def convert_csv_to_gpx(csv_file_path, output_gpx_path):
    # Load the CSV file and sort by time
    df = pd.read_csv(csv_file_path)
    df['dataTime'] = pd.to_datetime(df['dataTime'], unit='s')
    df = df.sort_values(by='dataTime').reset_index(drop=True)

    # Create the root GPX element with the correct namespace
    gpx = Element('gpx', version="1.1", creator="Michael", xmlns="http://www.topografix.com/GPX/1/1")

    # Create a track element
    trk = SubElement(gpx, 'trk')
    name = SubElement(trk, 'name')
    name.text = "Or2k"

    # Iterate through the DataFrame
    for i in range(len(df)):
        current_row = df.iloc[i]
        if i > 0:
            previous_row = df.iloc[i - 1]
            time_diff_prev = (current_row['dataTime'] - previous_row['dataTime']).total_seconds()  # in seconds
            distance_prev = haversine(current_row['latitude'], current_row['longitude'], previous_row['latitude'],
                                      previous_row['longitude'])
        else:
            time_diff_prev = None
            distance_prev = None

        if i < len(df) - 1:
            next_row = df.iloc[i + 1]
            time_diff_next = (next_row['dataTime'] - current_row['dataTime']).total_seconds()  # in seconds
            distance_next = haversine(current_row['latitude'], current_row['longitude'], next_row['latitude'],
                                      next_row['longitude'])
        else:
            time_diff_next = None
            distance_next = None

        # Determine whether to create a dedicated segment or link points
        if (time_diff_prev is not None and time_diff_prev <= 60 and distance_prev <= 1):
            # Link to previous point if criteria are met
            trkseg = SubElement(trk, 'trkseg')
            trkpt_start = SubElement(trkseg, 'trkpt', lat=f"{previous_row['latitude']:.6f}",
                                     lon=f"{previous_row['longitude']:.6f}")
            trkpt_end = SubElement(trkseg, 'trkpt', lat=f"{current_row['latitude']:.6f}",
                                   lon=f"{current_row['longitude']:.6f}")

        if (time_diff_next is not None and time_diff_next <= 60 and distance_next <= 1):
            # Link to next point if criteria are met
            trkseg = SubElement(trk, 'trkseg')
            trkpt_start = SubElement(trkseg, 'trkpt', lat=f"{current_row['latitude']:.6f}",
                                     lon=f"{current_row['longitude']:.6f}")
            trkpt_end = SubElement(trkseg, 'trkpt', lat=f"{next_row['latitude']:.6f}",
                                   lon=f"{next_row['longitude']:.6f}")

        if ((time_diff_prev is None or time_diff_prev > 60 or distance_prev > 1) and
                (time_diff_next is None or time_diff_next > 60 or distance_next > 1)):
            # Create a dedicated segment for the current point
            trkseg = SubElement(trk, 'trkseg')
            trkpt = SubElement(trkseg, 'trkpt', lat=f"{current_row['latitude']:.6f}",
                               lon=f"{current_row['longitude']:.6f}")
            trkpt = SubElement(trkseg, 'trkpt', lat=f"{current_row['latitude']:.6f}",
                               lon=f"{current_row['longitude']:.6f}")

    # Save the GPX content to a file
    ElementTree(gpx).write(output_gpx_path, encoding='utf-8', xml_declaration=True)
    print(f"GPX file saved to {output_gpx_path}")


if __name__ == "__main__":
    # Replace these with your actual file paths
    csv_file_path = 'backUpData.csv'  # Example: 'data.csv'
    output_gpx_path = 'output12.gpx'

    convert_csv_to_gpx(csv_file_path, output_gpx_path)
