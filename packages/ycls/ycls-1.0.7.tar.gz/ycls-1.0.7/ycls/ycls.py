import r128gain
import typer

def calculate_loudness_lufs(input_file: str) -> float:
    '''Calculates the loudness level of the input audio (or video) file in LUFS (Loudness Units Full Scale) using the r128gain library.'''
    return r128gain.get_r128_loudness([input_file])[0]

def calculate_youtube_content_loudness(input_file: str) -> float:
    '''Calculates the adjusted loudness suitable for YouTube content based on the input audio (or video) file. It adds 14 dB to the loudness level calculated by calculate_loudness_lufs.'''
    return round(calculate_loudness_lufs(input_file) + 14, 1)

def calculate_peak_dbfs(input_file: str) -> float:
    '''Calculates the peak loudness in dBFS (decibels relative to full scale) of the input audio (or video) file using the r128gain library.'''
    return round(r128gain.scale_to_gain(r128gain.get_r128_loudness([input_file])[1]), 1)


def main(input_file: str = typer.Option(None, "-i", help="Input file path.")):
    if not input_file:
        print("Please enter input file, --help to view commands.")
        return
    
    lufs = calculate_loudness_lufs(input_file)
    peak = calculate_peak_dbfs(input_file)
    youtube_content_loudness = calculate_youtube_content_loudness(input_file)

    print(f"File Loudness: {lufs} LUFS")
    print(f"Peak Loudness: {peak} dBFS")
    print(f"Youtube Content Loudness: {youtube_content_loudness} dB")


def run_cli():
    typer.run(main)

if __name__ == "__main__":
    run_cli()