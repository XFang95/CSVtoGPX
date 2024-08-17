import pandas as pd
from xml.etree.ElementTree import Element, SubElement, ElementTree


def convert_csv_to_gpx(csv_file_path, output_gpx_path):
    # Load the CSV file
    df = pd.read_csv(csv_file_path)

    # Create the root GPX element with the correct namespace
    gpx = Element('gpx', version="1.1", creator="Michael", xmlns="http://www.topografix.com/GPX/1/1")

    # Create a track element
    trk = SubElement(gpx, 'trk')
    name = SubElement(trk, 'name')
    name.text = "Or2k"

    # Iterate through the DataFrame and create a track segment for each point
    for _, row in df.iterrows():
        trkseg = SubElement(trk, 'trkseg')
        # Repeat the same point twice within the same track segment
        for _ in range(2):
            trkpt = SubElement(trkseg, 'trkpt', lat=f"{row['latitude']:.6f}", lon=f"{row['longitude']:.6f}")
            # Altitude and time can be added if needed
            # ele = SubElement(trkpt, 'ele')
            # ele.text = f"{row['altitude']:.2f}"
            # time = SubElement(trkpt, 'time')
            # time.text = pd.to_datetime(row['dataTime'], unit='s').isoformat() + "Z"  # Ensure UTC time

    # Save the GPX content to a file
    ElementTree(gpx).write(output_gpx_path, encoding='utf-8', xml_declaration=True)
    print(f"GPX file saved to {output_gpx_path}")


if __name__ == "__main__":
    # Replace these with your actual file paths
    csv_file_path = 'backUpData.csv'  # Example: 'data.csv'
    output_gpx_path = 'output5.gpx'

    convert_csv_to_gpx(csv_file_path, output_gpx_path)
