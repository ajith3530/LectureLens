
import time
from text_processor import parse_rtt_transcript
from generator_module import process_information
from render import create_flask_app

# Global variables
STUDENT_SUMMARY_FILEPATH = "None"
ADMIN_SUMMARY_FILEPATH = "None"

class LectureLens:
    def __init__(self, rtt_transcript):
        self.rtt_transcript = rtt_transcript
        self.generate_information()

    def __process_transcript(self):
        return parse_rtt_transcript(file_path=self.rtt_transcript)

    def generate_information(self):
        global STUDENT_SUMMARY_FILEPATH, ADMIN_SUMMARY_FILEPATH
        processed_transcript_filepath = self.__process_transcript()
        STUDENT_SUMMARY_FILEPATH, ADMIN_SUMMARY_FILEPATH = process_information(input_file=processed_transcript_filepath)


if __name__ == '__main__':
    filepath = r"/Users/ajith/PycharmProjects/LectureLens/transcripts/hscd_transcript.vtt"
    print("Starting Application")
    time.sleep(5)
    app_init = LectureLens(rtt_transcript=filepath)
    time.sleep(5)
    app = create_flask_app(STUDENT_SUMMARY_FILEPATH, ADMIN_SUMMARY_FILEPATH)
    app.run(debug=True)
