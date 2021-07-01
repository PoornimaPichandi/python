"""A video player class."""
import random

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()
        all_videos.sort(key=lambda x: x.title)
        print("Here is a list of available videos:")

        for video in all_videos:
            tagString = str(video.tags)

            print(video.title, "(", video.video_id, ")", "[",tagString.strip("()"), "]")

    """   videos = self._video_library.get_all_videos()
        show_all_videos_list = [] ##create list

        for element in videos:
            for t_a_g in element.tags:
                tags = "[" + t_a_g + " "
                tags = tags + "]"
                if tags != "[]":
                    tags = tags[0:len(tags)-2] + "]"
                    show_all_videos_list += [f"{element.title} ({element.video.id}){tags}"]
            ##sorting in lexicographical order

        show_all_videos_list.sort()
        print("here is alist of avaialable videos")
        for element in show_all_videos_list:
            print(element)
"""

    def play_video(self, video_id):
        video = self._video_library.get_video(video_id)
        if not video:
            print("Cannot play video: Video does not exist")
        if video:
            print(f"playing video: {video.title}")
            self._current_video = video

    def stop_video(self):
        """Stops the current video."""
        current_video = self._current_video
        if current_video:
            print(f'Stopping video:{self._current_video.title}')
            self._current_video = None
        else:
            print("Cannot play Video: Video does not exist")

        #print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        getVideos = self._video_library.get_all_videos()  # Grab all videos
        num_videos = len(self._video_library.get_all_videos())  # Borrowed code to check if videos.txt is empty

        if num_videos == 0:  # Should trigger if there were no videos found in the txt file
            print("There are no videos available to play")  # Will need retrofit to fit flagged videos if I get there
        else:
            pickvideo = random.choice(getVideos)
            print("playingvideo:",pickvideo.title)


    def pause_video(self):
        """Pauses the current video."""
        pause_video = self._current_video
        if pause_video:
            self.isPaused = True
            print(f"Pausing Video:{self._current_video} ")
            print("Stopping Video:",self._current_video.title)
            self._current_video = pause_video
            self.isPlaying = False
        else:
            print("No video playing currently")

    def continue_video(self):
        """Resumes playing the current video."""
        # if self._current_video is not None:
        #     if not self.pause_video:
        #         print(f"Cannot continue video: Video is not paused")
        #     else:
        #         print(f"Continuing video: {self._current_video.title}")
        # else:
        #     print("Cannot continue video: No video is currently playing")

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video == None:
            print("No videos playing now")
        else:
            print(f'video Playing:{self._current_video.title} ({self._current_video.video_id})[{self._current_video.tags}]')

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        video_term = self._video_library.get_video(search_term)
        if(video_term):
            print(f"search results: {search_term}")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        video_tag_search = self._video_library.get_video(video_tag)
        if (video_tag_search):
            print(f"search results for video tag:{video_tag}")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
