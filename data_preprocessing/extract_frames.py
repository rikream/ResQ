import cv2
import os

input_folder = "../data/raw_data"
output_folder = "frames"

os.makedirs(output_folder, exist_ok=True)

frame_skip = 5

for video_file in os.listdir(input_folder):
    video_path = os.path.join(input_folder, video_file)

    cap = cv2.VideoCapture(video_path)
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if count % frame_skip == 0:
            filename = f"{video_file}_frame_{count}.jpg"
            cv2.imwrite(os.path.join(output_folder, filename), frame)

        count += 1

    cap.release()

print("All videos processed!")