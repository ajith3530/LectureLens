import re
import os

from utils import generate_output_filename

def parse_rtt_transcript(file_path):
    combined_text = []
    # Read the RTT transcript file
    with open(file_path, 'r', encoding='utf-8') as file:
        transcript = file.read()

    # Regular expression pattern to extract speaker and text content
    pattern = r'<v (.*?)>(.*?)<\/v>(.*?)<v (.*?)>'

    # Compile the regular expression pattern
    regex = re.compile(pattern, re.DOTALL)

    # Initialize variables to store parsed data
    current_speaker = None
    current_text = ''
    output_filepath = os.path.join("output", generate_output_filename(suffix="IR"))
    with open(output_filepath, 'w', encoding='utf-8') as output:
        # Parse the transcript
        for match in regex.finditer(transcript):
            speaker, text = match.group(1), match.group(2).strip()

            if speaker != current_speaker:
                # If the speaker changes, print the accumulated text
                if current_speaker:
                    output.write(f"{current_speaker}: {current_text}\n")
                # Start accumulating text for the new speaker
                current_speaker = speaker
                current_text = text
            else:
                # If the speaker is the same, append the text
                current_text += ' ' + text


        # Print the final accumulated text for the last speaker
        if current_speaker:
            output.write(f"{current_speaker}: {current_text}\n")
    return output_filepath


if __name__ == "__main__":
    # Example usage
    file_path = 'transcripts/hscd_transcript.vtt'
    parse_rtt_transcript(file_path)
