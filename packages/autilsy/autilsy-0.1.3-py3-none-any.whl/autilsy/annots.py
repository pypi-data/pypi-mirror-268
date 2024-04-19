import os
from common import Autils

class Annot(Autils):
    def __init__(self):
        super().__init__()

     #------annot formats
    def DecodePolyline(self, polyline):
        pts = []
        label = polyline.get("label")
        points = polyline.get("points")
        points = points.split(";")
        for pt in points:
            x, y = pt.split(",")
            pts.append([float(x),float(y)])
            #pts.append({"x": x, "y":y})
        return label, pts

    def GetCVATannots(self, xml_path:str)->list:
        """
        args:
            xml_path: CVAT xml file path.
        return:
            cvat xml annotations.
        """
        all_annots = []
        if not os.path.exists(xml_path):
            print("{} does't exist!".format(xml_path))
            return all_annots
       
        root_node = self.ReadXMLFile(xml_path)
        if root_node is None:
            print("xml root node invalid!")
            return all_annots

        
        for annot in root_node.iter('image'):
            img_id = annot.get("name")
            file_name = img_id.split(os.path.sep)[-1]
            width = int(float(annot.get("width")))
            height= int(float(annot.get("height")))

            lines_info = {}
            lines_info["file_name"] = file_name
            lines_info["imageHeight"] = height
            lines_info["imageWidth"] = width
            lines_info["annots"] = []
            for polyline in annot.iter('polyline'):
                label, pts = self.DecodePolyline(polyline)
                lines_info["annots"].append(dict(label=label, pts=pts))

            all_annots.append(lines_info)

        return all_annots

    def CreateLabelmeProto(self,):
        "create common format labelme proto"
        labelme_annot = {}
        labelme_annot["shapes"] = []
        #labelme_annot["version"] = "5.0.2"
        labelme_annot["version"] = "3.16.7"
        labelme_annot["flags"] = {}
        labelme_annot["imagePath"] = ""
        labelme_annot["imageHeight"] = -1
        labelme_annot["imageWidth"] = -1
        labelme_annot["imageData"] = None
        labelme_annot["relations"] = None
        labelme_annot["lineColor"]=[0,255,0,128]
        labelme_annot["fillColor"]=[255,0,0,128]

        return labelme_annot

    def CreateLabelmeShapeProto(self,):
        "create common labelme single shape proto"
        line_annot = {}
        line_annot["label"] = ""
        line_annot["line_color"] = None,
        line_annot["fill_color"] = None,
        line_annot["points"] = []
        line_annot["uuid"] = ""
        line_annot["shape_type"] = "linestrip"
        line_annot["flags"] = {}
        line_annot["group_id"] =  None
        line_annot["in_freespace"] = None

        return line_annot

        
        
    
