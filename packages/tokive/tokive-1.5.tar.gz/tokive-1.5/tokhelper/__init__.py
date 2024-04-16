from tokhelper.tiktok_main import solve_captcha_auto, solve_ping_poll_captcha_auto, create_key_live, finish_live


class TokHelper():
    def __init__(self):
        print("init")
    def solve_auto_helper(self,id, room, stream_id):
        solve_ping_poll_captcha_auto(id, room, stream_id)
    def live_create(self, id):
        finish_live(id)
        x = create_key_live(id)
        print(x)