from rpc import Presence
client_id = 'Client ID'
import rumps
try:
    RPC = Presence(client_id)
    RPC.connect()
    RPC.update(details="A software developer", large_image='pfp-rounded',
               large_text="Johan Naizu", button1="johan.naizu", url1='https://johan.naizu.in/', button2="Discord",
               url2="https://discord.com/invite/SqS3kEGu5E") #Set the presence, picking a random quote
except:
    rumps.alert("Discord is not open")
    rumps.quit_application()



class Sypher(rumps.App):
    def __init__(self):
        super(Sypher, self).__init__("🔘")
        self.menu = ["Stop", "Start"]

    @rumps.clicked("Stop")
    def prefs(self, _):
        rumps.notification("Discord", "Stopped", "Rich presence has been stopped")
        RPC.close()
    @rumps.clicked("Start")
    def onoff(self,_):
        try:
            RPC.connect()
            RPC.update(details="A software developer", large_image='pfp-rounded',
                       large_text="Johan Naizu", button1="johan.naizu", url1='https://johan.naizu.in/',button2="Discord",url2="https://discord.com/invite/SqS3kEGu5E")
            rumps.notification("Discord", "STARTED", "Rich presence has started")
        except:
            rumps.alert("Discord is not open")
            rumps.quit_application()
if __name__ == "__main__":
    Sypher().run()
