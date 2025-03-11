import cv2
import os

def extract_frames(video_path, output_folder):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open video file
    cap = cv2.VideoCapture(video_path)
    
    # Get the frames per second (FPS)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print(f"Frames per second: {fps}")
    
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Save frame as image
        frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)
        
        frame_count += 1
    
    cap.release()
    print(f"Extracted {frame_count} frames and saved in '{output_folder}'.")

if __name__ == "__main__":
    video_path = input("Enter the video file path: ")
    output_folder = "extracted_frames"
    extract_frames(video_path, output_folder)
