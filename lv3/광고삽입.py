def solution(play_time, adv_time, logs):
    play = list(map(int, play_time.split(':')))
    play_time = (play[0] * 60 + play[1]) * 60 + play[2] # play 시간을 초로 변경
    adv = list(map(int, adv_time.split(':')))
    adv_time = (adv[0] * 60 + adv[1]) * 60 + adv[2] # adv 시간을 초로 변경
    logs_time = []
    for i in range(len(logs)):
        temp = logs[i].split('-')
        # 시작 시간과 끝 시간을 각각 파싱해서 초로 변환해서 튜플 형태로 저장
        t = (list(map(int, temp[0].split(':'))), list(map(int, temp[1].split(':'))))
        logs_time.append(((t[0][0] * 60 + t[0][1]) * 60 + t[0][2], (t[1][0] * 60 + t[1][1]) * 60 + t[1][2]))
    
    # 시청 시간의 누적합 구하기
    total_time = [0 for _ in range(play_time + 1)]
    for log in logs_time:
        total_time[log[0]] += 1
        total_time[log[1]] -= 1

    for i in range(1, play_time): # 초당 시청자 수
        total_time[i] = total_time[i - 1] + total_time[i]
    
    for i in range(1, play_time): # 초단위 누적 사용자 수
        total_time[i] = total_time[i - 1] + total_time[i]

    max_view = total_time[adv_time - 1]
    time_max_view = 0
    for i in range(adv_time, play_time):
        if max_view < total_time[i] - total_time[i - adv_time]: # i ~ i - adv 초 
            max_view = total_time[i] - total_time[i - adv_time]
            time_max_view = i + 1 - adv_time

    return num_to_time(time_max_view)

def num_to_time(num):
    s = '0' + str(num % 60)
    m = '0' + str((num // 60) % 60)
    h = '0' + str((num // 60) // 60)
    return h[-2:] + ':' + m[-2:] + ':' + s[-2:]

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59",	"25:00:00",	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00",	"50:00:00",	["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))