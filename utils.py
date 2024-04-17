import os
import datetime
import json

def read_prompts_from_json():
    with open('prompts.json', 'r') as file:
        data = json.load(file)
    return data

def generate_output_filename(suffix="LectureLens"):
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
    output_filename = f"{suffix}_{timestamp}.txt"  # You can change 'output' to your desired prefix
    return output_filename

def load_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def save_to_file(responses, suffix="dummy"):
    output_file = os.path.join("output", generate_output_filename(suffix=suffix))
    with open(output_file, 'w') as file:
        for response in responses:
            file.write(response[0] + '\n')
    return output_file

def save_summary_to_file(responses, suffix="dummy"):
    output_file = os.path.join("output", generate_output_filename(suffix=suffix))
    with open(output_file, 'w') as file:
        for response in responses:
            response_lines = response.split(".")
            for response_line in response_lines:
                file.write(response_line + '\n')
    return output_file

def single_summary_save_to_file_(responses, suffix="dummy"):
    output_file = os.path.join("output", generate_output_filename(suffix=suffix))
    with open(output_file, 'w') as file:
        for response in responses:
            file.write(response + '\n')
    return output_file

def single_summary_append_to_file_(responses, output_filepath):
    with open(output_filepath, 'a') as file:
        for response in responses:
            file.write('\n')
            file.write(response + '\n')
    return output_filepath


if __name__ == "__main__":
    # # Example usage:
    # prompts = read_prompts_from_json()
    # student_prompt1 = prompts['student_prompt1']
    # student_prompt2 = prompts['student_prompt2']
    # admin_prompt = prompts['admin_prompt']
    #
    # # Print the prompts
    # print("Student Prompt 1:", student_prompt1)
    # print("Student Prompt 2:", student_prompt2)
    # print("Admin Prompt:", admin_prompt)
    data = load_text(file_path=os.path.join("output", "IR_2024-04-15_00-46-07.txt"))
    print("Test Completed")

    single_summary_append_to_file_(["Hello"], output_filepath=r"/Users/ajith/PycharmProjects/LectureLens/output/second_level_2024-04-15_01-33-10.txt")