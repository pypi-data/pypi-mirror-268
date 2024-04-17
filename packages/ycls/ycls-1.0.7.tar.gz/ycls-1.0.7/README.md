# YCLS (YouTube Content Loudness Scanner)

YCLS is a Python module for calculating loudness metrics for audio (or video) files, particularly aimed at determining the loudness level suitable for YouTube content. It provides functions to calculate various loudness metrics such as LUFS (Loudness Units Full Scale), peak loudness in dBFS (decibels relative to full scale), and adjusted loudness suitable for YouTube.

## Installation

You can install the `ycls` module using pip:

```bash
pip install ycls
```

Make sure you have `ffmpeg` installed on your system.

**For Windows:**
```bash
winget install Gyan.FFmpeg.Essentials
```

## Usage

You can import functions from the `ycls` module using the following syntax:

```python
from ycls import calculate_loudness_lufs, calculate_youtube_content_loudness, calculate_peak_dbfs
```

## Functions

### `calculate_loudness_lufs(input_file)`

This function calculates the loudness level of the input audio (or video) file in LUFS (Loudness Units Full Scale) using the `r128gain` library.

- **Parameters:**
  - `input_file` (str): The path to the input audio (or video) file.

- **Returns:**
  - The loudness level of the input audio (or video) file in LUFS.

### `calculate_youtube_content_loudness(input_file)`

This function calculates the adjusted loudness suitable for YouTube content based on the input audio (or video) file. It adds 14 dB to the loudness level calculated by `calculate_loudness_lufs`.

- **Parameters:**
  - `input_file` (str): The path to the input audio (or video) file.

- **Returns:**
  - The adjusted loudness suitable for YouTube content in dB.

### `calculate_peak_dbfs(input_file)`

This function calculates the peak loudness in dBFS (decibels relative to full scale) of the input audio (or video) file using the `r128gain` library.

- **Parameters:**
  - `input_file` (str): The path to the input audio (or video) file.

- **Returns:**
  - The peak loudness of the input audio (or video) file in dBFS.

## Running the Module via CLI

You can also run `ycls` from the command line interface (CLI). After installing the module, you can use it as follows:

```bash
ycls -i <input_file_path>
```

Replace `<input_file_path>` with the path to your audio (or video) file.

### Example

Suppose you have an audio file named `example_audio.mp3`. You can calculate its loudness metrics using the CLI:

```bash
ycls -i example_audio.mp3
```

This will print the loudness metrics of the audio file to the console.
```
File Loudness: -23.6 LUFS
Peak Loudness: -2.3 dBFS
Youtube Content Loudness: -9.6 dB
```

## Requirements

- Python 3.6+
- r128gain library
- typer library
- ffmpeg