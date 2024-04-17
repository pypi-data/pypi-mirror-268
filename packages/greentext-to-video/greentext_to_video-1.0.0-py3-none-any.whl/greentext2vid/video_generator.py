import os
import random
from basc_py4chan import Board
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
from moviepy.editor import ImageClip, AudioFileClip, VideoFileClip, CompositeVideoClip, concatenate_audioclips, concatenate_videoclips
from moviepy.video.fx.all import crop

class Video_Generator:
    """
    A class that generates videos from text comments.

    Args:
        bg_video_path (str): The path to the background video file.
        tmp_dir (str, optional): The directory to store temporary files. Defaults to 'tmp'.
        output_dir (str, optional): The directory to save the output video files. Defaults to 'output'.
        font_path (str, optional): The path to the font file. Defaults to 'fonts/arial.ttf'.
        font_size (int, optional): The font size. Defaults to 50.
        bg_color (tuple, optional): The background color in RGB format. Defaults to (245, 233, 225).
        wall_color (tuple, optional): The color for wall text in RGB format. Defaults to (120, 153, 34).
        text_color (tuple, optional): The color for regular text in RGB format. Defaults to (128, 0, 0).
        h_padding (int, optional): The horizontal padding for the text. Defaults to 20.
        v_padding (int, optional): The vertical padding for the text. Defaults to 15.
        resolution (tuple, optional): The resolution of the output video in (width, height) format. Defaults to (1080, 1920).
        frame_rate (int, optional): The frame rate of the output video. Defaults to 30.
    """

    def __init__(self, bg_video_path, tmp_dir='tmp', output_dir='output', font_path='fonts/arial.ttf', font_size=50, bg_color=(245, 233, 225), wall_color=(120, 153, 34), text_color=(128, 0, 0), h_padding=20, v_padding=15, resolution=(1080, 1920), frame_rate=30):
        self.tmp_dir = tmp_dir
        self.output_dir = output_dir
        self.bg_video_path = bg_video_path
        self.font_path = font_path
        self.font_size = font_size
        self.bg_color = bg_color
        self.wall_color = wall_color
        self.text_color = text_color
        self.h_padding = h_padding
        self.v_padding = v_padding
        self.resolution = resolution
        self.frame_rate = frame_rate

        if not os.path.exists(self.tmp_dir):
            os.makedirs(self.tmp_dir)
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def set_bg_video_path(self, bg_video_path):
        """
        Set the path to the background video file.

        Args:
            bg_video_path (str): The path to the background video file.
        """
        self.bg_video_path = bg_video_path

    def _generate_img(self, text: str):
        """
        Generate an image from the given text.

        Args:
            text (str): The text to generate the image from.

        Returns:
            PIL.Image.Image: The generated image.
        """
        img = Image.new('RGB', (5000, 5000), color=self.bg_color)
        d = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.font_path, self.font_size)
        size = d.textbbox((self.h_padding, self.v_padding), text, font=font)
        if size[2] + self.h_padding > self.resolution[0]:
            if "." in text:
                texts = text.split('. ')
                texts[len(texts)//2] = '\n' + texts[len(texts)//2]
                text = '. '.join(texts)
            else:
                texts = text.split(' ')
                texts[len(texts)//2+1] = '\n' + texts[len(texts)//2+1]
                text = ' '.join(texts)
            size = d.textbbox((self.h_padding, self.v_padding), text, font=font)
        color = self.wall_color if text.startswith('>') else self.text_color
        d.text((self.h_padding, self.v_padding), text, fill=color, font=font)
        img = img.crop((0, 0, size[2] + self.h_padding, size[3] + self.v_padding))
        return img

    def _text_to_speech(self, text, filename):
        """
        Convert the given text to speech and save it as an audio file.

        Args:
            text (str): The text to convert to speech.
            filename (str): The path to save the audio file.
        """
        text = text.replace('>', '').replace('\'', '').replace('mfw', 'my face when').replace('qt', 'cutie').replace('3.14', 'pie').replace('tfw', 'that feel when')
        tts = gTTS(text=text, lang='en')
        tts.save(filename)

    def process_threads(self, links):
        """
        Process the threads from the given links and yield the topic of each thread.

        Args:
            links (list): A list of links to the threads.

        Yields:
            str: The topic of each thread.
        """
        for link in links:
            board_name, thread_id = link.split('/')[3], link.split('/')[5].split('#')[0]
            board = Board(board_name)
            thread = board.get_thread(thread_id)
            if thread:
                yield thread.topic

    def generate_video(self, post):
        """
        Generate a video from the given post.

        Args:
            post (Post): The post object containing the text comment.

        Returns:
            str: The path to the generated video file.
        """
        images = []
        audios = []

        for file in os.listdir(self.tmp_dir):
            os.remove(os.path.join(self.tmp_dir, file))

        lines = [line.strip() for line in post.text_comment.split('\n') if len(line) > 0]
        for index, line in enumerate(lines):
            img = self._generate_img(line)
            if img.size[0]+100 >= self.resolution[0]:
                img = img.resize((self.resolution[0]-100, img.size[1]*(self.resolution[0]-100)//img.size[0]))
            elif img.size[0] < 250:
                img = img.resize((250, img.size[1]*250//img.size[0]))
            img_path = os.path.join(self.tmp_dir, f'{index}.png')
            img.save(img_path)
            images.append(ImageClip(img_path))
            
            audio_path = os.path.join(self.tmp_dir, f'{index}.mp3')
            self._text_to_speech(line, audio_path)
            audios.append(AudioFileClip(audio_path))
        
        final_audio = concatenate_audioclips(audios)
        for index, img in enumerate(images):
            images[index] = img.set_duration(audios[index].duration)

        images_clip = concatenate_videoclips(images, method='compose').set_position(('center', 'center'))
        bg_clip = VideoFileClip(self.bg_video_path)
        
        bg_random = random.uniform(0, bg_clip.duration - final_audio.duration)
        width, height = bg_clip.size
        crop_width = height * 9/16
        x1, x2 = (width - crop_width)//2, (width + crop_width)//2
        y1, y2 = 0, height
        cropped_bg = crop(bg_clip, x1=x1, x2=x2, y1=y1, y2=y2).resize(self.resolution)
        trimmed_bg = cropped_bg.subclip(bg_random, bg_random + final_audio.duration)

        final_video = CompositeVideoClip([trimmed_bg, images_clip], size=self.resolution).set_audio(final_audio)
        output_video = os.path.join(self.output_dir, f'{post.post_id}.mp4')
        final_video.write_videofile(output_video, fps=self.frame_rate, codec='libx264', audio_codec='aac')

        return output_video

if __name__ == "__main__":

    with open('links.txt', 'r') as f:
        links = f.readlines()

    vg = Video_Generator("bg/minecraft.mp4")
    posts = vg.process_threads(links)
    for post in posts:
        videos = os.listdir(vg.output_dir)
        if f'{post.post_id}.mp4' not in videos:    
            vg.generate_video(post)
