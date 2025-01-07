import threading
import time
import serial

lock = threading.Lock()


data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
set_zero_data = [0xA5, 0x01, 0x00, 0x02, 0x5A]
# 代表左右臂的指令
hex_array_l = bytearray([0xA5, 0x01, 0x00, 0x06, 0x5A])  # 左臂
hex_array_r = bytearray([0xA5, 0x01, 0x00, 0x07, 0x5A])  # 右臂


class exoskeleton:

    def __init__(self, port):
        self.ser = serial.Serial(port=port, baudrate=1000000)

    # 0：左臂
    # 1: 右臂
    def get_data(self, arm):
        with lock:
            if arm == 0:
                self.ser.write(hex_array_l)
            elif arm == 1:
                self.ser.write(hex_array_r)
            else:
                raise ValueError("error arm")
            time.sleep(0.01)
            count = self.ser.in_waiting
            data = self.ser.read(count).hex()
            print(data)
            if len(data) == 84 and data[0:2] == "d5" and data[-2:] == "5d":
                for i in range(7):
                    data_h = data[8 + i * 10: 10 + i * 10]
                    data_l = data[10 + i * 10: 12 + i * 10]
                    encode = int(data_h + data_l, 16)
                    if encode == 2048:
                        angle = 0
                    elif encode < 2048:
                        angle = -180 * (2048 - encode) / 2048
                    else:
                        angle = 180 * (encode - 2048) / 2048
                    data_list[i] = round(angle, 2)
                button = bin(int(data[-10: -8]))[2:].rjust(4, "0")
                data_list[7] = int(button[1])
                data_list[8] = int(button[2])
                data_list[9] = int(data[-6: -4], 16)
                data_list[10] = int(data[-4: -2], 16)
                return data_list
            else:
                return None

    # 0：左臂
    # 1: 右臂
    def set_zero(self, arm, arm_id):
        with lock:
            if arm == 0:
                set_zero_data[3] = 0x12
            elif arm == 1:
                set_zero_data[3] = 0x02
            else:
                raise ValueError("error arm")
            if 1 <= arm_id <= 7:
                set_zero_data[1] = arm_id
            else:
                raise ValueError("error id")
            self.ser.write(bytearray(set_zero_data))