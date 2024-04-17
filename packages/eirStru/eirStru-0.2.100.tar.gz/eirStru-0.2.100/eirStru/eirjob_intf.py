import requests
from aiohttp import ClientSession
from eirStru import *


class EirParams(BaseModel):
    session: Optional[SessionData] = None
    order: Optional[EirOrder] = None


class JobIntf:
    def __init__(self, host):
        self.host = host

    async def do_eir(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        return await self.call_eir_job('do_eir', session_data, order)

    async def get_bill_info(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        resp = await self.call_eir_job('get_bill_info', session_data, order)
        if resp.code == RespType.task_success:
            bill_info = BillInfo(**resp.data)
            bill_info.bookingagent_id = session_data.bookingagent_id
            resp.data = bill_info
            return resp
        return resp

    async def get_ctn_list(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        if not order.booking_no:
            logger.error(f'{order} 没有 bookingno')
            return ResponseData(code=RespType.task_failed, msg=f'{order} 没有 bookingno')
        resp = await self.call_eir_job('get_ctn_list', session_data, order)
        if resp.code == RespType.task_success:
            resp.data = list(map(lambda x: CtnInfo(**x), resp.data))
        return resp

    async def apply_eir(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        if not order.booking_no:
            logger.error(f'{order} 没有 bookingno')
            return ResponseData(code=RespType.task_failed, msg=f'{order} 没有 bookingno')
        return await self.call_eir_job('apply_eir', session_data, order)

    async def print_eir(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        if not order.booking_no:
            logger.error(f'{order} 没有 bookingno')
            return ResponseData(code=RespType.task_failed, msg=f'{order} 没有 bookingno')
        return await self.call_eir_job('print_eir', session_data, order)

    async def call_eir_job(self, job_type, session_data: SessionData, order: EirOrder) -> ResponseData:
        url = f'{self.host}/{job_type}/'
        data = EirParams(session=session_data, order=order)
        # data = {
        #     'session': session_data.model_dump(),
        #     'order': order.model_dump()
        # }
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, data=data.model_dump_json(), verify_ssl=False) as resp:
                    r_json = await resp.json()
                    return ResponseData(**r_json)
        except Exception as e:
            return ResponseData(code=RespType.task_failed, message=f'{order}:{e}')

    async def quote_spot(self, params: SpotParams):
        url = f'{self.host}/quote_spot'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = requests.post(url, headers=headers, data=params.model_dump_json(), verify=False)
        return ResponseData(**response.json())
        # try:
        #     async with ClientSession() as cs:
        #         async with cs.post(url, headers=headers, data=params.model_dump_json(), verify_ssl=False) as resp:
        #             r_json = await resp.json()
        #             return ResponseData(**r_json)
        # except Exception as e:
        #     return ResponseData(code=RespType.task_failed, message=f'{e}')
