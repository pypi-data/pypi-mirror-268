import os
import PySimpleGUI as sg
import cv2
from autilsy.common import Autils
from resource.image_bytes import ImgBytes
import cv2
class VideoFile(object):
    def __init__(self, video_path="") -> None:
        self._video_path = video_path
        self._vid_cap = None
        self._init_stat = False
        self._fram_id = 0

    def Start(self, video_path):
        if self._vid_cap is not None:
            self._vid_cap.release()
        
        self._video_path = video_path
        self._vid_cap = cv2.VideoCapture(video_path)
        
        self._width  = self._vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self._height = self._vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self._frams  = self._vid_cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self._fps    = self._vid_cap.get(cv2.CAP_PROP_FPS)
        
    def GetNextFrame(self,):
        ret, frame = self._vid_cap.read()
        self._fram_id += 1

        return frame if ret else None

    def GoToFrame(self, frame_num):
        if frame_num <= 0: frame_num = 1
        if frame_num >= self._frams: frame_num = self._frams - 1
        
        self._vid_cap.set(cv2.CAP_PROP_POS_FRAMES, frame_num)
        ret, frame = self._vid_cap.read()

        return frame if ret else None

    def __del__(self,):
        if self._vid_cap.isOpened():
            self._vid_cap.release()

class Camera(object):
    def __init__(self, cam_id=0) -> None:
        self._cam_id = cam_id
        self._curr_fram_num = 0
        self._record_fram_num = 0
        self._stat = False
        self._vid_cap = None
        

    def SetCamID(self, cam_id):
        if self._vid_cap is not None:
            self._vid_cap.release()
        self._cam_id = cam_id
        self._vid_cap = cv2.VideoCapture(self._cam_id)

    def Record(self,):
        if self._vid_cap is None: return None
        ret, frame = self._vid_cap.read()
        self._stat = True

        return frame if ret else None

    def __del__(self,):
        if self._vid_cap.isOpened() or self._vid_cap is not None:
            self._vid_cap.release()


class UIApp(Autils):
    def __init__(self, gui_engine=sg,
                 font=("宋体", 15),
                 theme='DarkBlue4'):
        self._image_paths = ""
        self._image_names = ""
        self._img_idx = 0
        self._engine = gui_engine
        self._video_frame = None
        self._video_file_path = ""
        self._dis_region_size = (1080, 720)
        self._engine.theme(theme)
        self._engine.set_options(font=font)

    def ChooseImages(self, img_suffix="all"):
        folder = self._engine.popup_get_folder('Image folder to open')
        if folder is None or not self.IsDirPath(folder):
            sg.popup_cancel('Image folder invalid!')
            return

        image_paths = self.GetImgPaths(folder)
        self._folder = folder
        self._image_paths = []
        for img_path in image_paths:
            if img_suffix == "all":
                self._image_paths.append(img_path)
            elif img_suffix == "jpg" and os.path.basename(img_path)[:-3] == img_suffix:
                self._image_paths.append(img_path)
            elif img_suffix == "png" and os.path.basename(img_path)[:-3] == img_suffix:
                self._image_paths.append(img_path)
            elif img_suffix == "bmp" and os.path.basename(img_path)[:-3] == img_suffix:
                self._image_paths.append(img_path)

        
        self._img_idx = 0    
        self._image_names = [os.path.basename(f) for f in self._image_paths]

        if len(self._image_paths) == 0:
            sg.popup_cancel("There are no images!")

    def ShowImage(self, window, img):
        if self.IsFilePath(img):
            img = cv2.imread(img)
        if img is None:
            print("image is None!")
            return
        img = cv2.resize(img, self._dis_region_size)
        imgbytes = cv2.imencode('.png', img)[1].tobytes()
        window['-IMAGE1-'].update(data=imgbytes)

    def PromptWindow(self, info):
        self._engine.popup(info)

    def Layouts(self,):
        image_buttons = [[sg.Button('选择图片',key="-browse_images-")],
            [sg.Button('检测', key='-detect_image-')],
            [sg.Button('Prev', size=(4, 1)), sg.Button('Next', size=(4, 1))],
            [sg.Listbox(values=self._image_names, size=(20, 15), key='-IMG_LIST_BOX-', enable_events=True)],
            [sg.Text('File {} of {}'.format(self._img_idx,len(self._image_paths)), size=(15, 1),key='-FILENUM-')]
            ]

        camera_buttons = [
            [sg.Checkbox("Cam ID:", key="-CHECK_CAM_ID-", enable_events=True), sg.Combo([0,1,2,3,4,5], key='-CAM_ID-', size=(2, 1))],
            [sg.Radio('关闭', 'Cam_Radio', True, size=(10, 1),key='-CLOSE_CAM-')],
            [sg.Radio('开启', 'Cam_Radio', False, size=(10, 1),key='-START_CAM-')],
        ]

        video_buttons = [
            # video file  
            [sg.Radio('播放', 'Video_Radio', False, size=(10, 1),key='-PLAY_VIDEO-')],
            [sg.Radio('停止', 'Video_Radio', True, size=(10, 1),key='-STOP_VIDEO-')],
            [sg.Button("浏览",size=(10, 1), key='-SELECT_VIDEO-')], 
            [sg.Input(size=(150,6),key="_FILEPATH_")]
        ]

        images_layout= [[sg.Text(size=(1,1))],  # some blank lines
                        [sg.Image(ImgBytes.canvas3,size=self._dis_region_size, key='-IMAGE1-', background_color='white')],
                    ] 

        buttons = [
            [sg.Frame("video",  video_buttons,  size=(160,150), title_color="red",element_justification='c')],
            [sg.Frame("camera", camera_buttons, size=(160,130), title_color="red",element_justification='c')],
            [sg.Frame("image",  image_buttons,  size=(160,330), title_color="red",element_justification='c')]]



        self._layout = [
            [
            sg.Column(buttons, element_justification='c', vertical_alignment='t'),
            sg.Column(images_layout, element_justification='c', vertical_alignment='t'),
            ]
        
        ]

    def SetImageFolder(self, window):
        self.ChooseImages()
        if len(self._image_names) > 0:
            img_path = self._image_paths[self._img_idx]
            self.ShowImage(window, img_path)
            window['-IMG_LIST_BOX-'].update(values=self._image_names)

    def TraverseImage(self, window, mode, list_val=None):
        assert mode in ("Prev", "Next", "List")

        if len(self._image_paths) == 0:
            self.PromptWindow("Please choose files fisrt!")
        else:
            if mode == "Next":
                self._img_idx += 1
                if self._img_idx >= len(self._image_paths):
                    self._img_idx = len(self._image_paths) - 1    
            elif mode == "Prev":
                self._img_idx -= 1
                if self._img_idx < 0:
                    self._img_idx = 0
            elif mode == "List":
                assert list_val is not None
                img_path = os.path.join(self._folder, list_val)
                self._img_idx = self._image_paths.index(img_path)
                self.ShowImage(window, img_path)

            print("img_idx:{}".format(self._img_idx))
            self.ShowImage(window, self._image_paths[self._img_idx])
            window['-IMG_LIST_BOX-'].update(set_to_index=self._img_idx, scroll_to_index=self._img_idx)
            window['-FILENUM-'].update('File {} of {}'.format(self._img_idx+1,len(self._image_paths)))

    def InitVideoFile(self, window):
        try:
            video_path = sg.filedialog.askopenfile().name
            self._video_file_path = video_path
            window.Element("_FILEPATH_").Update(video_path)
        except AttributeError:
            print("no video selected!")
        
    def UpdateImage(self, window, img):
        img = cv2.resize(img, self._dis_region_size)
        imgbytes = cv2.imencode('.png', img)[1].tobytes()

        window['-IMAGE1-'].update(data=imgbytes)

    def Init(self,):
        self.Layouts()
        self._window = sg.Window('用户界面', self._layout, resizable=True)#size=(1280,720),disable_minimize=True, , disable_close=False, resizable=True, scaling=False
        self._camera = Camera()
        self._video_player = VideoFile()


    def Run(self,):
        window = self._window
        while True:             # Event Loop
            event, values = window.read(timeout=1) #
            print(event, values)
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            
            #---image
            if event == '-browse_images-':
                self.SetImageFolder(window)
            if event in ('-Next-'): #, 'Down:40', 'Next:34'
                self.TraverseImage(window, "Next")
            elif event in ('-Prev-'): #,'Up:38', 'Prior:33'
                self.TraverseImage(window, "Prev")
            elif event == '-IMG_LIST_BOX-':
                self.TraverseImage(window, "List", values['-IMG_LIST_BOX-'][0])

            #---camera
            if event == "-CHECK_CAM_ID-":
                cam_id = values.get('-CAM_ID-')
                if cam_id != "": 
                    cam_id = int(cam_id)
                    self._camera.SetCamID(cam_id)
            if values['-CHECK_CAM_ID-'] and values['-START_CAM-']:
                frame = self._camera.Record()
                if frame is not None:
                    self.UpdateImage(window,frame)
            
            #---video file
            if event == "-SELECT_VIDEO-":
                self.InitVideoFile(window)
                self._video_player.Start(self._video_file_path)
            if values['-PLAY_VIDEO-']:
                frame = self._video_player.GetNextFrame()
                if frame is not None:
                    self.UpdateImage(window, frame)
                

            if event == '-detect_image-':
                pass
        window.close()


def main():
    ui = UIApp()
    ui.Init()
    ui.Run()


if __name__ == '__main__':
   
    main()