from image_to_video_generator import generate_video
from save_generated_video import get_task_result



if __name__ == "__main__":
    # Generate video
    task_result = generate_video(prompt="make a video of the cartoon man doing a moonwalk dance on stage (in full view, head to toe showing).")
    
    print("Task ID:",task_result)


    # Save generated video
    get_task_result(task_result['task_id'])
    
