import os
from openvideo.video.utils import cal_video_duration
from scenedetect import open_video, SceneManager, split_video_ffmpeg
from scenedetect.detectors import ContentDetector
from scenedetect.video_splitter import split_video_ffmpeg


def split_video_into_scenes(
    video_path: str,
    save_dir: str,
    min_time: str = 5.0,
    max_time: str = 60.0,
    threshold: int = 27.0
):
    # Open our video, create a scene manager, and add a detector.
    video = open_video(video_path)
    scene_manager = SceneManager()
    scene_manager.add_detector(
        ContentDetector(threshold=threshold))
    scene_manager.detect_scenes(video, show_progress=True)
    scene_list = scene_manager.get_scene_list()
    
    # split video
    split_video_ffmpeg(
        input_video_path=video_path, 
        scene_list=scene_list, 
        output_dir=save_dir, 
        show_progress=True
    )
    
    # filter
    videos = os.listdir(save_dir)
    for video_name in videos:
        video_path = os.path.join(save_dir, video_name)
        duration = cal_video_duration(video_path)
        if duration < min_time or duration > max_time:
            os.remove(video_path)