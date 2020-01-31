from __future__ import print_function

import os
from shutil import copyfile
from google_drive_downloader import GoogleDriveDownloader as gdd


try:
    from urllib.request import urlretrieve
except ImportError:
    from urllib import urlretrieve

URLBASE = 'https://www.data.gouv.fr/fr/datasets/r/{}'
URLS = ['b4aaeede-1a80-4d76-8f97-543dad479167', '72b251e1-d5e1-4c46-a1c2-c65f1b26549a',
        'd9d65ca1-16a3-4ea3-b7c8-2412c92b69d9', '6eee0852-cbd7-447e-bd70-37c433029405',
        'd6103d0c-6db5-466f-b724-91cbea521533', '07bfe612-0ad9-48ef-92d3-f5466f8465fe',
        '9b76a7b6-3eef-4864-b2da-1834417e305c', '9a7d408b-dd72-4959-ae7d-c854ec505354',
        'be2191a6-a7cd-446f-a9fc-8d698688eb9e', 'e4c6f4fe-7c68-4a1d-9bb6-b0f1f5d45526',
        '08b77510-39c4-4761-bf02-19457264790f', '86c64436-427f-4042-a4ee-ed0aa31bac76'
        ]
DATA = []
for year in [2018, 2017, 2016]:
    for type_data in ["vehicules", "usagers", "lieux", "caracteristiques"]:
        DATA.append(f"{type_data}_{year}.csv")


def main(output_dir='data'):
    filenames = DATA
    full_urls = [URLBASE.format(url) for url in URLS]

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for url, filename in zip(full_urls, filenames):
        output_file = os.path.join(output_dir, filename)

        if os.path.exists(output_file):
            continue

        print("Downloading from {} ...".format(url))
        urlretrieve(url, filename=output_file)
        print("=> File saved as {}".format(output_file))

    # Download sensor data
    output_sensor_file = os.path.join(output_dir, "sensors_data.csv")
    if not os.path.exists(output_sensor_file):
        gdd.download_file_from_google_drive(file_id="1W-sD3qS5KXj1z2QUXuLyFx7lbL_WPoeX",
                                        dest_path=output_sensor_file)

    if os.path.exists(os.path.join('submissions', 'starting_kit')):
        copyfile(
            os.path.join('data', DATA[0]),
            os.path.join('submissions', 'starting_kit',
                         DATA[0])
        )



if __name__ == '__main__':
    test = os.getenv('RAMP_TEST_MODE', 0)

    if test:
        print("Testing mode, not downloading any data.")
    else:
        main()
