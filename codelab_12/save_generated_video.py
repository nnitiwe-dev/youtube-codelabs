import requests
import os
import time
import itertools
import sys
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

url = "https://api.novita.ai/v3/async/task-result"

sys.stdout.reconfigure(line_buffering=True)
os.environ["PYTHONUNBUFFERED"] = "1"

api_key = os.getenv("NOVITA_API_KEY")
task_id = ""
# Ensure output folder exists
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_file(file_url, filename):
    """Download and save file to output directory"""
    try:
        response = requests.get(file_url, stream=True)
        response.raise_for_status()
        file_path = os.path.join(OUTPUT_DIR, filename)
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"\n✅ Saved: {file_path}")
    except Exception as e:
        print(f"\n❌ Download failed: {e}")

def get_task_result(task_id, poll_interval=10):
    """Poll task status until completion, with loading animation"""
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    while True:
        try:
            payload = {"task_id": task_id}
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"{api_key}"
            }

            response = requests.get(url, headers=headers, params=payload)
            result = response.json()

            # Handle invalid responses
            if "task" not in result:
                print(f"\n❌ Invalid response: {result}")
                return None
            
            
            task = result["task"]
            
            status = task.get("status")


            # Show small spinner while polling
            sys.stdout.write(f"\rChecking task status {next(spinner)}  [{status}]")
            sys.stdout.flush()

            if status == "TASK_STATUS_SUCCEED":
                print("\n✅ Task completed!")

                # Download results
                for i, v in enumerate(result.get("videos", []), start=1):
                    video_url = v.get("video_url")
                    if video_url:
                        download_file(video_url, f"video_{i}.mp4")

                for i, img in enumerate(result.get("images", []), start=1):
                    image_url = img.get("image_url")
                    if image_url:
                        download_file(image_url, f"image_{i}.png")

                for i, a in enumerate(result.get("audios", []), start=1):
                    audio_url = a.get("audio_url")
                    if audio_url:
                        download_file(audio_url, f"audio_{i}.mp3")

                print("✅ All files saved to /output/")
                break

            elif status == "TASK_STATUS_PROCESSING" or status == "TASK_STATUS_QUEUED":
                pass
            else:
                print("\n❌ Task failed.")
                break

            # Wait before polling again
            time.sleep(poll_interval)

        except KeyboardInterrupt:
            print("\n🛑 Stopped by user.")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            break