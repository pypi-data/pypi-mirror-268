import time
import unittest

from rocs_client import Human
from rocs_client.robot.human import ArmAction, HandAction


async def on_connected():
    print("WebSocket opened...")


async def on_message(message: str):
    print("Received message:", message)


async def on_close():
    print("WebSocket closed")


async def on_error(error: Exception):
    print("WebSocket error:", error)


human = Human(on_connected=on_connected, host="127.0.0.1", on_message=on_message, on_close=on_close, on_error=on_error)

res_svr_status = human._control_svr_status()

if res_svr_status['data']:
    print('--------------------- server status is running')
else:
    for chunk in human._control_svr_start():
        if 'init!' in chunk and 'start json init' not in chunk:
            print('### -------------- server starting success')
            break


class TestHuman(unittest.TestCase):

    def test_enable_debug_state(self):
        res = human.enable_debug_state(1)
        print(f'test_enable_debug_state: {res}')
        # time.sleep(2)
        # human.exit()

    def test_disable_debug_state(self):
        res = human.disable_debug_state()
        print(f'test_disable_debug_state: {res}')
        human.exit()

    def test_get_video_status(self):
        res: bool = human.camera.video_stream_status
        print(f'test_get_video_status: {res}')
        human.exit()

    def test_get_video_stream_url(self):
        res: str = human.camera.video_stream_url
        print(f'test_get_video_stream_url:  {res}')
        human.exit()

    def test_get_joint_limit(self):
        res = human.get_joint_limit()
        print(f'test_get_joint_limit: {res}')
        human.exit()

    def test_get_joint_states(self):
        res = human.get_joint_states()
        print(f'human.test_get_joint_states: {res}')
        human.exit()

    def test_start(self):
        res = human.start()
        print(f'human.test_start: {res}')
        human.exit()

    def test_stop(self):
        res = human.stop()
        print(f'human.test_stop: {res}')
        human.exit()

    def test_stand(self):
        res = human.stand()
        print(f'human.test_stand: {res}')
        human.exit()

    def test_move(self):
        human.walk(0, 0)
        time.sleep(5)
        human.exit()

    def test_head(self):
        human.head(1, 1, 0.8)
        human.exit()

    def test_upper_body_arm(self):
        human.upper_body(arm=ArmAction.HELLO)
        human.exit()

    def test_upper_body_arm_waving_left_right(self):
        human.upper_body(arm=ArmAction.WAVING_LEFT_RIGHT)
        human.exit()

    def test_upper_body_arm_nvidia_dance(self):
        human.upper_body(arm=ArmAction.NVIDIA_DANCE)
        human.exit()

    def test_upper_body_hand(self):
        human.upper_body(hand=HandAction.TREMBLE)
        human.exit()

    def test_start_control_svr(self):
        for chunk in human._control_svr_start():
            print(chunk.decode('utf-8'))

    def test_log_view_control_svr(self):
        for chunk in human._control_svr_log_view():
            print(chunk.decode('utf-8'))

    def test_close_control_svr(self):
        print('test_close_control_svr: ', human._control_svr_close())
        human.exit()

    def test_status_control_svr(self):
        print('test_status_control_svr: ', human._control_svr_status())
        human.exit()
