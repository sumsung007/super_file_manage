# -*- coding: utf-8 -*-

"""
声明、定义
"""

class RETURN_CODE:
	SUCCESS = "SUCCESS"   # 成功
	FAIL    = "FAIL"      # 失败
	WARNING = "WARNING"	  # 警告


	PRODUCT_REORDER         = "PRODUCT_REORDER"     # 产品重复订购
	PRODUCT_CANT_ORDER      = "PRODUCT_CANT_ORDER"  # 该产品当前无法订购
	PRODUCT_CANT_RENEW      = "PRODUCT_CANT_RENEW"  # 该产品不可续订
	PRODUCT_NOT_ORDERED     = "PRODUCT_NOT_ORDERED" # 产品未订购
	INVALID_FEE_CODE        = "INVALID_FEE_CODE"    # 无效的计费代码
	INVALID_PRODUCT         = "INVALID_PRODUCT"     # 无效的产品代码
	DX_RETURN_FAIL          = "DX_RETURN_FAIL"      # 电信返回订购失败
	PAY_TOO_FAST            = "PAY_TOO_FAST"        # 用户支付频率过快
	USER_PAY_DISABLED       = "USER_PAY_DISABLED"   # 该用户禁止支付
	INVALID_PAY_PASSWD      = "INVALID_PAY_PASSWD"  # 无效的支付密码
	PAY_MONTH_LIMIT         = "PAY_MONTH_LIMIT"     # 达到月消费限额
	INVALID_SIGN            = "INVALID_SIGN"        # 无效的签名
	INVALID_PARAMS          = "INVALID_PARAMS"      # 无效的（请求）参数
	USER_NOT_LOGINED        = "USER_NOT_LOGINED"    # 用户未登录

	CHANNEL_EXISTED_IN_FAVORS    = "CHANNEL_EXISTED_IN_FAVORS"     # 该课件已经在收藏夹中
	CHANNEL_NOTEXISTED_IN_FAVORS = "CHANNEL_NOTEXISTED_IN_FAVORS"  # 该课件没在收藏夹中
	LESSON_EXISTED_IN_FAVORS     = "LESSON_EXISTED_IN_FAVORS"      # 该课程已经在收藏夹中
	LESSON_NOTEXISTED_IN_FAVORS  = "LESSON_NOTEXISTED_IN_FAVORS"   # 该课程没在收藏夹中



class PRODUCT_TYPE:
	"""
	充值（支付）类型。主要用于PaymentOrders
	"""
	ONETIME    = 0  # 单次支付
	MONTHS     = 1  # 包月支付
	DAYS       = 2  # 包日支付

	# MONTHS      = 0  # 包月支付
	# SEASONS     = 1  # 季度支付
	# HALFYEARS   = 2  # 半年支付
	# YEARS       = 3  # 年支付

PRODUCT_TYPE_CHOICES = (
	(PRODUCT_TYPE.ONETIME, "单次支付"),
	(PRODUCT_TYPE.MONTHS,  "包月支付"),
	(PRODUCT_TYPE.DAYS,    "包日支付"),

	# (PRODUCT_TYPE.MONTHS, "包月支付"),
	# (PRODUCT_TYPE.SEASONS, "季度支付"),
	# (PRODUCT_TYPE.HALFYEARS, "半年支付"),
	# (PRODUCT_TYPE.YEARS, "年支付"),
)
PRODUCT_TYPE_MAPS = dict(PRODUCT_TYPE_CHOICES)


class PAY_STATE:
	"""
	充值（支付）状态。主要用于PaymentOrders
	"""
	WAITING = 0  # 等待中
	SUCCESS = 1  # 成功
	FAIL    = 2  # 失败


class PAY_TYPE:
	"""
	支付类型（如支付宝支付、微信扫码支付等等）
	"""
	UNKNOWN    = 0  # 未知
	PT_RMB     = 1  # 运营商平台RMB支付
	PT_SCORE   = 2  # 运营商平台积分支付


class PPID:
	"""
	平台提供商定义
	"""
	UNKNOWN   = 0
	DX        = 1  # 电信
	GD        = 2  # 广电
	LT        = 3  # 联通
	CW        = 4  # 创维


class POH_TYPE:
	"""
	platform of hardware
	硬件平台类型
	"""
	UNKNOWN = 0
	IPTV    = 1
	OTT     = 2

class BP_TYPE:
	"""
	平台业务类型
	"""
	UNKNOWN = 0
	GAME    = 1 # 游戏
	EDU     = 2 # 教育

class VIDEO_PLAY_AUTH:
	"""
	视频播放权限
	"""
	FREE = 0  # 免费
	PAY  = 1  # 付费

# 视频播放权限选择
VIDEO_PLAY_AUTH_CHOICES = (
	(VIDEO_PLAY_AUTH.FREE, "免费播放"),
	(VIDEO_PLAY_AUTH.PAY,  "付费播放"),
)



# 按钮额外标志
LINK_FLAG_CHOICES = (
	(0, "无"),
	(1, "推荐"),
	(2, "新增"),
	(3, "免费"),
	(4, "热门"),
	(5, "活动"),
)

# 首页按钮额外标志对应的图片地址，按上面顺序匹配
LINK_FLAG_IMG_URLS_HOME = (
	"",
	"/static/main/images/common/tips/index/recommend.png",
	"/static/main/images/common/tips/index/new.png",
	"/static/main/images/common/tips/index/free.png",
	"/static/main/images/common/tips/index/hot.png",
	"",
)

# 视频列表按钮额外标志对应的图片地址，按上面顺序匹配
LINK_FLAG_IMG_URLS_LIST = (
	"",
	"/static/main/images/common/tips/recommend.png",
	"/static/main/images/common/tips/new.png",
	"/static/main/images/common/tips/free.png",
	"/static/main/images/common/tips/hot.png",
	"",
)



VERSION_CHOICES = (
	('0.0.0.0',			'0.0.0.0'),
	('0.0.0.1',			'0.0.0.1'),
	('0.0.0.2',			'0.0.0.2'),
)


MAP_DICT = {
	"河北省":['石家庄市','邯郸市','保定市','承德市','唐山市','廊坊市','沧州市','衡水市','邢台市','秦皇岛市','张家口市'],
	"山西省":[],  
	"辽宁省":[],
	"吉林省":[],
	"黑龙江省":[],  
	"江苏省":[],  
	"浙江省":[],  
	"安徽省":[],  
	"福建省":[],  
	"江西省":[],  
	"山东省":[],  
	"河南省":[],  
	"湖北省":[], 
	"湖南省":[],  
	"广东省":[],  
	"海南省":[],  
	"四川省":[],  
	"贵州省":[],  
	"云南省":[],  
	"陕西省":[],  
	"甘肃省":[],  
	"青海省":[],  
	"台湾省":[],
}


TEACHER_LABEL = (
	(0, '初级教师'),
	(1, '中级教师'),
	(2, '高级教师'),
	(3, '特级教师'),
)