# import speedtest module
import speedtest
def speedtest1():
    speed_test = speedtest.Speedtest()
    upload_speed = speed_test.upload()
    print("Your Upload speed is", upload_speed/1024**2)
    speed = upload_speed/1024**2
    return speed
