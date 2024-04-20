from pydub import AudioSegment
import numpy as np
from plot import Plot

from pydub import AudioSegment

# Set the path to FFmpeg
AudioSegment.converter = "./ffmpeg/bin/ffmpeg.exe"


zf = lambda x,y: str(x).zfill( len( str(y) ) )

class binbeats:

    main_buffer = [] 
    diffrence=[]
    timeline=[]
    
    @staticmethod
    def reset():
        binbeats.main_buffer = [] 
        binbeats.diffrence = []
        binbeats.timeline = []

    @staticmethod
    def save(filename, format):

        combined_audio = sum(binbeats.main_buffer)
        print(f"Saving to {filename}")
        combined_audio.export(filename+"."+format, format=format)
    
    def create(left_hz, right_hz, duration, sample_rate=44100, left_level=1.0, right_level=1.0):
        time = np.arange(0, duration, 1/sample_rate)
        left_channel = np.sin(2 * np.pi * left_hz * time) * left_level
        right_channel = np.sin(2 * np.pi * right_hz * time) * right_level
        
        stereo_audio = np.column_stack((left_channel, right_channel))
        
        max_amplitude = np.max(np.abs(stereo_audio))
        stereo_audio /= max_amplitude if max_amplitude != 0 else 1

        stereo_audio = (stereo_audio * 32767).astype(np.int16)
        gen_beats = AudioSegment(stereo_audio.tobytes(), frame_rate=sample_rate, sample_width=2, channels=2)

        return gen_beats
    
    def steady(base_f, diffrence, mins, sample_rate=44100, left_level=1.0, right_level=1.0):

        seconds = mins * 60

        left = base_f
        right = base_f + diffrence

        print("Base Frequency:", base_f)
        print("Difference:", diffrence)
        print("Left:", left)
        print("Right:", right)
        print("Duration in seconds:", seconds)
        
        

        if len(binbeats.timeline) == 0:
            binbeats.timeline.append(0)
            binbeats.timeline.append(seconds)
            binbeats.diffrence.append(diffrence)
            binbeats.diffrence.append(diffrence)
        else:
            binbeats.diffrence.append(diffrence)
            binbeats.timeline.append(binbeats.timeline[-1] + seconds)
     
        buffer = binbeats.create(left, right, seconds, sample_rate, left_level, right_level)
        binbeats.main_buffer.append(buffer)
        
    def down(base_f, int_diff, fin_diff , mins, 
                d_l=None, d_r=None, d_e=None,
                sample_rate=44100 , left_level=1.0, right_level=1.0):
    
        secs = mins * 60
        base_f = float(base_f)
        left = base_f
        right = base_f + int_diff

        points = ( int_diff - fin_diff + 0.1 )  * 10

        fin_diff = (int_diff - fin_diff ) + 0.1
        
        update_per_sec = secs / points

        print("Base Frequency:", base_f)
        print("Initial Difference:", int_diff)
        print("Final Difference:", fin_diff)
        print("Duration in seconds:", secs)
        print("Left:", left)
        print("Right:", right)
        print("Points:", points)
        print("Update per second:", update_per_sec)

        # Increment timeline if it's not empty
        if binbeats.timeline:
            offset = binbeats.timeline[-1]  # Get the last value in the timeline
        else:
            offset = 0

        # Decerse
        for i in range(0,int(points)):

            curr_diff = round(right - left, 3)
            binbeats.diffrence.append(curr_diff)

            x = update_per_sec * i + offset
            binbeats.timeline.append(round(x,2))

            print(f"| {zf(i+1,points)} | left: {left} | right: {right} | difference: {curr_diff:.1f} | timeline: {x:.1f}" )
            
            if d_r:
                
                buffer= binbeats.create(left, right, update_per_sec, sample_rate, left_level, right_level)
                binbeats.main_buffer.append(buffer)
                
                right = round( right - 0.1 , 1)


            elif d_l:
                buffer= binbeats.create(left, right, update_per_sec, sample_rate, left_level, right_level)
                binbeats.main_buffer.append(buffer)
                left = round( left + 0.1 , 1)


            elif d_e:
                buffer= binbeats.create(left, right, update_per_sec, sample_rate, left_level, right_level)
                binbeats.main_buffer.append(buffer)
                left = round(left + 0.05,1)
                right = round(right - 0.05,1)

        
        return left , round(right,1) , curr_diff 
    
    def up(base_f, int_diff, fin_diff, mins, 
        u_l=None, u_r=None, u_e=None,
        sample_rate=44100, left_level=1.0, right_level=1.0):

        if fin_diff < int_diff:
            print( f" Final diffrence {fin_diff}Hz Is smaller initial difference {int_diff}" )
            print( f" Final diffrence shouldbe greater to move upwards in Hz " )
            return

        secs = mins * 60
        base_f = float(base_f)
        
        left = base_f
        right = base_f + int_diff
        
        fin_diff = round(fin_diff - int_diff + 0.1 , 2 )
        points = round( (fin_diff + 0.1) * 10 , 2)
        update_per_sec = secs / points

        print("Base Frequency:", base_f)
        print("Initial Difference:", int_diff)
        print("Final Difference:", fin_diff)
        print("Duration in seconds:", secs)
        print("Left:", left)
        print("Right:", right)
        print("Points:", points)
        print("Update per second:", update_per_sec)
        print("--------------------------\n\n")
        

        # Increment timeline if it's not empty
        if binbeats.timeline:
            offset = binbeats.timeline[-1]  # Get the last value in the timeline
        else:
            offset = 0

        # Increase
        for i in range(0, int(points)):
        
            curr_diff = round(right - left, 3)
            binbeats.diffrence.append(curr_diff)

            x = round(update_per_sec * i + offset, 2)
            binbeats.timeline.append(x)

            print(f"| {zf(i, points)} | left: {left:.1f} | right: {right:.1f} | difference: {curr_diff:.1f} | seconds: {x:.2f}")

            if u_r:
                buffer = binbeats.create(left, right, update_per_sec, sample_rate, left_level, right_level)
                binbeats.main_buffer.append(buffer)
                right += 0.1
            elif u_l:
                buffer = binbeats.create(left, right, update_per_sec, sample_rate, left_level, right_level)
                binbeats.main_buffer.append(buffer)
                left -= 0.1
            elif u_e:
                buffer = binbeats.create(left, right, update_per_sec, sample_rate, left_level, right_level)
                binbeats.main_buffer.append(buffer)
                left -= 0.05
                right += 0.05

    def power_nap( base_f, start_diff, goto_d ,start_duration ,
                    stay_duration
                   ):

        left , right , last_diff =binbeats.down( base_f , start_diff , goto_d , mins=start_duration , d_r=True )

        print( left , right , last_diff )    

        binbeats.steady( base_f=left , diffrence=last_diff , mins=stay_duration )

        exit=binbeats.up( base_f=left , int_diff=last_diff , fin_diff=start_diff , mins=start_duration , u_e=True )

    def down_xx(base_f, int_diff, fin_diff, mins,
                d_l=None, d_r=None, d_e=None,
                sample_rate=44100, left_level=1.0, right_level=1.0):

        base_f = float(base_f)

        total_duration = mins * 60

        distance = int_diff - fin_diff

        points = distance * 10

        update_per_sec = round(total_duration / points , 2 )

        left = base_f
        right = base_f + int_diff

        print("Base Frequency:", base_f)
        print("Initial Difference:", int_diff)
        print("Final Difference:", fin_diff)
        print("Duration in seconds:", total_duration)
        print("Distance:", distance)
        print("Points:", points)

        print( "Update per sec: " , update_per_sec )

        print("Left:", left)
        print("Right:", right)

        num=0
        while num <= total_duration:
            
            print(f"| {zf(num, total_duration)} | left: {left:.1f} | right: {right:.1f} | difference: {right - left:.1f} | seconds: {num:.2f}")

            if d_r:
            
                binbeats.main_buffer.append( binbeats.create( left , right , update_per_sec , 
                                                             sample_rate , left_level , 
                                                             right_level ) )
                
                right = round(right - 0.1, 1)


            num = round( num + update_per_sec , 1 )