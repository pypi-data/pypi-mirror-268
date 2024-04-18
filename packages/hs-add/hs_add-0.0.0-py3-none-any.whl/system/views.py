import time
from itertools import combinations
from utils.prediction import mark_area_points
from utils.change_picture import change_format
from utils.Canny import identify_anwser_condition
from utils.platts_algorithm import find_result, find_offset, center_coordinates
from utils.json_response import SuccessResponse, ErrorResponse
from django.views import View
import numpy as np
import cv2
import json
import os
import sys
import logging
logger = logging.getLogger('server.log')
# 获取当前项目所在的目录
current_dir = os.path.dirname(os.path.abspath('apxwwplication.settings.py'))
# 将目录添加到系统路径中
sys.path.insert(0, os.path.abspath(current_dir))
# from utils.remove_noise_points import PointProcessor


def is_on_line(bbox_list, threshold):
    """
    判断是否在一条直线（直线/竖线）
    :param bbox_list: 包含矩形坐标的列表，每个矩形坐标以 [x1, y1, x2, y2] 的形式给出
    :param threshold: 判断两点在x轴或y轴上的阈值
    :return: 如果所有点都在一条直线上返回True，否则返回False
    """

    center_points = center_coordinates(bbox_list)
    dist_x_list = []
    dist_y_list = []
    # 遍历排序后的中心点列表，检查相邻点之间的距离
    for i in range(len(center_points)-1):
        dist_x = center_points[i+1][0] - center_points[i][0]
        dist_y = center_points[i+1][1] - center_points[i][1]
        # print("点", i, "和点", i+1, "之间的距离为:", dist_x, dist_y)
        dist_x_list.append(abs(dist_x))
        dist_y_list.append(abs(dist_y))

    # 判断是直线还是竖线
    direction = None
    if max(dist_x_list) < threshold:
        # y轴递增
        direction = 'y'
    else:
        # x轴递增
        direction = 'x'
    if max(dist_x_list) > threshold and max(dist_y_list) > threshold:
        return False, None
    return True, direction


# 判断作业区市一条直线找到笔记区为一条直线的
def find_online_answer(coordinates, count):
    # 使用组合函数生成所有可能的5个点的组合
    combinations_list = list(combinations(coordinates, count))
    for combo in combinations_list:
        # print(combo)
        result, direction = is_on_line(combo, 25)
        # print('----',direction)
        if result is True:
            # print('-----', combo)
            return combo


class TestView(View):
    def get(self, request):

        # 学科
        subject = request.GET.get('subject')
        area_path = request.GET.get('area_path')
        answer_path = request.GET.get('answer_path')
        print(subject)
        # 模型地址
        model_path = "./fasterrcnn_resnet50_fpn_v2_yingyu.pth"
        # # 图片来源地址
        images_path = "./data/valid/"
        # 作业区图片
        images_name = [area_path]
        # images_name = ["1.jpg"]
        # 答案图片
        anwser_images_name = [answer_path]
        # anwser_images_name = ["2-1.png"]
        # 保存点位信息的地址
        save_path = './data/condition/'

        # 展示效果图的作业区名称
        show_area_condition_filename = images_path + 'result_'+images_name[0]
        # 展示效果图的答案名称
        show_answer_condition_filename = images_path + \
            'grayscale_'+anwser_images_name[0]

        # 调用模型识别答题区域的坐标
        model_time = time.time()

        mark_area_points(save_path, model_path, images_path, images_name)
        mid_time = time.time()

        # # 将图片添加底色
        # 笔迹图片放大倍数
        scale_factor = 1.33
        format_photos = change_format(
            images_path, anwser_images_name, 'grayscale_', scale_factor)

        # 识别答案区域的坐标
        middle_time = time.time()
        for i in format_photos:
            identify_anwser_condition(save_path, images_path, i)
        second_time = time.time()
        print('识别出笔记区坐标的耗时----', second_time-middle_time)

        # return SuccessResponse(msg='test')
        # # 将两组数据进行普氏算法
        # area_condition = []

        answer_condition = []
        area_condition_filename = images_name[0].replace('jpg', 'json')
        anwser_condition_filename = anwser_images_name[0].replace(
            'png', 'json')
        # 过滤掉噪音点
        # area_condition = eval(request.GET.get('area_condition'))

        with open(save_path+area_condition_filename, 'r', encoding='utf8') as f:

            area_condition = json.loads(f.read())['small']
        with open(save_path+anwser_condition_filename, 'r', encoding='utf8') as f:
            answer_condition = json.loads(f.read())['all']

        if len(area_condition) == 0 or len(answer_condition) == 0:
            print('无坐标数据无法验证')
            return ErrorResponse(msg='无坐标数据无法验证')

        if len(area_condition) < 3 or len(answer_condition) < 3:
            return ErrorResponse(msg='答题区或作业区点小于三个,无法做识别')

        # 判断area_condition 是否在一条直线
        # # 判断是否在一条直线的阈值
        threshold = 15
        result, direction = is_on_line(area_condition, threshold)
        x_translation, y_translation = 0, 0
        angle = 0
        if result is True:
            print('在一条直线', direction)
            # 找出所有的点进行比较
            # with open(save_path+area_condition_filename, 'r', encoding='utf8') as f:
            #     new_area_condition = json.loads(f.read())['boxes']['small']
            print('====', area_condition, '\n', answer_condition)
            result_answers = find_online_answer(
                answer_condition, len(area_condition))
            print('得到的answer', result_answers)
            x_translation, y_translation = find_offset(
                area_condition, result_answers, result)
            angle = 0

        else:
            print('不在一条直线')
            flag = None
            if len(area_condition) <= 5 or len(answer_condition) <= 5:
                # 1.所有的点参与普氏分析
                flag = True

            else:
                flag = False
            # # 计算耗时
            print('====', flag)
            start_time = time.time()
            #  flag -》判断是否是所有的点参与普氏分析
            result = find_result(area_condition, answer_condition,
                                 show_area_condition_filename, show_answer_condition_filename, flag)
            final_time = time.time()

            # # # 缩放比例暂时不加
            # scale = result[0]
            x_translation = result[2]
            y_translation = result[3]
            angle = result[1]
            print('普氏分析耗时---', final_time-start_time,
                  x_translation, y_translation)
        # 生成用来叠加的带底色的笔迹图
        save_photo = change_format(
            images_path, anwser_images_name, 'overlay_', scale_factor)

        # print('图片生成完毕，开始叠加之前耗时-----',middle_time-start_time)
        # end_time = time.time()
        # 读取两张图片
        image1 = cv2.imread(images_path + images_name[0])
        image2 = cv2.imread(images_path + 'overlay_' + anwser_images_name[0])
        # print(image2.shape)
        # 创建一个空白画布
        canvas_height = 7000
        canvas_width = 7000
        canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)
        # 获取第一张图片的尺寸
        image1_height, image1_width, _ = image1.shape

        # 计算第一张图片在画布中的放置位置（居中）
        image1_x = (canvas_width - image1_width) // 2
        image1_y = (canvas_height - image1_height) // 2

        # 将第一张图片放置在画布中间
        canvas[image1_y:image1_y+image1_height,
               image1_x:image1_x+image1_width] = image1

        # 缩放笔迹图片
        scale_percent = 1.0
        width = int(image2.shape[1] * scale_percent)
        height = int(image2.shape[0] * scale_percent)
        resized_image2 = cv2.resize(
            image2, (width, height), interpolation=cv2.INTER_AREA)
        offset_x = int(x_translation)
        offset_y = int(y_translation)
        # offset_x = 0 # x 方向的偏移量
        # offset_y = 0 # y 方向的偏移量
        # 获取缩放后的第二张图片的尺寸
        resized_image2_height, resized_image2_width, _ = resized_image2.shape

        # 计算第二张图片在画布中的放置位置（左上角与第一张图片对齐）
        image2_x = image1_x + offset_x
        image2_y = image1_y + offset_y

        # 将缩放后的第二张图片放置在第一张图片的对应位置，并透明叠加
        alpha = 0.8  # 笔迹图片透明度为80%
        overlay = canvas.copy()
        overlay[image2_y:image2_y+resized_image2_height,
                image2_x:image2_x+resized_image2_width] = resized_image2
        cv2.addWeighted(overlay, alpha, canvas, 1 - alpha, 0, canvas)

        # # 调整窗口大小使其适应屏幕

        # cv2.imshow("Canvas with Images", canvas)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()xwwww

        # 保存展示的结果
        save_path = "./data/result/"
        cv2.imwrite(save_path + '叠加后的_'+anwser_images_name[0], canvas)

        # print('总耗时----', final_time-start_time)
        logger.info(f"笔迹图片地址{answer_path},x位移{offset_x}, y位移:{offset_y}")
        data = {'scale': scale_factor, 'angle': angle, 'offset_x': offset_x,
                'offset_y': offset_y, 'answer_condition': answer_condition}
        return SuccessResponse(msg='hello,yingyu', data=data)
