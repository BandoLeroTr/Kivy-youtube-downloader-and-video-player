from Home_Page import Home_Page

class Video():
    xHome_Page = Home_Page()
    def selected(self, filename):
        global path
        for path in filename:
            print(path)

    def video_play(self, app):
        print("play")
        app.root.ids.video.source = path
        app.root.ids.video.state = "play"

    def video_pause(self, app):
        print("pause")
        app.root.ids.video.state = "pause"

    def video_stop(self, app):
        print("stop")
        app.root.ids.video.state = "stop"
