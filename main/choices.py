# -*- coding: utf-8 -*-

"""
选择数据定义
"""


# 科目选择
SUBJECT_CHOICES = (
	(1, "语文"),
	(2, "英语"),
	(3, "数学"),
)
SUBJECT_MAPS = dict(SUBJECT_CHOICES[1:])

# 班级选择
CLASS_CHOICES = (
	(1, "小学一年级"),
	(2, "小学二年级"),
	(3, "小学三年级"),
	(4, "小学四年级"),
	(5, "小学五年级"),
	(6, "小学六年级"),
	(7, "初中一年级"),
	(8, "初中二年级"),
	(9, "初中三年级"),
	(10, "高中一年级"),
	(11, "高中二年级"),
	(12, "高中三年级"),
)
CLASS_MAPS = dict(CLASS_CHOICES)

# 学期选择
TERM_CHOICES = (
	(1011, "小学一年级上学期"),
	(1012, "小学一年级下学期"),
	(1021, "小学二年级上学期"),
	(1022, "小学二年级下学期"),
	(1031, "小学三年级上学期"),
	(1032, "小学三年级下学期"),
	(1041, "小学四年级上学期"),
	(1042, "小学四年级下学期"),
	(1051, "小学五年级上学期"),
	(1052, "小学五年级下学期"),
	(1061, "小学六年级上学期"),
	(1062, "小学六年级下学期"),
	(1071, "初中一年级上学期"),
	(1072, "初中一年级下学期"),
	(1081, "初中二年级上学期"),
	(1082, "初中二年级下学期"),
	(1091, "初中三年级上学期"),
	(1092, "初中三年级下学期"),
	(1101, "高中一年级上学期"),
	(1102, "高中一年级下学期"),
	(1111, "高中二年级上学期"),
	(1112, "高中二年级下学期"),
	(1121, "高中三年级上学期"),
	(1122, "高中三年级下学期"),
)
TERM_MAPS = dict(TERM_CHOICES[1:])




class RECOMMEND_TYPE:
	"""
	"""
	Unknown            = 0  # 未知
	ChannlesAndLessons = 1  # 频道和视频列表(Category)
	Lessons            = 2  # 特定频道下的剧集列表(Channel)
	Url                = 3  # html页面
	VideoPlay          = 4  # 视频播放
	Channels           = 5  # 特定分类下的频道列表
	ReciteWords        = 6  # 背单词课本分类列表

RECOMMEND_TYPE_CHOICES = (
	(RECOMMEND_TYPE.Unknown,            "未知"),
	(RECOMMEND_TYPE.ChannlesAndLessons, "频道和视频列表"),
	(RECOMMEND_TYPE.Lessons,            "剧集列表"),
	(RECOMMEND_TYPE.Url,                "html页面"),
	(RECOMMEND_TYPE.VideoPlay,          "视频播放页"),
	(RECOMMEND_TYPE.Channels,           "频道列表"),
	(RECOMMEND_TYPE.ReciteWords,        "背单词课本分类列表"),
)


