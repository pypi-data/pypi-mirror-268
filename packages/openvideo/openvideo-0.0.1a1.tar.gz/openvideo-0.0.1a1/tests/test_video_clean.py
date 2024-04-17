import os
import sys
root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)
from openvideo.utils import download, get_md5
from openvideo.video.utils import check_video_integrity
from openvideo.video.clean import extract_key_frames, split_video_into_scenes


def test_video_clean():
    # params
    save_path = "tests/test_clean/panda_example.mp4"
    split_save_dir = "tests/test_clean/splits"
    key_frames_dir = "tests/test_clean/key_frames"
    
    if not os.path.exists("tests/test_clean/"):
        os.makedirs("tests/test_clean/")
    
    # download the test video
    download(
        filename=save_path,
        url="https://huggingface.co/heatingma/OpenVideo/resolve/main/panda_example.mp4"
    )
    
    # check the integrity of the video
    check_video_integrity(save_path)
    
    # split the video into scenes
    split_video_into_scenes(
        video_path=save_path,
        save_dir=split_save_dir
    )
    
    # extract key frames
    videos = os.listdir(split_save_dir)
    for video_name in videos:
        video_path = os.path.join(split_save_dir, video_name)
        md5 = get_md5(video_path)
        extract_key_frames(
            video_path=video_path,
            save_dir=os.path.join(key_frames_dir, md5),
            filename=md5
        )
        

if __name__ == "__main__":
    test_video_clean()
