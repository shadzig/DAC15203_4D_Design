import time



while True:
        
	uin = 36000
	try:
		when_to_stop = abs(int(uin))
	except KeyboardInterrupt:
		break
	except:
		print("Not a number!")

	while when_to_stop >= 0:
		m, s = divmod(when_to_stop, 60)
		h, m = divmod(m, 60)
		time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
		
		neutral_score = (when_to_stop)/360/4
		sad_score = (when_to_stop)/360/6.666
		angry_score = (when_to_stop)/360/1.666
		score = (when_to_stop)/360
		
		score_minus_neutral = 75 + (neutral_score)
		neutral_minus_sad = 60 + (sad_score)
		sad_minus_angry = (angry_score)

		#print(time_left + "  | score " + str(score) + "\r", end="")
		#print(time_left + "  | score " + str(score_minus_neutral) + "\r", end="")
		print(time_left + "  | score " + str(score_minus_neutral) + "  | score " + str(neutral_minus_sad) + "  | score " + str(sad_minus_angry) + "\r", end="")
		#print(time_left + "  | neutral_score " + str(neutral_score) +  "  | Sad_score " + str(sad_score) + "  | angry_score " + str(angry_score) + "\r", end="")
		when_to_stop -= 1

                

	print()

