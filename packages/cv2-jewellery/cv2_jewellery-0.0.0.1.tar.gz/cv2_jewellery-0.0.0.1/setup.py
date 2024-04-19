from setuptools import setup, find_packages

setup(
    name='cv2_jewellery',
    version='0.0.0.1',
    packages=find_packages(),
    description='Package for overlaying jewellery on webcam feed',
    author='Dipenkumar👨‍💻',
    install_requires=[
        'tf-bodypix==0.4.2',
        'tfjs-graph-converter==1.6.3',
        'tensorflowjs==3.13.0',
        'tensorflow==2.8.0',
        'numpy==1.23.5',
        'pandas==2.2.1',
        'requests==2.31.0',
        'mediapipe==0.10.11',
        'opencv-python==4.7.0.68'
    ],
     package_data={
        '': ['data/**/*.png']   # Include all files in the data_folder
    },
     include_package_data=True
)
