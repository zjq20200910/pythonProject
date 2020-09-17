ask_distance_str = input("What is the current distance (in km)?")
transport_speed_str= input("What is the speed of the transport that you chose?(in km/h)")

time_start_str= input("What is the start time for you?(in hours 0-23)")
time_parking_str=input("what is the time to park?(in hours)")


final_answer=int(time_start_str)+int(ask_distance_str)/int(transport_speed_str)+int(time_parking_str)
final_answer = int(final_answer) % 24


print(final_answer)