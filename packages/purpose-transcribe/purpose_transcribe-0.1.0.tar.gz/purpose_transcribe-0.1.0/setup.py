from setuptools import setup, find_packages
setup(
    name='purpose_transcribe',
    version='0.1.0',
    description='A CLI tool for transcribing audio files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mark Okello',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        'click',
        'openai-whisper'
    ],
    entry_points={
        'console_scripts': [
            'purpose_transcribe=purpose_transcribe.main:process_audio'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.9',
)