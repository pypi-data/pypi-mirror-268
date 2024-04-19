from distutils.core import setup

setup(
    name='sightvision',
    packages=['sightvision'],
    version='0.0.1',
    license='MIT',
    description='Computer vision package that makes its easy to run Image processing and AI functions.',
    author='Leonardi Melo',
    author_email='opensource.leonardi@gmail.com',
    url='https://github.com/rexionmars/SightVision',
    keywords=['ComputerVision', 'Tensorflow', 'MediaPipe', 'FaceDetection'],
    install_requires=['opencv-python', 'numpy', 'mediapipe'],
    python_requires='>=3.8',  # Requires any version >= 3.6
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',  # Specify which pyhton versions that you want to support
    ],
)
