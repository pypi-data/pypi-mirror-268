from __future__ import annotations
import os
import imutils, imutils.paths
import json
import xml.etree.ElementTree as ET
import uuid
import cv2
import numpy as np
import scipy.interpolate
import shutil
from tqdm import tqdm
import random
from tabulate import tabulate
from moviepy.video.io.bindings import mplfig_to_npimage
from easydict import EasyDict as edict
import yaml

from shapely.geometry import Point, Polygon, LineString
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import (
    HuberRegressor,
    LinearRegression,
    RANSACRegressor,
    TheilSenRegressor,
)

class Autils:
    def __init__(self):
        
        pass

    def PrintTable(self, table_heads: list, info_dict: dict):
        """
        args:
            table_heads: contents of table heads. ex:table_header = ["class", "iou"]
            info_dict: infomation contained by dictionay
        return:
            fancy grid table
        """
        
        exp_table = [
            (str(k), str(v))
            for k, v in info_dict.items()
        ]
        
        print(tabulate(exp_table,headers=table_heads,tablefmt="fancy_grid"))

    def IsDirPath(self, dir_path:str)->bool:
        """
        args:
            dir_path: path of directory.
        return:
            bool value represent whether the directory is valid.
        """
        if os.path.isdir(dir_path) and os.path.exists(dir_path):
            return True
        else:
            print("image's directory invalid!")
            return False

    def IsFilePath(self, file_path:str)->bool:
        """
        args:
            file_path: path of a file
        return:
            bool value repesent whether the file is valid.
        """
        if os.path.isfile(file_path) and os.path.exists(file_path):
            return True
        else:
            return False

    def GetImgPaths(self, imgs_dir:str)->list:
        """
        args:
            imgs_dir: directory of images.
        return:
            list of image paths.
        """
        if not self.IsDirPath(imgs_dir):
            return []

        img_paths = list(imutils.paths.list_images(imgs_dir))
        return img_paths

    def GetImgsNamePath(self, imgs_dir:str, with_suffix)->dict:
        """
        args:
            imgs_dir: directory of images.
            with_suffix: return dictionary's key whether contain image's suffix.
        return:
            dictionary of image's name and matched path.
        """
        imgs_dict = {}
        if not self.IsDirPath(imgs_dict):
            return imgs_dict
            
        img_paths = self.GetImgPaths(imgs_dir)
        for img_path in tqdm(img_paths):
            if with_suffix:
                base_name = os.path.basename(img_path)
            else:
                base_name = os.path.basename(img_path)[:-4]
            imgs_dict[base_name] = img_path
        return imgs_dict
    
    def GetFilePaths(self, file_dir:str, file_type:str)->list:
        """
        args:
            file_dir: directory of files.
            file_type: file's type, ex:".txt",".json",...
        """
        if not self.IsDirPath(file_dir):
            return []

        json_paths = list(imutils.paths.list_files(file_dir, validExts=file_type))
        return json_paths

    def ReadJsonFile(self, json_path:str):
        """
        args:
            json_path: json file's path.
        return:
            json file's data.
        """
        if not os.path.exists(json_path):
            return None
        try:
            with open(json_path, 'r', encoding="utf-8") as f:
                js_data = json.load(f)
        except:
            return None
        return js_data

    def ReadXMLFile(self, xml_path:str):
        """
        args:
            xml_path: xml file's path.
        return:
            xml file's data.
        #get node values
        for annot in root.iter('image'):
            img_id = annot.get("name")
            id = int(annot.get("id"))
        """
        if not self.IsFilePath(xml_path): return None

        tree = ET.parse(xml_path)
        root_node = tree.getroot()

        return root_node

    def ReadYMLFile(self, yml_path:str):
        """
        Read yaml file data to dict.
        args:
            yml_path: yaml file path
        """
        cfg = yaml.load(open(yml_path, 'r').read(), Loader=yaml.FullLoader)
        cfg = edict(cfg)
        return cfg

    def WriteYML(self, data:dict, yml_path):
        """
        Write dict data to yaml file.
        args:
            data: data to write file.
            yml_path: yaml save path.
        """
        with open(yml_path, 'w') as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False, sort_keys=False)
    
    def MkDir(self, dir_path:str)->None:
        """
        args:
            dir_path: directory of want to create
        return:
            None
        """
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print("Maked directory: {}".format(dir_path))
        else:
            print("Directory have exist!")

    def RmDir(self, dir_path:str)->None:
        """
        args:
            dir_path: directory of want to remove
        return:
            None
        """
        if not self.IsDirPath(dir_path):
            shutil.rmtree(dir_path)
        else:
            print("Directory have exist!")
    
    def GenUUID(self,)->str:
        return str(uuid.uuid4().hex)

    def ShuffleList(self,src_list:list):
        random.shuffle(src_list)

    def SaveJsonData(self, js_data, save_path:str):
        """
        args:
            js_data: json format data
            save_path: json file path
        """
        with open(save_path, "w", encoding='utf-8') as f:
            json.dump(js_data, f, indent=4, ensure_ascii=False)

    def ConcateTxts(self, txt_paths:list[str], dst_path:str, mode="rewrite"):
        """
        merge all contents of some txt files to a new txt file.
        
        args:
            txt_paths: list of source txt file paths.
            dst_path:  path of output txt file.
            mode: write output file's mode.
             ('rewrite': create a new file; 'append': append conents to the output file.)

        """
        assert mode in ["rewrite", "append"]

        src_lines = []
        for txt_path in txt_paths:
            assert self.IsFilePath(txt_path), "{} invalid".format(txt_path)
            with open(txt_path, 'r') as f:
                src_lines.extend(list(f.readlines()))

        if not self.IsDirPath(os.path.dirname(dst_path)):
            self.MkDir(os.path.dirname(dst_path))
            print("Output directory have maked.")
        
        open_mode = 'w' if mode == "rewrite" else "a+"
        with open(dst_path, open_mode) as f:
            for line in src_lines:
                f.write(line)
   
    #-----math
    def CalTwoPtsDist(self,p1, p2)->float:
        """
        args:
            p1, p2: two points.
        return:
            distance of two points.
        """
        return  np.linalg.norm(np.array(p1)-np.array(p2))

    def CalLineLength(self,pts:list)->float:
        """
        args:
            pts: list of points.
        return:
            length of a line with some points.
        """
        assert len(pts) > 1, "number of pts must larger than 2"
        length = 0.0
        for i in range(len(pts) - 1):
            length += self.CalTwoPtsDist(pts[i], pts[i+1])

        return length

    def calImgBoarderPtOnLine(self,pt1, pt2, img_size):
        #计算由两点确定的直线的向图像底部的延伸线与图像边缘的交点
        """
        ax + by = c   // 线性方程
        由两点(x1,y1),(x2,y2)确定的参数
        a=(y2-y1)
        b=(x1-x2)
        c=ax1+by1
        ==> x = (c - by) / a 
        ==> y = (c - ax) / b
        """
        assert pt1[1] > pt2[1]  # pt1.y > pt2.y

        x1, y1 = pt1
        x2, y2 = pt2
        img_h, img_w = img_size
        a = y2 - y1
        b = x1 - x2
        c = a*x1 + b*y1

        if a == 0:
            return [(x1, img_h-2),(x1, 1)] # 竖直线：返回位于直线上的图像底部及顶部边缘点
        if b == 0:
            return [(1, y1), (img_w-2, y1)] # 水平线：返回位于直线上的图像左右边缘点

        x = (c - b * (img_h-1)) / a
        if x >=0 and x < img_w:
            return [(x, img_h-1)] # 返回位于直线上图像底部的边缘点
        y = (c - a * 0) / b
        if y > y1 and y < img_h:
            return [(0, y)] # 返回位于直线上图像左边缘点
        y = (c - a * (img_w-1))/b
        if y > y1 and y < img_h:
            return [(img_h-1, y)] # 返回位于直线上图像右边缘点

        return None

    def CalPt2LineDist(self,p1, p2, p):
        """
        args:
            p1, p2: a line ditermined by this two points .
            p: a single point.
        return:
            distance of point p to line determined by p1 and p2.
        """
        # distance of pt to the line (p1, p2)
        p1, p2, p = np.array(p1), np.array(p2), np.array(p)
        return np.abs(np.linalg.norm(np.cross(p2-p1, p1-p)))/np.linalg.norm(p2-p1)

    def CalPtNearImgBoarder(self, pt,img_size,near_thres=5)->bool:
        ##判断点与图像的左，右，上，下四个边缘是否靠近
        """
        args:
            pt: a single point.
            img_size: image's size with (img_h, img_w).
            near_thre: threshold whether point locate in boarder.
        """

        h, w = img_size
        boarder_polygon = [[0,0],[0,h-1],[w-1,h-1], [w-1,0]]
        dst_pt = Point(pt)
        boarder_region =  Polygon(boarder_polygon)

        return boarder_region.exterior.distance(dst_pt) <= near_thres

    def CalLineSlop(self, xs, ys)->float:
        """
        args:
            xs: x coorninates of two points.
            ys: y coorninates of two points.
        return:
            the slop of a line determined by two points.
        """
        assert len(xs)==2 and len(ys)==2 
        if xs[0] == xs[1]:
            return 0.0
        else:
            slope = np.polyfit(xs,ys,1)[0]
        return slope

    def CalLineAngle(self, xs, ys)->float:
        """
        args:
            xs: x coorninates of two points.
            ys: y coorninates of two points.
        return:
            angle of a line determined by two points.
        """
        assert len(xs)==2 and len(ys)==2 
        angle = np.rad2deg(np.arctan2(ys[-1] - ys[0], xs[-1] - xs[0]))
        return angle

    def Interp1d(self,ys,xs, fit_order)->list:
        """
        #以y为自变量拟合x
        #y: samll -> large
        args:
            xs: x coorninates of two points.
            ys: y coorninates of two points.
        return:
            interpolated points between of two points
        """
        
        assert ys[1] > ys[0], "ys[1] must larger than ys[0]"
        fit_param = np.polyfit(ys, xs,fit_order)
        fit_xy = np.poly1d(fit_param)
        pts = []
        for y in range(int(ys[0]),int(ys[-1]) , 1):
            pts.append((fit_xy(y), y))

        return pts

    def Inter1dV2(self, xs:list, ys:list, dst_xs:list, dst_ys:list, indep_dim="y", inter_every=True, inter_step=1):
        """
        interpolate points among [(x1,y1), (x2,y2),...,(xn,yn)]
        args:
            xs: x values of all points.
            ys: y values of all points.
            dst_xs: interpolated x values.
            dst_ys: interpolated y values.
            indep_dim: value in ["x", "y"].
            inter_every: interpolate evey two points iteratively.
            inter_step: interpolate step.
        """
        assert indep_dim in ["x", "y"]
        assert len(xs) >=2 and len(ys) >=2
        assert isinstance(dst_xs, list) and isinstance(dst_ys, list)

        xs_parts, ys_parts = [],[]
        if inter_every:
            for i in range(len(xs)-1):
                xs_parts.append([xs[i], xs[i+1]])
                ys_parts.append([ys[i], ys[i+1]])
        else:
            xs_parts.append(xs)
            ys_parts.append(ys)

        for xs_part, ys_part in zip(xs_parts, ys_parts):
            if indep_dim == "x":
                indep_var = xs_part
                dep_var = ys_part
            else:
                indep_var = ys_part
                dep_var = xs_part

            inter_func = scipy.interpolate.interp1d(indep_var, dep_var)
            step = inter_step if indep_var[0] < indep_var[1] else -1*inter_step
            for idx in range(indep_var[0], indep_var[-1], step):
                if indep_dim == "x":
                    dst_xs.append(idx)
                    dst_ys.append(float(inter_func(idx)))
                else:
                    dst_xs.append(float(inter_func(idx)))
                    dst_ys.append(idx)
        dst_xs.append(xs[-1])
        dst_ys.append(ys[-1])

    def RefineLine(self,line, poly_factor, fit_method="RANSAC"):
        """
        args:
            line: a list of points.
            poly_facotr: 1,2,3...
            fit_method: "RANSAC", "HuberRegressor","Theil_Sen","OLS"
        return:
            refined line
        """
        line = np.array(line).astype(float)
        xs,ys = line[:,0], line[:,1]
        ys_fit = ys[:,np.newaxis]
        estimators = [
            ("RANSAC", RANSACRegressor(random_state=42)),
            ("HuberRegressor", HuberRegressor()),
            ("Theil_Sen", TheilSenRegressor(random_state=42)),
            ("OLS", LinearRegression())
        ]
        # poly_factor = 1 if fit_type.get("line") else 2
        fit_types = dict(RANSAC=0, HuberRegressor=1,Theil_Sen=2,OLS=3)
        estimator_type = fit_types.get(fit_method)
        assert estimator_type is not None
            
        model = make_pipeline(PolynomialFeatures(poly_factor), estimators[estimator_type][1])
        model.fit(ys_fit, xs)
        xs_fit = model.predict(ys_fit)

        fit_line = np.concatenate((xs_fit[:,np.newaxis],ys_fit), axis=-1)
        return fit_line

    #---image    

    def ConvertPILimg2numpy(self, pil_img):
        """
        convert pillow image to opencv image format
        args:
            pil_img: pillow format image.
        """
        opencvImage = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

        return opencvImage

    def convertFigure2numpy(self, figure):
        """
        convert matplot figure to opencv image format.
        args:
            figure: matplot format figure.
        """
        numpy_fig = mplfig_to_npimage(figure)

        return numpy_fig

    def ConvertVideoFormat(self, src_path:str, dst_path:str)->None:
        """
        converted video can diplay in web and notion etc.
        args:
            src_path: video's source path.
            dst_path: converted video save path.
        """
        if not self.IsFilePath(src_path):
            print("video path invalid!")
            return
        dir_name = os.path.dirname(dst_path)
        if not self.IsDirPath(dir_name):
            self.MkDir(dir_name)
            print("Save directory created!")
        cmd = "ffmpeg -i {} -vcodec h264 {}".format(src_path, dst_path)
        os.system(cmd) #f'ffmpeg -i "src_path" -vcodec h264 "dst_path"'

    def ConvertVideo2Imgs(self, video_path, save_dir:str)->None:
        """
        args:
            video_path: path of video. if set 0, read from camera.
            save_dir: directory of images to be save.
        """
        self.MkDir(save_dir)
        vs = cv2.VideoCapture(video_path) # 0代表内置摄像头，1，2...代表外置网络摄像头；string代表视频路径
        (W, H) = (None, None)
        
        frame_cnt = 0
        counter = -1

        while True:
            (grabbed, frame) = vs.read()
            if not grabbed:
                break
            
            save_path = os.path.join(save_dir, str(frame_cnt).zfill(6)+".jpg")
            cv2.imwrite(save_path, frame)
            frame_cnt +=1

        print("Convert done!")
        vs.release()

    def ConvertImgs2video(self, imgs_dir:str, video_path:str, dst_imgsize=None, fps=30):
        """
        args:
            imgs_dir: directory of images.
            video_path: video's save path.
            dst_imgsize: if set, customize video image size, else keep origin image size.
        """
        if not self.IsDirPath(imgs_dir):
            print("Directory of images invalid!")
            return

        img_paths = list(imutils.paths.list_images(imgs_dir))
        if len(img_paths) < 2:
            print('Image directory have nothing!')
            return 

        dst_dir = os.path.dirname(video_path)
        if not self.IsDirPath(dst_dir):
            self.MkDir(dst_dir)
            print("Created video path:{}".format(dst_dir))

        if dst_imgsize is not None and isinstance(dst_imgsize, tuple) \
            and dst_imgsize[0] > 10 and dst_imgsize[1] > 10:
            h, w = dst_imgsize
        else:
            img = cv2.imread(img_paths[0])
            h, w = img.shape[:2]

        fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
        writer = cv2.VideoWriter(video_path, fourcc, fps, (w,h))
        
        img_paths = sorted(img_paths, key=lambda k: os.path.basename(k)[:-4])
        for img_path in tqdm(img_paths):
            img = cv2.imread(img_path)
            img = cv2.resize(img, (w,h))
            writer.write(img)

        writer.release()

    def PutTextOnPILImg(self,img, pos:tuple, color, text, text_size=30):
        """
        args:
            img: pillow fomat image
            pos: position of text
            color: text color
            text: text string 
            text_size: text size 

        return: 
            image added text on it 
        """
        font_path = os.path.join(os.path.dirname(__file__), "font/arial.ttf")
        pil_font = ImageFont.truetype(font_path, text_size)
        # img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        
        draw.text(pos,text,color,font=pil_font)

        return img

    def PutChinaText(self, img, text, pos, color=(0, 0, 255), text_size=20):
        """
        args:
            img: numpy array image.
            text: the text to put on image.
            pos: the position of the text on image.
            color: the color of text.
            text_size: text size.
        return:
            numpy array image.
        """
        if isinstance(img, np.ndarray):
            img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img)
        font_path = os.path.join(os.path.dirname(__file__), "font/simsun.ttc") 
        font = ImageFont.truetype(font_path, text_size, encoding='utf-8')
        draw.text(pos, text, color, font=font)

        return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    def RandColor(self,)->tuple:
        """
        return:
            a tuple represent random color.
        """
        b = random.randint(0,255)
        g = random.randint(0,255)
        r = random.randint(0,255)

        return (b,g,r)

    def ConcateImgs(self, imgs_dir1:str, imgs_dir2:str, save_dir:str, concate_type="hconcate")->None:
        """
        args:
            imgs_dir1: directory of images.
            imgs_dir2: directory of images.
            save_dir : directory of concated images.
            concate_type: 'hconcate' or 'vconcate'.
        return:
            concated images in save_dir.
        """
        #---concate images with same basename from two directory
        assert self.IsDirPath(imgs_dir1) and self.IsDirPath(imgs_dir2)
        img_paths1 = list(imutils.paths.list_images(imgs_dir1))
        assert len(img_paths1) > 0

        self.MkDir(save_dir)

        for path1 in img_paths1:
            file_name = os.path.basename(path1)
            path2 = os.path.join(imgs_dir2, file_name)

            if not  os.path.exists(path2):
                continue
            
            img1 = cv2.imread(path1)
            img2 = cv2.imread(path2)
            if img1 is None or img2 is None:continue

            if concate_type == "hconcate":
                img = cv2.hconcat((img1, img2))
            elif concate_type == "vconcate":
                img = cv2.vconcat((img1, img2))
            else:
                raise ValueError("Invalid concate type!")

            save_path = os.path.join(save_dir, file_name)
            cv2.imwrite(save_path, img)


    def VisPickImgs(self, src_imgs_dir:str, dst_imgs_dir:str, show_size=(480,270))->None:
        """
        show and pick images according keyshot.
        args:
        src_imgs_dir: source directory of images.
        dst_imgs_dir: destinate directory of images.
        show_size: visualization window size.
        """

        assert self.IsDirPath(src_imgs_dir), "Source image directory invalid!"
        img_paths = list(imutils.paths.list_images(src_imgs_dir))
        assert  len(img_paths) > 0, "Image number is zero!"
        self.mk(dst_imgs_dir)

        for img_path in tqdm(img_paths):
            img = cv2.imread(img_path)
            if img is None: continue
            h,w = img.shape[:2]
            if show_size is not None:
                assert isinstance(show_size, tuple), "show size invalid"
                assert show_size[0] > 50 and show_size[1] > 50
                img = cv2.resize(img, (show_size[0], show_size[1]))
            
            cv2.imshow("img", img)

            key = cv2.waitKey(100000)
            if key == 102: # "f"
                print("Forward...")
                continue
            elif key == 13: # "Enter"
                img_name = os.path.basename(img_path)
                save_path = os.path.join(dst_imgs_dir, img_name)
                shutil.copy2(img_path, save_path)
                print("Copyed:{} ".format(save_path))
                continue
            elif key == 32: #"space" (pause)
                print("pause!")
                cv2.waitKey(0)
            elif key == 113: #"q" (quit):
                print("exit!")
                break
            else:
                print("Invalid key!")
                continue

if __name__ == "__main__":
    autil = Autils()
    autil.ReadYMLFile("")
    