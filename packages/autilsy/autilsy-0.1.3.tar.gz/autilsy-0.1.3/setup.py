from setuptools import setup, find_packages
setup(
    name="autilsy",
    version="0.1.3",
    packages=find_packages(),
    install_requires=["imutils","jsonpatch","uuid","opencv-python",
        "numpy","tqdm","tabulate", "shapely","moviepy","yaml",
        "pillow","scikit-learn","jsonpointer","easydict"],
    author="admon",
    author_email="admon@gmail.com",
    description="A brief utils of scripts"
)