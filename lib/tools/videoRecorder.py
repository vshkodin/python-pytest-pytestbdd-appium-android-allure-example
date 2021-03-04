import allure
import base64
import os


class VideoRecorder:

    def __init__(self, driver,video_record):
        self.driver = driver
        self.video_record=video_record
        if self.video_record == "True":
            self.driver.start_recording_screen()
        else:
            pass

    def stop_recording(self, name_of_test):

        if self.video_record == "True":
            video_data = self.driver.stop_recording_screen()
            pathforscripttwo = os.path.realpath(__file__)
            pathforscripttwo = pathforscripttwo.replace('lib/tools/videoRecorder.py', '')
            failePath = os.path.join(pathforscripttwo, name_of_test+'.mp4')  # TODO refactor to config
            with open(failePath, 'wb') as vd:
                vd.write(base64.b64decode(video_data))
            allure.attach.file(str(name_of_test)+'.mp4', attachment_type=allure.attachment_type.MP4, name="VIDEO_"+str(name_of_test))
            os.system('rm -f ' + str(name_of_test)+'.mp4')
        else:
            pass
