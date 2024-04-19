# -*- coding: utf-8 -*-

#from _typeshed import Self

from .pypack.fylo.controlserver import Controlserver, ConnectType

class UserApi:
	def __init__(self):
		self._control_server = Controlserver()

#=============================================System Config======================================================================#

	def connect(self, server_ip):
		'''
			描述:
			上位机作为服务器,
			参数:
			connect_type:连接方式 ConnectType.Network 或者 ConnectType.Serial
			返回值:
			True:成功 False:失败
		'''
		return self._control_server.connect(server_ip)

	# scratch
	def single_fly_takeoff(self):
		'''
			描述:
			实时控制飞机起飞
     	'''
		return	self._control_server.single_fly_takeoff()
	
	def single_fly_touchdown(self):
		'''
			描述:
			实时控制飞机降落
		'''
		return self._control_server.single_fly_touchdown()
	
	def single_fly_forward(self, distance):
		'''
			描述:
			实时控制飞机向前飞
			参数:
			distance:飞行距离（厘米）
		'''
		self._control_server.single_fly_forward(distance)
	
	def single_fly_back(self, distance):
		'''
			描述:
			实时控制飞机向后飞
			参数:
			distance:飞行距离（厘米）
		'''
		self._control_server.single_fly_back( distance)
	
	def single_fly_left(self,  distance):
		'''
			描述:
			实时控制飞机向左飞
			参数:
			distance:飞行距离（厘米）
		'''
		self._control_server.single_fly_left( distance)
	
	def single_fly_right(self, distance):
		'''
			描述:
			实时控制飞机向右飞
			参数:
			distance:飞行距离（厘米）
		'''
		self._control_server.single_fly_right( distance)

	def single_fly_up(self,  height):
		'''
			描述:
			实时控制飞机向上飞
			参数:
			distance:飞行高度（厘米）
		'''
		self._control_server.single_fly_up(height)
		
	def single_fly_down(self, height):
		'''
			描述:
			实时控制飞机向下飞
			参数:
			distance:飞行高度（厘米）
		'''
		self._control_server.single_fly_down( height)
		
	def single_fly_turnleft(self, angle):
		'''
			描述:
			实时控制飞机向左转
			参数:
			distance:旋转角度（度）
		'''
		self._control_server.single_fly_turnleft( angle)
		
	def single_fly_turnright(self,  angle):
		'''
			描述:
			实时控制飞机向右转
			参数:
			distance:旋转角度（度）
		'''
		self._control_server.single_fly_turnright(-angle)

	def single_fly_bounce(self, frequency, height):
		'''
			描述:
			实时控制飞机跳起
			参数:
			frequency:弹跳次数
			distance:弹跳距离（厘米）
		'''
		self._control_server.single_fly_bounce(frequency, height)

	def single_fly_straight_flight(self, x, y, z):
		'''
			描述:
			直线飞行(x,y,z)
			参数:
			plane_id:飞机编号
			x:坐标x（厘米）
			y:坐标y（厘米）
			z:坐标z（厘米）
		'''
		self._control_server.single_fly_straight_flight( x, y, z)

	def single_fly_radius_around(self, radius):
		'''
			描述:
			半径环绕飞行
			参数:
			radius：环绕半径(厘米，正：逆时针 负：顺时针)
		'''
		return self._control_server.single_fly_radius_around(radius)
	def single_fly_autogyration360(self,num):
		'''
			描述:
			顺时针、逆时针自转一定圈数
			参数:
			num:(正：逆时针 负：顺时针)
		'''
		return self._control_server.single_fly_autogyration360(num)
	def	single_fly_somersault(self, direction):
		'''
			描述:
			飞机原地向上下前后左右翻滚
			参数:
			num:DIRECTION_FORWARD=0, /* forward. | */
                DIRECTION_BACK=1, /* back. | */
                DIRECTION_LEFT=2, /* left. | */
                DIRECTION_RIGHT=3, /* right. | */
                DIRECTION_DOWN=4, /* down. | */
                DIRECTION_UP=5, /* up. | */
		'''
		return self._control_server.single_fly_somersault(direction)
	def single_fly_curvilinearFlight(self, x, y, z):
		'''
			描述:
			曲线飞行(x,y,z)
			参数:
			x：x轴坐标（厘米）（机体左右，右为正）
			y：y轴坐标（厘米）（机体前后，前为正）
			z：z轴坐标（厘米）（机体上下，上为正）
		'''
		return self._control_server.single_fly_curvilinearFlight(x, y, z)
	
	def single_fly_hover_flight(self, time):
		'''
			描述:
			飞机悬停
			参数:
			time:悬停时间（秒）
		'''
		return self._control_server.single_fly_hover_flight(time)
	
	def single_fly_barrier_aircraft(self, mode ):
		'''
			描述:
			开启避障
			参数:
			mode:True:开启 False:关闭
		'''
		return self._control_server.single_fly_barrier_aircraft(mode)
	
	def single_fly_Line_walking(self,fun_id, dist, tv, way_color):
		'''
			描述:
			巡线检测
			参数:
			fun_id  = 0  //0:向前巡线，无视路口；1：向前巡线，遇到路口结束巡线；2：在路口悬停；3：在轨道上悬停； 10：退出巡线； 现在只有向前巡线
			dist          //距离，单位cm
			tv            //巡线时间，单位s
			way_color   //巡线颜色色域，0-黑色 255-白色
			返回:
			return result = 1; //指令执行的结果：0-失败，1-成功 2-成功遇到路口

		'''	
		return self._control_server.single_fly_Line_walking(fun_id, dist, tv, way_color)
	def single_fly_AiIdentifies(self,mode):
		'''
			描述:
			识别标签
			参数:
			mode:0-9识别0-9的数字标签，10识别左箭头，11识别右箭头，12识别上箭头，13识别下箭头，20结束任务，65-90大写字母A-Z；触发识别后识别过程持续300ms，如果识别成功就立马结束
			返回:
			result；//0 识别失败， 1识别成功

		'''
		return self._control_server.single_fly_AiIdentifies(mode)
	def single_fly_Qrcode_tracking(self,mode, type, time_duration):
		'''
			描述:
			识别二维码
			参数:
			mode://0-9识别0-9的数字二维码，20结束任务，21跟踪二维码（控飞机横移与云台角度） 
            type=1 ;//1 持续跟踪；2二维码识别（触发识别后识别300ms，如果识别到立即返回二维码位置坐标）；3跟踪4s（控飞机横移与云台角度）
	        time_duration //追踪时间s
			返回:
			result；//0 识别失败， 1识别成功

		'''
		return self._control_server.single_fly_Qrcode_tracking(mode, type, time_duration)
	
	def single_fly_Qrcode_align(self, mode, time_duration, search_radius, qr_id):
		'''
			描述:
			识别对齐二维码
			参数:
			mode; /*<  mode： 0 结束任务，1开启下视摄像头二维码对齐并识别二维码，2 下视摄像头识别二维码ID【0，9】但不对齐二维码（识别到就退出）
			time_duration; /*<  time_duration，任务持续时间*/s
            search_radius; /*<  search_radius*/0 close，非0 open explore；search_radius为搜索半径（cm），当激活探索时，飞机在找不到二维码，就在一个小的范围内运动扫描寻找二维码
            qr_id; /*<  qr_id：1:mode=2||mode=12时，识别qr_id的二维码；2:识别到二维码id，外部可根据qr_id执行相应的动作*/ 
			返回:
			result；//0 识别失败， 1识别成功
		'''
		return self._control_server.single_fly_Qrcode_align(mode, time_duration, search_radius, qr_id)
	
	def single_fly_getColor(self, Mode = 1):
		'''
			描述:
			识别标签
			参数:
		    Mode:1开始,跑一帧
			返回:
			r,g,b:色域
            state:0失败 1成功

		'''
		return self._control_server.single_fly_getColor(Mode)
	#灯光
	def	single_fly_lamplight(self, r, g, b, time, mode):
		'''
			描述:
			设置灯光颜色和模式
			不会阻塞主线程
			参数:
		    r,g,b:色域
		    time: 灯光时长/s
		    mode: 12/开灯,13/关灯,16/开启七色RGB闪烁,17/关闭七色RGB闪烁,18/开启流水灯,19/关闭流水灯
			返回:
			True:执行成功
			False:执行失败

		'''
		return	self._control_server.single_fly_lamplight( r, g, b, time, mode)
	
	#8.Linux端业务控制指令
	def Plane_fly_line_walking(self):
        
		return self._control_server.Plane_Linux_cmd(9,1,type,0,0)
	
	def Plane_fly_take_photo(self):
		'''
			描述:
			拍照,必须开启视频流后调用
			参数:
		'''
		return self._control_server.Plane_Linux_cmd(5 ,1 ,0 ,1 ,0)
	def Plane_cmd_swith_rtp(self,type):
		'''
			描述:
			开启视频流
			参数:
			type:0-开启，1-关闭
		'''
		return self._control_server.Plane_Linux_cmd(9,1,type,0,0)
	
	
	def single_fly_flip_rtp(self):
		'''
			描述:
			打开视频流(调用前需开启视频流)
			参数:
			
		'''
		self._control_server.single_fly_flip_rtp()
	def	Plane_cmd_camera_angle(self, type, data):
		'''
			描述:
			设置主摄俯仰角度
			参数:
			type = 0;  // 转动的方向: 0-上,1-下(绝对),2和3算法控制，4-校准，5-积木上，6-积木下（相对）
			data = 30; // 转动的角度: 0~90	
		'''
		return self._control_server.Plane_Linux_cmd(8,1,type,data,0)
	
	


#=================================================Plane Control===================================================================#
		
	def plane_led_on(self, plane_id_start, plane_id_end):
		'''
			描述:
			飞机开灯
			参数:
			plane_id_start:起始飞机编号
			plane_id_end:结束飞机编号
		'''
		self._control_server.plane_led_on(plane_id_start, plane_id_end)
		
	def plane_led_off(self, plane_id):
		'''
			描述:
			飞机关灯
			参数:
			plane_id_start:起始飞机编号
			plane_id_end:结束飞机编号
		'''
		return self._control_server.plane_led_off(plane_id)
	#def plane_fly_arm(self, plane_id_start, plane_id_end):
		'''
			描述:
			低速转动螺旋桨
			参数:
			plane_id_start:起始飞机编号
			plane_id_end:结束飞机编号
		'''
	#	self._control_server.plane_fly_arm(plane_id_start, plane_id_end)	
	def plane_fly_arm(self):
		'''
			描述:
			低速转动螺旋桨
			参数:
			plane_id_start:起始飞机编号
			plane_id_end:结束飞机编号
		'''
		return self._control_server.plane_fly_arm()

	def plane_fly_disarm(self):
		'''
			描述:
			停止低速转动螺旋桨
			参数:
			plane_id_start:起始飞机编号
			plane_id_end:结束飞机编号
		'''
		return self._control_server.plane_fly_disarm()


		
	def Plane_getBarrier(self):
		'''
			描述:
			获取避障信息
			参数:
			
			返回: 字典 每个方向的障碍物状态，True:有障碍物，False:无障碍物
			{
            'forward': True
            'back': True,
            'left': True,
            'right': True,   
            }
		'''
		return self._control_server.Plane_getBarrier()
	def get_battery(self):
		'''
			描述:
			获取飞机电量百分比
			参数:
			plane_id:飞机编号
			返回值:
			整数:电量百分比
		'''
		return self._control_server.get_battery()
		
	def get_coordinate(self):
		'''
			描述:
			获取飞机坐标(x,y,z)
			参数:
			plane_id:飞机编号
			返回值:
			(x, y, z)
		'''
		return self._control_server.get_coordinate()
		
	def get_yaw(self):
		'''
			描述:
			获取飞机偏航角（度）
			参数:
			plane_id:飞机编号
			返回值:
			整数:偏航角
		'''
		return self._control_server.get_yaw()
		

	
	def get_timesync(self):
		'''
			描述:
			判断飞机是否同步时间成功
			参数:
			plane_id:飞机编号
			返回值:
			True:成功 False:不成功
		'''
		return self._control_server.get_timesync()
	

	
	def get_dance_state(self, plane_id):
		'''
			描述:
			判断飞机载入的舞步是否与本地生成舞步一致
			参数:
			plane_id:飞机编号
			返回值:
			True:一致 False:不一致
		'''
		return self._control_server.get_dance_state(plane_id)

	def get_ip(self, plane_id):
		'''
			描述:
			取ip地址
			参数:
			plane_id:飞机编号
			返回值:
			True:一致 False:不一致
		'''
		return self._control_server.get_ip(plane_id)
	def multi_dance_get_update_rate(self):
		'''
			描述:
			获取舞步上传进度（用户接口都是串行处理，舞步传输过程中，如果需要获取进度，则需要在线程中调用该函数进行获取）
			返回值:
			-1:上传错误 飞机舞步上传进度百分比:正常传输
		'''
		return self._control_server.multi_dance_get_update_rate()
	#=====================================================Debug==================================================================#

	def show_plane(self):
		'''
			描述:
			打印飞机各项状态
		'''
		self._control_server.show_plane()
		
	def show_plane_sensor(self):
		'''
			描述:
			打印飞机传感器状态
		'''
		self._control_server.show_plane_sensor()

	def show_station(self):
		'''
			描述:
			打印基站标定结果
		'''
		self._control_server.show_station()




################################################