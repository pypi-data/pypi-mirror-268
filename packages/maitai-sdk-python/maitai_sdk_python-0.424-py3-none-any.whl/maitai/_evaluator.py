import json
import asyncio
import threading
import aiohttp
import ssl
from maitai._eval_request import EvalRequestEncoder
from maitai._config import config
from maitai import MaiTaiObject, EvalRequest


class Evaluator(MaiTaiObject):

    MAITAI_HOST = 'https://maitai.ai.yewpay.com'

    def __init__(self):
        super().__init__()

    @classmethod
    def evaluate(cls, session_id, reference_id, action_type, content, application_id=None, application_ref_name=None):
        if application_id is None and application_ref_name is None:
            raise Exception('application_id or application_ref_name must be provided')
        eval_request: EvalRequest = cls.create_eval_request(application_id, application_ref_name, session_id, reference_id, action_type, content)
        cls.run_async(cls.send_evaluation_request(eval_request))

    @classmethod
    def create_eval_request(cls, application_id, application_ref_name, session_id, reference_id, action_type, content):
        if type(content) != str:
            raise Exception('Content must be a string')
        eval_request: EvalRequest = EvalRequest()
        eval_request.application_id = application_id
        eval_request.application_ref_name = application_ref_name
        eval_request.session_id = session_id
        eval_request.reference_id = reference_id
        eval_request.action_type = action_type
        eval_request.evaluation_content = content
        eval_request.evaluation_content_type = 'text'
        return eval_request

    @classmethod
    def update_session_context(cls, session_id, context, application_id = None, application_ref_name = None):
        if type(context) != dict:
            raise Exception('Context must be a dictionary')
        if application_id is None and application_ref_name is None:
            raise Exception('application_id or application_ref_name must be provided')
        session_context = {
            'application_id': application_id,
            'application_ref_name': application_ref_name,
            'session_id': session_id,
            'context': context
        }
        cls.run_async(cls.send_session_context_update(session_context))

    @classmethod
    def append_session_context(cls, session_id, context, application_id = None, application_ref_name = None):
        if type(context) != dict:
            raise Exception('Context must be a dictionary')
        if application_id is None and application_ref_name is None:
            raise Exception('application_id or application_ref_name must be provided')
        session_context = {
            'application_id': application_id,
            'application_ref_name': application_ref_name,
            'session_id': session_id,
            'context': context
        }
        cls.run_async(cls.send_session_context_append(session_context))

    @classmethod
    def update_application_context(cls, context, application_id = None, application_ref_name = None):
        if type(context) != dict:
            raise Exception('Context must be a dictionary')
        if application_id is None and application_ref_name is None:
            raise Exception('application_id or application_ref_name must be provided')
        application_context = {
            'application_id': application_id,
            'application_ref_name': application_ref_name,
            'context': context
        }
        cls.run_async(cls.send_application_context_update(application_context))

    @classmethod
    def append_application_context(cls, context, application_id = None, application_ref_name = None):
        if type(context) != dict:
            raise Exception('Context must be a dictionary')
        if application_id is None and application_ref_name is None:
            raise Exception('application_id or application_ref_name must be provided')
        application_context = {
            'application_id': application_id,
            'application_ref_name': application_ref_name,
            'context': context
        }
        cls.run_async(cls.send_application_context_append(application_context))

    @classmethod
    async def send_evaluation_request(cls, eval_request):
        async def send_request():
            try:
                host = cls.MAITAI_HOST
                url = f'{host}/evaluation/request'
                headers = {
                    'Content-Type': 'application/json',
                    'x-api-key': config.api_key
                }
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                    async with session.post(url, headers=headers, data=json.dumps(eval_request, cls=EvalRequestEncoder)) as response:
                        if response.status != 200:
                            error_text = await response.text()
                            print(f"Failed to send evaluation request. Status code: {response.status}. Error: {error_text}")
                        else:
                            print(f"Successfully sent evaluation request. Status code: {response.status}")
            except Exception as e:
                print(f"An error occurred while sending evaluation request: {e}")

        await send_request()

    @classmethod
    async def send_session_context_update(cls, session_context):
        async def send_context():
            try:
                host = cls.MAITAI_HOST
                url = f'{host}/context/session'
                headers = {
                    'Content-Type': 'application/json',
                    'x-api-key': config.api_key
                }
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                    async with session.put(url, headers=headers, data=json.dumps(session_context)) as response:
                        if response.status != 200:
                            error_text = await response.text()
                            print(f"Failed to send session context update. Status code: {response.status}. Error: {error_text}")
                        else:
                            print(f"Successfully sent session context update. Status code: {response.status}")
            except Exception as e:
                print(f"An error occurred while sending session context update: {e}")

        await send_context()

    @classmethod
    async def send_session_context_append(cls, session_context):
        async def send_context():
            try:
                host = cls.MAITAI_HOST
                url = f'{host}/context/session/append'
                headers = {
                    'Content-Type': 'application/json',
                    'x-api-key': config.api_key
                }
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                    async with session.put(url, headers=headers, data=json.dumps(session_context)) as response:
                        if response.status != 200:
                            error_text = await response.text()
                            print(f"Failed to send session context for append. Status code: {response.status}. Error: {error_text}")
                        else:
                            print(f"Successfully sent session context for append. Status code: {response.status}")
            except Exception as e:
                print(f"An error occurred while sending session context for append: {e}")

        await send_context()

    @classmethod
    async def send_application_context_update(cls, application_context):
        async def send_context():
            try:
                host = cls.MAITAI_HOST
                url = f'{host}/context/application'
                headers = {
                    'Content-Type': 'application/json',
                    'x-api-key': config.api_key
                }
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                    async with session.put(url, headers=headers, data=json.dumps(application_context)) as response:
                        if response.status != 200:
                            error_text = await response.text()
                            print(f"Failed to send application context update. Status code: {response.status}. Error: {error_text}")
                        else:
                            print(f"Successfully sent application context update. Status code: {response.status}")
            except Exception as e:
                print(f"An error occurred while sending application context update: {e}")

        await send_context()

    @classmethod
    async def send_application_context_append(cls, application_context):
        async def send_context():
            try:
                host = cls.MAITAI_HOST
                url = f'{host}/context/application/append'
                headers = {
                    'Content-Type': 'application/json',
                    'x-api-key': config.api_key
                }
                async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
                    async with session.put(url, headers=headers, data=json.dumps(application_context)) as response:
                        if response.status != 200:
                            error_text = await response.text()
                            print(f"Failed to send application context for append. Status code: {response.status}. Error: {error_text}")
                        else:
                            print(f"Successfully sent application context for append. Status code: {response.status}")
            except Exception as e:
                print(f"An error occurred while sending application context for append: {e}")

        await send_context()
        
    @classmethod
    def run_async(cls, coro):
        """
        Modified helper method to run coroutine in a background thread if not already in an asyncio loop,
        otherwise just run it. This allows for both asyncio and non-asyncio applications to use this method.
        """
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:  # No running event loop
            loop = None

        if loop and loop.is_running():
            # We are in an asyncio loop, schedule coroutine execution
            asyncio.create_task(coro, name='maitai')
        else:
            # Not in an asyncio loop, run in a new event loop in a background thread
            def run():
                new_loop = asyncio.new_event_loop()
                asyncio.set_event_loop(new_loop)
                new_loop.run_until_complete(coro)
                new_loop.close()
            threading.Thread(target=run).start()

