import json
import time
from loguru import logger
from aily.openapi import OpenAPIClient

from typing import List, Optional, Dict
from datetime import datetime


class Session:
    def __init__(self, session_id: str, created_at: int, metadata: Optional[str] = None):
        self.id = session_id
        self.created_at = created_at
        self.metadata = metadata

    def __str__(self):
        return f"Session(id={self.id}, created_at={self.created_at}, metadata={self.metadata})"


class Sender:
    def __init__(self, aily_id: str, sender_type: str, identity_provider: str, entity_id: str):
        self.aily_id = aily_id
        self.sender_type = sender_type
        self.identity_provider = identity_provider
        self.entity_id = entity_id

    def __str__(self):
        return f"Sender(aily_id={self.aily_id}, sender_type={self.sender_type}, identity_provider={self.identity_provider}, entity_id={self.entity_id})"


class Message:
    def __init__(self, message_id: str, session_id: str, content_type: str, content: str,
                 sender: Sender, created_at: int, run_id: Optional[str] = None,
                 file_ids: Optional[List[str]] = None, quote_message_id: Optional[str] = None,
                 mentions: Optional[List[dict]] = None, plain_text: Optional[str] = None):
        self.id = message_id
        self.session_id = session_id
        self.content_type = content_type
        self.content = content
        self.sender = sender
        self.created_at = created_at
        self.run_id = run_id
        self.file_ids = file_ids
        self.quote_message_id = quote_message_id
        self.mentions = mentions
        self.plain_text = plain_text

    def __str__(self):
        return f"Message(id={self.id}, session_id={self.session_id}, content_type={self.content_type}, content={self.content}, sender={self.sender}, created_at={self.created_at}, run_id={self.run_id}, file_ids={self.file_ids}, quote_message_id={self.quote_message_id}, mentions={self.mentions}, plain_text={self.plain_text})"


class Run:
    def __init__(self, run_id: str, session_id: str, app_id: str, created_at: int,
                 status: str, start_at: int = None, end_at: int = None,
                 error: Optional[dict] = None, metadata: Optional[str] = None):
        self.id = run_id
        self.session_id = session_id
        self.app_id = app_id
        self.created_at = created_at
        self.status = status
        self.start_at = start_at
        self.end_at = end_at
        self.error = error
        self.metadata = metadata

    def __str__(self):
        return f"Run(id={self.id}, session_id={self.session_id}, app_id={self.app_id}, created_at={self.created_at}, status={self.status}, start_at={self.start_at}, end_at={self.end_at}, error={self.error}, metadata={self.metadata})"


class RunStep:
    def __init__(self, step_id: str, run_id: str, step_type: str, status: str,
                 created_at: int, completed_at: Optional[int] = None,
                 expired_at: Optional[int] = None, failed_at: Optional[int] = None,
                 last_error: Optional[dict] = None, step_details: Optional[dict] = None,
                 usage: Optional[dict] = None):
        self.id = step_id
        self.run_id = run_id
        self.step_type = step_type
        self.status = status
        self.created_at = created_at
        self.completed_at = completed_at
        self.expired_at = expired_at
        self.failed_at = failed_at
        self.last_error = last_error
        self.step_details = step_details
        self.usage = usage

    def __str__(self):
        return f"RunStep(id={self.id}, run_id={self.run_id}, step_type={self.step_type}, status={self.status}, created_at={self.created_at}, completed_at={self.completed_at}, expired_at={self.expired_at}, failed_at={self.failed_at}, last_error={self.last_error}, step_details={self.step_details}, usage={self.usage})"


class SessionAPI:
    def __init__(self, client):
        self.client = client

    def create(self, channel_context=None, metadata=None) -> Session:
        return self.client.create_session(channel_context, metadata)

    def retrieve(self, session_id: str) -> Session:
        return self.client.retrieve_session(session_id)


class MessageAPI:
    def __init__(self, client):
        self.client = client

    def create(self, session_id: str, content: str, content_type: str = 'MDX', idempotent_id: Optional[str] = None,
               file_ids: Optional[List[str]] = None, mentions: Optional[List[dict]] = None,
               quote_message_id: Optional[str] = None) -> Message:
        return self.client.create_message(session_id, content, content_type, idempotent_id,
                                          file_ids, mentions, quote_message_id)

    def list(self, session_id: str, page_size: int = 20, page_token: Optional[str] = None,
             run_id: Optional[str] = None) -> List[Message]:
        return self.client.list_messages(session_id, page_size, page_token, run_id)


class RunAPI:
    def __init__(self, client):
        self.client = client

    def create(self, session_id: str, app_id: str, skill_id: Optional[str] = None,
               skill_input: Optional[dict] = None, metadata: Optional[str] = None) -> Run:
        return self.client.create_run(session_id, app_id, skill_id, skill_input, metadata)

    def retrieve(self, session_id: str, run_id: str) -> Run:
        return self.client.retrieve_run(session_id, run_id)

    def list(self, session_id: str, page_size: int = 20, page_token: Optional[str] = None) -> List[Run]:
        return self.client.list_runs(session_id, page_size, page_token)

    def cancel(self, session_id: str, run_id: str) -> Run:
        return self.client.cancel_run(session_id, run_id)

    def list_steps(self, session_id: str, run_id: str, page_size: int = 20, page_token: Optional[str] = None) -> List[
        RunStep]:
        return self.client.list_run_steps(session_id, run_id, page_size, page_token)


class ChatAPI:
    def __init__(self, client):
        self.client = client

    def create(self, app_id: str, content: str, skill_id: Optional[str] = None, skill_input: Optional[dict] = None,
               channel_context: Optional[dict] = None, meta_data: Optional[dict] = None,
               timeout: int = 60, poll_interval: int = 1) -> Message:
        session = self.client.sessions.create(channel_context=channel_context, metadata=meta_data)

        # 创建消息
        self.client.messages.create(
            session_id=session.id,
            content=content
        )

        # 创建运行
        run = self.client.runs.create(session_id=session.id, app_id=app_id, skill_id=skill_id, skill_input=skill_input)

        # 轮询判断运行状态
        start_time = time.time()
        while True:
            run = self.client.runs.retrieve(session_id=session.id, run_id=run.id)
            if run.status in ["COMPLETED", "FAILED", "CANCELLED", "EXPIRED"]:
                break

            elapsed_time = time.time() - start_time
            if elapsed_time >= timeout:
                logger.warning(f"Run {run.id} timed out after {timeout} seconds.")
                break

            time.sleep(poll_interval)

        # 获取消息列表
        messages = self.client.messages.list(session_id=session.id, run_id=run.id)
        for msg in messages:
            if msg.sender.sender_type == 'ASSISTANT':
                return msg


class FileAPI:
    def __init__(self, client):
        self.client = client

    def upload(self, name: str, mime_type: str, file) -> dict:
        return self.client.upload_file(name, mime_type, file)

    def retrieve(self, file_id: str) -> dict:
        return self.client.retrieve_file(file_id)


class AssistantClient(OpenAPIClient):
    def __init__(self, user_access_token=None, app_id=None, app_secret=None):
        super().__init__(user_access_token, app_id, app_secret)
        self.base_url = "https://open.larkoffice.com/open-apis/aily/v1"
        self.sessions = SessionAPI(self)
        self.messages = MessageAPI(self)
        self.runs = RunAPI(self)
        self.chat_completions = ChatAPI(self)
        self.files = FileAPI(self)  # 新增FileAPI

    def create_session(self, channel_context=None, metadata=None) -> Session:
        logger.info("Creating a new session...")
        url = f"{self.base_url}/sessions"
        data = {}
        if channel_context:
            data["channel_context"] = json.dumps(channel_context)
        if metadata:
            data["metadata"] = json.dumps(metadata)
        try:
            response = self.post(url, json=data)
            logger.debug(response)
            session_data = response['data']["session"]
            logger.info(f"Session created successfully. Session ID: {session_data['id']}")
            return Session(
                session_id=session_data["id"],
                created_at=int(session_data["created_at"]),
                metadata=session_data.get("metadata")
            )
        except Exception as e:
            logger.error(f"Error creating session: {str(e)}")
            raise

    def retrieve_session(self, session_id: str) -> Session:
        logger.info(f"Retrieving session with ID: {session_id}")
        url = f"{self.base_url}/sessions/{session_id}"
        try:
            response = self.get(url)
            session_data = response["session"]
            logger.info(f"Session retrieved successfully. Session ID: {session_data['id']}")
            return Session(
                session_id=session_data["id"],
                created_at=int(session_data["created_at"]),
                metadata=session_data.get("metadata"),
            )
        except Exception as e:
            logger.error(f"Error retrieving session: {str(e)}")
            raise

    @property
    def gen_idempotent_id(self):
        import random
        import string

        # 目标字符串
        target_string = "S9GiePojDRLuGFv-G8BZQ"
        # 计算目标字符串的长度
        length_of_target = len(target_string)

        # 生成一个相同长度的随机字符串
        # 包括大写字母、小写字母和数字
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length_of_target))

        return random_string

    def create_message(self, session_id: str, content: str, content_type: str = 'MDX', idempotent_id: str = None,
                       file_ids: Optional[List[str]] = None, mentions: Optional[List[dict]] = None,
                       quote_message_id: Optional[str] = None) -> Message:
        logger.info(f"Creating a new message in session: {session_id}")
        url = f"{self.base_url}/sessions/{session_id}/messages"
        data = {
            "content_type": content_type,
            "content": content
        }
        if not idempotent_id:
            data['idempotent_id'] = self.gen_idempotent_id
        if file_ids:
            data["file_ids"] = file_ids
        if mentions:
            data["mentions"] = mentions
        if quote_message_id:
            data["quote_message_id"] = quote_message_id
        try:
            response = self.post(url, json=data)
            message_data = response['data']["message"]
            logger.info(f"Message created successfully. Message ID: {message_data['id']}")
            return Message(
                message_id=message_data["id"],
                session_id=message_data["session_id"],
                content_type=message_data["content_type"],
                content=message_data["content"],
                sender=Sender(
                    aily_id=message_data["sender"].get('aily_id'),
                    sender_type=message_data["sender"].get('sender_type'),
                    identity_provider=message_data["sender"].get('identity_provider'),
                    entity_id=message_data["sender"].get('entity_id'),
                ),
                created_at=int(message_data["created_at"]),
                run_id=message_data.get("run_id"),
                file_ids=message_data.get("file_ids"),
                quote_message_id=message_data.get("quote_message_id"),
                mentions=message_data.get("mentions"),
                plain_text=message_data.get("plain_text")
            )
        except Exception as e:
            logger.error(f"Error creating message: {str(e)}")
            raise

    def list_messages(self, session_id: str, page_size: int = 20, page_token: Optional[str] = None,
                      run_id: Optional[str] = None) -> List[Message]:
        logger.info(f"Listing messages in session: {session_id}")
        url = f"{self.base_url}/sessions/{session_id}/messages"
        query = {"page_size": page_size}
        if page_token:
            query["page_token"] = page_token
        if run_id:
            query["filter"] = {"run_id": run_id}
        try:
            response = self.get(url, query=query)
            messages = []
            for message_data in response['data']["messages"]:
                message = Message(
                    message_id=message_data["id"],
                    session_id=message_data["session_id"],
                    content_type=message_data["content_type"],
                    content=message_data["content"],
                    sender=Sender(
                        aily_id=message_data["sender"].get('aily_id'),
                        sender_type=message_data["sender"].get('sender_type'),
                        identity_provider=message_data["sender"].get('identity_provider'),
                        entity_id=message_data["sender"].get('entity_id'),
                    ),
                    created_at=int(message_data["created_at"]),
                    run_id=message_data.get("run_id"),
                    file_ids=message_data.get("file_ids"),
                    quote_message_id=message_data.get("quote_message_id"),
                    mentions=message_data.get("mentions"),
                    plain_text=message_data.get("plain_text")
                )
                messages.append(message)
            logger.info(f"Listed {len(messages)} messages in session: {session_id}")
            return messages
        except Exception as e:
            logger.error(f"Error listing messages: {str(e)}")
            raise

    def create_run(self, session_id: str, app_id: str, skill_id: Optional[str] = None,
                   skill_input: Optional[dict] = None, metadata: Optional[str] = None) -> Run:
        logger.info(f"Creating a new run in session: {session_id}")
        url = f"{self.base_url}/sessions/{session_id}/runs"
        data = {"app_id": app_id}
        if skill_id:
            data["skill_id"] = skill_id
        if skill_input:
            data["skill_input"] = json.dumps(skill_input)
        if metadata:
            data["metadata"] = metadata
        try:
            response = self.post(url, json=data)
            run_data = response['data']["run"]
            logger.info(f"Run created successfully. Run ID: {run_data['id']}")
            return Run(
                run_id=run_data["id"],
                session_id=run_data["session_id"],
                app_id=run_data["app_id"],
                created_at=int(run_data["created_at"]),
                status=run_data["status"],
                start_at=datetime.fromtimestamp(int(run_data["start_at"]) / 1000) if run_data.get("start_at") else None,
                end_at=datetime.fromtimestamp(int(run_data["end_at"]) / 1000) if run_data.get("end_at") else None,
                error=run_data.get("error"),
                metadata=run_data.get("metadata")
            )
        except Exception as e:
            logger.error(f"Error creating run: {str(e)}")
            raise

    def retrieve_run(self, session_id: str, run_id: str) -> Run:
        logger.info(f"Retrieving run with ID: {run_id} in session: {session_id}")
        url = f"{self.base_url}/sessions/{session_id}/runs/{run_id}"
        try:
            response = self.get(url)
            run_data = response['data']["run"]
            logger.info(f"Run retrieved successfully. Run ID: {run_data['id']}")
            return Run(
                run_id=run_data["id"],
                session_id=run_data["session_id"],
                app_id=run_data["app_id"],
                created_at=int(run_data["created_at"]),
                status=run_data["status"],
                start_at=datetime.fromtimestamp(int(run_data["start_at"]) / 1000) if run_data.get("start_at") else None,
                end_at=datetime.fromtimestamp(int(run_data["end_at"]) / 1000) if run_data.get("end_at") else None,
                error=run_data.get("error"),
                metadata=run_data.get("metadata")
            )
        except Exception as e:
            logger.error(f"Error retrieving run: {str(e)}")
            raise

    def list_runs(self, session_id: str, page_size: int = 20, page_token: Optional[str] = None) -> List[Run]:
        logger.info(f"Listing runs in session: {session_id}")
        url = f"{self.base_url}/sessions/{session_id}/runs"
        query = {"page_size": page_size}
        if page_token:
            query["page_token"] = page_token
        try:
            response = self.get(url, query=query)
            runs = []
            for run_data in response["runs"]:
                run = Run(
                    run_id=run_data["id"],
                    session_id=run_data["session_id"],
                    app_id=run_data["app_id"],
                    created_at=int(run_data["created_at"]),
                    status=run_data["status"],
                    start_at=datetime.fromtimestamp(int(run_data["start_at"]) / 1000) if run_data.get(
                        "start_at") else None,
                    end_at=datetime.fromtimestamp(int(run_data["end_at"]) / 1000) if run_data.get("end_at") else None,
                    error=run_data.get("error"),
                    metadata=run_data.get("metadata")
                )
                runs.append(run)
                logger.info(f"Listed {len(runs)} runs in session: {session_id}")
            return runs
        except Exception as e:
            logger.error(f"Error listing runs: {str(e)}")
            raise

    def cancel_run(self, session_id: str, run_id: str) -> Run:
        logger.info(f"Cancelling run with ID: {run_id} in session: {session_id}")
        url = f"{self.base_url}/sessions/{session_id}/runs/{run_id}/cancel"
        try:
            response = self.post(url)
            run_data = response["run"]
            logger.info(f"Run cancelled successfully. Run ID: {run_data['id']}")
            return Run(
                run_id=run_data["id"],
                session_id=run_data["session_id"],
                app_id=run_data["app_id"],
                created_at=int(run_data["created_at"]),
                status=run_data["status"],
                start_at=datetime.fromtimestamp(int(run_data["start_at"]) / 1000) if run_data.get("start_at") else None,
                end_at=datetime.fromtimestamp(int(run_data["end_at"]) / 1000) if run_data.get("end_at") else None,
                error=run_data.get("error"),
                metadata=run_data.get("metadata")
            )
        except Exception as e:
            logger.error(f"Error cancelling run: {str(e)}")
            raise

    def list_run_steps(self, session_id: str, run_id: str, page_size: int = 20, page_token: Optional[str] = None) -> \
            List[RunStep]:
        logger.info(f"Listing run steps for run with ID: {run_id} in session: {session_id}")
        url = f"{self.base_url}/sessions/{session_id}/runs/{run_id}/steps"
        query = {"page_size": page_size}
        if page_token:
            query["page_token"] = page_token
        try:
            response = self.get(url, query=query)
            run_steps = []
            for step_data in response["steps"]:
                run_step = RunStep(
                    step_id=step_data["id"],
                    run_id=step_data["run_id"],
                    step_type=step_data["type"],
                    status=step_data["status"],
                    created_at=int(step_data["created_at"]) if step_data.get(
                        "created_at") else None,
                    completed_at=int(step_data["completed_at"]) if step_data.get(
                        "completed_at") else None,
                    expired_at=int(step_data["expired_at"]) if step_data.get(
                        "expired_at") else None,
                    failed_at=int(step_data["failed_at"]) if step_data.get(
                        "failed_at") else None,
                    last_error=step_data.get("last_error"),
                    step_details=step_data.get("step_details"),
                    usage=step_data.get("usage")
                )
                run_steps.append(run_step)
            logger.info(f"Listed {len(run_steps)} run steps for run with ID: {run_id}")
            return run_steps
        except Exception as e:
            logger.error(f"Error listing run steps: {str(e)}")
            raise

    def upload_file(self, files) -> dict:
        url = f"{self.base_url}/files"
        files_m = {}
        for idx, file in enumerate(files):
            files_m[f'file_{idx}'] = file

        try:
            response = self.post(url, files=files_m)
            logger.info(f"File uploaded successfully. Data: {response['data']}")
            return response["data"]
        except Exception as e:
            logger.error(f"Error uploading file: {str(e)}")
            raise

    def retrieve_file(self, file_id: str) -> dict:
        logger.info(f"Retrieving file with ID: {file_id}")
        url = f"{self.base_url}/files/{file_id}"
        try:
            response = self.get(url)
            logger.info(f"File retrieved successfully. File ID: {response['file']['id']}")
            return response["file"]
        except Exception as e:
            logger.error(f"Error retrieving file: {str(e)}")
            raise
