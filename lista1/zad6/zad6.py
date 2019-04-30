class television:
    
    def __init__(self,channel,volume = 50):
        self._channel = channel
        self._volume = volume
        print(f"Channel: {self._channel}\nVolume: {self._volume}\n")
    
    def ChangeChannel(self,channel):
        if channel > 0 and channel <= 10:
            self._channel = channel
            print(f"Channel changed to: {self._channel}")
        else:
            print(f"Channel {channel} doesn't exist!")
    
    def VolumeUp(self):
        if (self._volume + 5) <= 100:
            self._volume += 5
            print(f"Volume changed to {self._volume}")
        else:
            print(f"Volume too high!")
    
    def VolumeDown(self):
        if (self._volume - 5) >= 0:
            self._volume -= 5
            print(f"Volume changed to {self._volume}")
        else:
            print(f"Volume too low!")

        
TV = television(1)
TV.ChangeChannel(4)
TV.VolumeDown()
TV.VolumeDown()
TV.VolumeUp()
