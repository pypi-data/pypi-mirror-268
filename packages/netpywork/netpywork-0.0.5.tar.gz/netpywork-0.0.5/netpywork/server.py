import socket
import select
from threading import Thread
from .protocol import *
from .sequence_manager import sequence_manager
from .utils import *
from .utils import _utils
from .constants import *

class server:
    def __init__(self,port : int) -> None:
        self.port : int = port
        self.auto_receive_udp: bool = True
        self.auto_receive_tcp: bool = True
        self.on_receive = None
        self.on_connect = None
        self.on_disconnect = None

        self.__tcp_socket: socket.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__tcp_socket.bind(('',port))

        self.__udp_socket: socket.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.__udp_socket.bind(('',port))

        self.__tcp_thread: Thread = None
        self.__udp_thread: Thread = None

        self.__udp_messages: list = []
        self.__tcp_messages: list = []
        self.__clients: list = []
        self.__seq_manager: sequence_manager = sequence_manager()
        self.__addr_to_sock: dict = {}
        self.__udp_seq = 0
        self.__is_running = False
    def get_clients(self):
        return [x.getpeername() for x in self.__clients]
    def run(self):
        self.__is_running = True
        self.__tcp_thread = Thread(target=self.__run_tcp)
        self.__tcp_socket.listen()
        self.__tcp_thread.start()

        self.__udp_thread = Thread(target=self.__run_udp)
        self.__udp_socket.settimeout(UDP_TIMEOUT)
        self.__udp_thread.start()
    def close(self):
        self.__is_running = False
        self.__tcp_socket.close()
        self.__tcp_thread.join()
        for client in self.__clients:
            self.__seq_manager.delete_addr(client.getpeername())
        self.__udp_thread.join()
        self.__udp_socket.shutdown(socket.SHUT_RDWR)
        self.__udp_socket.close()
        self.__seq_manager.stop()
    def has_tcp_messages(self) -> bool:
        return len(self.__tcp_messages) > 0
    def read_tcp_message(self) -> tcp_msg:
        while len(self.__tcp_messages) < 1:
            continue
        return self.__tcp_messages.pop(0)
    def has_udp_messages(self) -> bool:
        return len(self.__udp_messages) > 0
    def read_udp_message(self) -> udp_msg:
        while len(self.__udp_messages) < 1:
            continue
        return self.__udp_messages.pop(0)
    def send_all(self,msg:bytes,proto:protocol = protocol.TCP,exceptions: list = []):
        for client in self.get_clients():
            if(client in exceptions):
                continue
            self.send(msg,client,proto)
    def send(self,msg:bytes,address:tuple,proto:protocol = protocol.TCP):
        if(proto == protocol.TCP):
            self.send_reliable(msg,address)
        elif(proto == protocol.UDP):
            self.send_unreliable(msg,address)
        else:
            raise ValueError(f"Protocol type is unknown")
    def send_reliable(self,msg: bytes,address:tuple):
        _utils.send_tcp(self.__addr_to_sock[address],msg)
    def __get_actual_address(self,address):
        return self.__addr_to_sock[address].getpeername()
    def send_unreliable(self,msg: bytes,address:tuple):
        msg_len = len(msg)
        if(msg_len <= MAX_UDP_PACKET_SIZE):
            _utils.send_udp(self.__udp_socket,self.__tcp_socket.getsockname()[1],self.__get_actual_address(address),msg,self.__udp_seq,0,1)
        else:
            parts = []
            while (len(msg) > MAX_UDP_PACKET_SIZE):
                parts.append(msg[0:MAX_UDP_PACKET_SIZE])
                msg = msg[MAX_UDP_PACKET_SIZE:]
            parts.append(msg)
            for i in range(len(parts)):
                _utils.send_udp(self.__udp_socket,self.__tcp_socket.getsockname()[1],self.__get_actual_address(address),parts[i],self.__udp_seq,i,len(parts))
        self.__udp_seq += 1
    def __has_client(self,address):
        for client in self.__clients:
            client_address = client.getpeername()
            if(address == client_address):
                return True
        return False
    
    def __delete_client(self,sock):
        self.__clients.remove(sock)
        socket_addr = sock.getpeername()
        self.__seq_manager.delete_addr(socket_addr)
        del self.__addr_to_sock[socket_addr]
        if(self.on_disconnect):
            self.on_disconnect(socket_addr,self)
    def __run_udp(self):
        while self.__is_running:
            try:
                message: udp_msg = _utils.read_udp_msg(self.__udp_socket)
                if(not self.__has_client(message.address)):
                    continue
                self.__seq_manager.add_seq(message.address,message.seq_no,message.data,message.seq_id)
                if(message.amount == self.__seq_manager.get_amount(message.address,message.seq_no)):
                    # TODO : move to logging
                    # print("UDP",)
                    data = self.__seq_manager.get_result(message.address,message.seq_no)
                    result_msg = udp_msg()
                    result_msg.data = data
                    result_msg.address = message.address
                    result_msg.length = len(data)
                    result_msg.port = message.port
                    result_msg.amount = message.amount
                    result_msg.seq_no = message.seq_no
                    self.__udp_messages.append(result_msg)
            except:
                continue
            finally:
                while(self.on_receive and self.auto_receive_udp and self.has_udp_messages()):
                    self.on_receive(self.__udp_messages.pop(0),protocol.UDP,self)
    def __run_tcp(self):
        while self.__is_running:
            try:
                sockets,_,_ = select.select(self.__clients + [self.__tcp_socket],[],[])
                for sock in sockets:
                    if(sock == self.__tcp_socket):
                        client_socket,_ = sock.accept()
                        self.__clients.append(client_socket)
                        client_addr = client_socket.getpeername()
                        self.__seq_manager.add_addr(client_addr)
                        self.__addr_to_sock[client_addr] = client_socket
                        if(self.on_connect):
                            self.on_connect(client_addr,self)
                    else:
                        try:
                            message: tcp_msg = _utils.read_tcp_msg(sock)
                            # Remove the length of the is end byte to match udp length which is the data length
                            message.length -= 1
                            self.__tcp_messages.append(message)
                            # TODO : move to logging
                            #print("TCP",message.data)
                            if(message.closing):
                                self.__delete_client(sock)
                        except:
                            self.__delete_client(sock)
                        finally:
                            while(self.on_receive and self.auto_receive_tcp and self.has_tcp_messages()):
                                self.on_receive(self.__tcp_messages.pop(0),protocol.TCP,self)
            except:
                continue