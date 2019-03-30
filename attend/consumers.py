from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    # websocket이 연결 되었을 때 행해질 메서드
    def connect(self):
        self.accept()
	# 연결이 끊길 경우 행해질 메서드
    def disconnect(self, close_code):
        pass
	# 클라이언트로부터 메세지를 받으면 행해질 메서드
    # 아래에서는 메세지를 받으면 다시 클라이언트로 보내는 코드를 작성한 예시이다.
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
		# 이 부분이 클라이언트로 다시 메세지를 보내는 부분이다.
        self.send(text_data=json.dumps({
            'message': message
        }))