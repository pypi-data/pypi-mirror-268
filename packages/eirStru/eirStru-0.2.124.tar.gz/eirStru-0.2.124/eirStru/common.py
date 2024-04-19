import re
import uuid
from datetime import datetime, timedelta, date
from enum import Enum
from typing import Optional, Any, List, Dict

from loguru import logger
from pydantic import BaseModel


# 调用返回类型
class RespType(Enum):
    """
    调用返回类型
    """
    task_success = 1  # 任务成功执行，并有结果
    task_normal = 0  # 任务成功执行
    task_failed = -1  # 任务失败/取消
    task_delay = -2  # 任务延迟执行，比如下一次执行时间5min后
    task_stock_limit = -3  # 无库存
    session_expired = -11  # session过期
    session_invalid_token = -12  # 无效token
    session_invalid_user = -13  # 无效用户名
    session_invalid_password = -14  # 无效密码
    session_user_blocked = -15  # 用户被冻结
    session_request_limit = -16  # 访问次数受限
    proxy_error = -21  # 代理服务器错误
    timeout_error = -22  # 超时


class ActionType(Enum):
    """
    动作类型
    """

    bill_info = 1  # 提单信息
    ctn_list = 2  # 集装箱列表
    apply_eir = 3  # 申请条码
    print_eir = 4  # 打印条码


class BillStatus(Enum):
    canceled = -1  # 已取消
    unknown = 0  # 未知
    inited = 1  # 已订舱
    applied = 2  # 已申请
    printed = 3  # 已打印


def get_f_time(action):
    if action == ActionType.bill_info:
        return 'last_bill_info_time'
    elif action == ActionType.ctn_list:
        return 'last_ctn_list_time'
    elif action == ActionType.apply_eir:
        return 'last_apply_eir_time'
    else:
        return 'last_print_eir_time'


class ResponseData(BaseModel):
    """
    响应类
    """
    code: Optional[RespType] = None
    msg: Optional[str] = ''
    data: Optional[Any] = None  # 转换后的数据
    response: Optional[Any] = None  # 原始响应
    log: Optional[bool] = False  # 是否打印日志

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if (self.msg or self.data):
            if self.code == RespType.task_success:
                logger.warning(f'{self.msg} {self.data if self.data else ""}')
            elif self.code == RespType.task_failed:
                logger.error(f'{self.msg} {self.data if self.data else ""}')
            else:
                logger.info(f'{self.msg} {self.data if self.data else ""}')

    def __str__(self):
        return f'{self.code.name} {self.msg} {self.data if self.data else ""}'


class SessionData(BaseModel):
    """
    session信息
    """
    session_guid: Optional[str] = None
    carrier_id: Optional[str] = None
    account: Optional[str] = None
    sub_code: Optional[str] = None
    bookingagent_id: Optional[str] = None
    proxy_id: Optional[str] = None
    data: dict = {}
    lock_id: Optional[str] = None  # 锁ID
    login_time: Optional[float] = None
    last_access_time: Optional[float] = None
    last_access_resp_type: Optional[RespType] = RespType.task_normal

    def __init__(self, **data: Any):
        super().__init__(**data)
        if not data.get('session_guid'):
            self.session_guid = uuid.uuid4().hex

    def __str__(self):
        return f'{self.carrier_id}-{self.session_guid}'

    @property
    def redis_session_key(self):
        return f'{self.carrier_id}:{self.account}:{self.session_guid}'


class EirTaskInfo(BaseModel):
    """
    创建EirOrder参数
    """
    order_guid: Optional[str] = None
    carrier_id: Optional[str] = ''  # 船公司
    bookingagent_id: Optional[str] = ''  # 一代
    account: Optional[str] = ''  # 账号
    password: Optional[str] = ''  # 密码
    bill_no: Optional[str] = ''  # 提单号
    valid_code: Optional[str] = ''  # 校验码

    apply_ctntypedigit: Optional[str] = ''  # 需一次性申请的箱型箱量
    ctntype_id: Optional[str] = ''  # 箱型
    ctn_digit: Optional[int] = 0  # 箱量
    client_user: Optional[str] = ''  # 客户用户名
    client_user_openid: Optional[str] = ''  # 客户用户Openid用于推送

    callback_url: Optional[str] = ''  # 回调url
    notify_email: Optional[str] = ''

    begin_time: Optional[datetime] = datetime.strptime(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
                                                       '%Y-%m-%d %H:%M:%S')  # 刷箱开始时间
    end_time: Optional[datetime] = datetime.strptime(
        datetime.strftime(datetime.now() + timedelta(hours=4), '%Y-%m-%d %H:%M:%S'),
        '%Y-%m-%d %H:%M:%S')  # 刷箱结束时间
    plan_amount: Optional[int] = 0  # 计划数 todo
    memo: Optional[str] = None  # 备注
    cyname: Optional[str] = None  # 推荐堆场
    account_list: Optional[List[dict]] = []
    vessel: Optional[str] = None
    voyage: Optional[str] = None

    def log(self, msg: str) -> str:
        logger.info(f'{self} {msg}')
        return msg

    def __str__(self):
        return f'{self.carrier_id} {self.bill_no}'


class CtnInfo(BaseModel):
    """
    集装箱信息
    """
    bill_no: Optional[str] = None  # 提单号
    ctn_id: Optional[str] = None  # 集装箱号
    ctntype_id: Optional[str] = None  # 箱型
    is_applied: Optional[bool] = None  # 是否已申请
    is_printed: Optional[bool] = None  # 是否已打印
    is_taken: Optional[bool] = None  # 是否已提箱
    order_guid: Optional[str] = None  # 完成的订单号
    ctn_data: Optional[dict] = {}  # 服务器返回的集装箱数据
    barcode_data: Optional[dict] = {}  # 条码信息
    barcode: Optional[str] = None
    desc: Optional[str] = ''


class CtnListData(BaseModel):
    data: Optional[List[CtnInfo]] = []


class CtnTypeDigit(BaseModel):
    """
    箱型箱量
    """
    ctntype_id: Optional[str] = None  # 箱型
    ctn_digit: Optional[int] = 0  # 箱量
    ctn_digit_applied: Optional[int] = 0  # 已申请量
    ctn_digit_printed: Optional[int] = 0  # 已打印量
    ctn_digit_for_apply: Optional[int] = 0  # 可申请量，未申请
    ctn_digit_for_print: Optional[int] = 0  # 可打印量，已申请未打印
    ctn_digit_need_apply: Optional[int] = 0  # 总申请量,订单传过来的，
    yard_info: Optional[Dict] = {}  # 用于msk，指定堆场

    # 总申请量>0 本次需申请量=总申请量-已申请量, 总申请量=0 本次申请量=箱量-可打印量
    # 本次打印量=min(可打印量,箱量)
    def __str__(self):
        return f'{self.ctn_digit}x{self.ctntype_id.upper()}'


def convert_ctntype_tolist(ctntype_id, ctn_digit=1):
    """
    将箱型箱量字符串1x20gp;2x40gp，转化为箱型箱量列表
    @return:
    """
    ctntypedigit_list = []
    if not ctntype_id:
        return ctntypedigit_list

    ctntype_id = ctntype_id.upper()

    # 如果未输入箱量并且箱型不符合 1x20GP 这样的格式,将ctntypedigit_list清空
    if not ctn_digit and not re.search('[xX]', ctntype_id):
        return ctntypedigit_list

    if ctntype_id.find('X') != -1:
        for item in re.split(r'[;,]', ctntype_id):
            if item:
                lst = re.split(r'[xX]', item)
                ctntypedigit = CtnTypeDigit()
                if lst[0].isdigit():
                    ctntypedigit.ctntype_id = lst[1]
                    ctntypedigit.ctn_digit = int(lst[0])
                else:
                    ctntypedigit.ctntype_id = lst[0]
                    ctntypedigit.ctn_digit = int(lst[1])
                ctntypedigit_list.append(ctntypedigit)
    elif ctntype_id:
        ctntypedigit = CtnTypeDigit()
        ctntypedigit.ctntype_id = ctntype_id
        ctntypedigit.ctn_digit = ctn_digit
        ctntypedigit_list.append(ctntypedigit)
    return ctntypedigit_list


# 检查箱型箱量是否和集装箱列表匹配


class EirOrder(BaseModel):
    order_guid: Optional[str] = None
    task_info: Optional[EirTaskInfo] = None
    carrier_id: Optional[Any] = None  # 船公司
    bill_no: Optional[Any] = None  # 提单号
    booking_no: Optional[Any] = None  # 订舱号
    cyname: Optional[str] = None  # 推荐堆场

    ctntype_id: Optional[str] = ''  # 箱型
    ctn_digit: Optional[int] = 0  # 箱量
    apply_ctntypedigit: Optional[str] = ''  # 需一次性申请的箱型箱量

    begin_time: Optional[datetime] = datetime.strptime(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
                                                       '%Y-%m-%d %H:%M:%S')  # 刷箱开始时间
    end_time: Optional[datetime] = datetime.strptime(
        datetime.strftime(datetime.now() + timedelta(hours=4), '%Y-%m-%d %H:%M:%S'),
        '%Y-%m-%d %H:%M:%S')  # 刷箱结束时间

    bookingagent_id: Optional[Any] = None  # 账号对应的订舱代理
    vessel: Optional[Any] = None  # 船名
    voyage: Optional[Any] = None  # 航次

    ctntypedigit_list: List[CtnTypeDigit] = []  # eir订单箱型箱量
    is_canceled: bool = False
    is_disabled: bool = False
    is_completed: bool = False

    internal_ctns: List[CtnInfo] = []  # 集装箱列表

    def check_ctntype_id(self, ctntype_id, ctn_list):
        set1 = set(map(lambda ctn: ctn.ctntype_id, ctn_list))
        ctntypedigit_list = convert_ctntype_tolist(ctntype_id)
        set2 = set(map(lambda ctntypedigit: ctntypedigit.ctntype_id, ctntypedigit_list))

        if set2 - set1 and len(set1) == 1 and len(set2) == 1:
            ctntype_id = ctntype_id.replace(list(set2)[0], list(set1)[0])
            return ResponseData(code=RespType.task_success, msg=f'{self} 箱型成功转化', data=ctntype_id)
        elif set2 - set1:
            return ResponseData(code=RespType.task_failed, msg=f'{self} 放舱列表中未找到对应箱型，请联系一代')
        else:
            return ResponseData(code=RespType.task_success, msg=f'{self} 箱型匹配', data=ctntype_id)

    def __str__(self):
        return f'{self.carrier_id} {self.bill_no} {self.order_guid if self.order_guid else ""}'

    @property
    def ctns(self) -> List[CtnInfo]:
        return self.internal_ctns

    @ctns.setter
    def ctns(self, value: List[CtnInfo]):
        self.internal_ctns = value
        ctntypedigit_dict = {}

        # 指定箱型箱量模式
        if self.ctntype_id:
            ctntypedigit_list = convert_ctntype_tolist(self.ctntype_id, self.ctn_digit)
            ctntypedigit_dict = {x.ctntype_id: x for x in ctntypedigit_list}

            # cma统一申请模式,更新各箱型 ctn_digit_need_apply
            if self.apply_ctntypedigit:
                apply_ctntypedigit_list = convert_ctntype_tolist(self.apply_ctntypedigit)
                for item in apply_ctntypedigit_list:
                    ctntypedigit = ctntypedigit_dict.get(item.ctntype_id)
                    if ctntypedigit:
                        ctntypedigit.ctn_digit_need_apply = item.ctn_digit
                    else:
                        ctntypedigit_dict.update({item.ctntype_id: item})

        # 更新各箱型已申请量、已打印量
        for ctn in value:
            ctntypedigit = ctntypedigit_dict.get(ctn.ctntype_id)
            if not ctntypedigit:
                ctntypedigit = CtnTypeDigit()
                ctntypedigit.ctntype_id = ctn.ctntype_id
                ctntypedigit_dict.update({ctn.ctntype_id: ctntypedigit})
            if ctn.is_applied:
                ctntypedigit.ctn_digit_applied += 1
            if ctn.is_printed:
                ctntypedigit.ctn_digit_printed += 1

        for item in ctntypedigit_dict.values():

            # 整单模式,不需要申请
            if not self.ctntype_id:
                item.ctn_digit_for_print = item.ctn_digit_applied - item.ctn_digit_printed
                item.ctn_digit_need_apply = 0
            # 指定箱型箱量模式
            else:
                # 本次打印量=min(已申请量-已打印量,箱量)
                item.ctn_digit_for_print = min(item.ctn_digit_applied - item.ctn_digit_printed, item.ctn_digit)

                # 总申请量=0 本次申请量=箱量-可打印量
                if item.ctn_digit_need_apply == 0 and item.ctn_digit > item.ctn_digit_applied - item.ctn_digit_printed:
                    item.ctn_digit_for_apply = item.ctn_digit - item.ctn_digit_applied + item.ctn_digit_printed
                # 总申请量>0 本次需申请量=总申请量-已申请量
                elif item.ctn_digit_need_apply > item.ctn_digit_applied:
                    item.ctn_digit_for_apply = item.ctn_digit_need_apply - item.ctn_digit_applied

        self.ctntypedigit_list = list(ctntypedigit_dict.values())

    @property
    def status(self) -> BillStatus:
        if self.is_canceled or self.is_canceled:
            return BillStatus.canceled
        elif not self.bill_info or not self.bill_info.voyage:
            return BillStatus.unknown
        elif self.ctns and self.ctns_for_print():
            return BillStatus.printed
        elif self.ctns and self.ctns_for_apply():
            return BillStatus.applied
        else:
            return BillStatus.inited

    def check_completed(self):
        """
        不需要申请，不需要打印
        """
        return not (self.need_apply or self.need_print)

    def ctns_for_apply(self):
        """
        获得待申请集装箱清单，整单则返回所有，按箱型则返回该箱型实际需求量
        @return:
        """
        if self.ctntypedigit_list:
            ctns = []
            for ctntypedigit in self.ctntypedigit_list:
                if ctntypedigit.ctn_digit_for_apply:
                    ctn_list = list(
                        filter(lambda x: x.ctntype_id == ctntypedigit.ctntype_id and not x.is_applied,
                               self.ctns))
                    ctns += ctn_list[:ctntypedigit.ctn_digit_for_apply]
                    return ctns
        else:
            return list(filter(lambda x: not x.is_applied, self.ctns))

    def ctns_for_print(self) -> List[CtnInfo]:
        """
        获得待打印集装箱清单，整单则返回所有，按箱型则返回该箱型实际需求量
        @return:
        """
        if self.ctntypedigit_list:
            ctns = []
            for ctntypedigit in self.ctntypedigit_list:
                if ctntypedigit.ctn_digit_for_print:
                    ctn_list = list(
                        filter(lambda x: x.ctntype_id == ctntypedigit.ctntype_id and x.is_applied and not x.is_printed,
                               self.ctns))
                    ctns += ctn_list[:ctntypedigit.ctn_digit_for_print]
                    return ctns
        else:
            return list(filter(lambda x: x.is_applied and not x.is_printed, self.ctns))

    @property
    def need_apply(self):
        """
        判断本单是否需要申请
        @return:
        """
        if self.ctntypedigit_list:
            return bool(list(filter(lambda x: x.ctn_digit_for_apply, self.ctntypedigit_list)))
        else:
            return bool(list(filter(lambda x: not x.is_applied, self.ctns)))

    @property
    def need_print(self):
        """
        判断本单是否需要打印,未打印的 大于 未申请的 大于 0
        @return:
        """
        if self.ctntypedigit_list:
            return bool(list(filter(lambda x: x.ctn_digit_for_print, self.ctntypedigit_list)))
        else:
            return bool(list(filter(lambda x: x.is_applied and not x.is_printed, self.ctns)))

    @property
    def order_ctntype_digit_describe(self):
        """
        订单箱型箱量描述
        @return:
        """
        return self.ctntypedigit


class AccountInfo(BaseModel):
    carrier_id: Optional[str] = None  # 船公司
    account: Optional[str] = None
    password: Optional[str] = None
    bookingagent_id: Optional[str] = None
    info: dict = {}

    def __str__(self):
        return f'{self.carrier_id} {self.account}'


class SpotParams(BaseModel):
    session_data: Optional[SessionData] = None
    carrier_id: Optional[str] = None
    from_port_id: Optional[str] = None  # 起运港
    to_port_id: Optional[str] = None  # 目的港
    ctntype_id: Optional[str] = None  # 箱型
    begin_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


class SpotData(BaseModel):
    carrier_id: Optional[str] = None
    from_port_id: Optional[str] = None  # 起运港
    to_port_id: Optional[str] = None  # 目的港
    ctntype_id: Optional[str] = None  # 箱型

    spot_id: Optional[str] = None  # spot_id
    vessel: Optional[str] = None  # 船名
    voyage: Optional[str] = None  # 航次
    carrier_line: Optional[str] = None  # 船公司航线
    etd: Optional[date] = None  # 开港日
    eta: Optional[date] = None  # 抵港日
    days: Optional[int] = None  # 航程
    cut_off_datetime: Optional[datetime] = None  # 截港日
    doc_closure_datetime: Optional[datetime] = None  # 截单日
    base_price: Optional[float] = None  # 运费
    spot_price: Optional[float] = None
    last_base_price: Optional[float] = None
    last_spot_price: Optional[float] = None
    spot_info: Optional[dict] = None  # json数据
    spot_time: datetime = datetime.now()  # 报价时间
    carrier_account: Optional[str] = None


class ParamsGetSession(BaseModel):
    carrier_id: Optional[str] = None
    action: Optional[ActionType] = None
    account: Optional[str] = None
    bookingagent_id: Optional[str] = None
    sub_code: Optional[str] = None
    session_guid: Optional[str] = None


class ParamsCheckAccount(BaseModel):
    carrier_id: str = ''  # 船公司
    account: str = ''  # 账号
    password: str = ''  # 密码

    def __str__(self):
        return f'{self.carrier_id}/{self.account}'


class LoginParams(BaseModel):
    carrier_id: str = ''  # 船公司
    account: str = ''  # 账号
    password: str = ''  # 密码
    proxy_id: Optional[str] = None

    def __str__(self):
        return f'{self.carrier_id}/{self.account} {self.proxy_id if self.proxy_id else ""}'


class RespSessionException(Exception):
    def __init__(self, code, msg, detail=None):
        self.code = code
        self.msg = msg
        self.detail = detail

    def __str__(self):
        return f'\n{str(self.code)}\n{self.detail or self.msg}'


class RespProxyException(RespSessionException):
    pass


class RespNetworkException(RespSessionException):
    pass
