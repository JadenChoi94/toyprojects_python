# -*- coding: utf-8 -*-
from twisted.internet import protocol
from twisted.internet import reactor
import names
COLORS = ["\033[31m", #RED
          '\033[32m', #Green
          '\033[33m', #Yellow
          '\033[34m', #Blue
          '\033[35m', #Magenta
          '\033[36m', #Cyan
          '\033[37m', #White
          '\033[4m', #Underline
          ]
transports = set()
users = set()
class Chat(protocol.Protocol):
    def connectionMade(self):
        name = names.get_first_name()
        # color = COLORS[len(users) % len(COLORS)]
        users.add(name)
        transports.add(self.transport)
        self.transport.write(f'{name}\033[0m'.encode())       
        
    def dataReceived(self, data):
        for t in transports:
            if self.transport is not t:
                t.write(data)
        
class ChatFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Chat()

print('Server started!')
reactor.listenTCP(8000, ChatFactory())
reactor.run()

# python  명령프롭프트에 출력시 색깔넣기
# Escape 코드와 ANSI Text 색변경 숫자코드을 사용하여 프린터명령어 사용시 글자에 색상 및 배경을 바꿀수있다.
# '\033[' 이 기호는 Escape sequences 중에서 Control Sequence Introduce(CSI)를 나타내는 코드이고 Terminal 창에 특수한 역활을 하는 명령을 주는 시작코드임


# 윈도우10에서 작동이 되지않을때 해결방법
# 레지스트리 편집기에서
# HKEY_CURRENT_USER\Console 에서 DWORD를 생성하여 이름VirtualTerminalLevel 값을 1을 넣어준다.
