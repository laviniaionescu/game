import json
import time
import basic_functions
import main_functions


mission_type = ["1. Rescue Operation", "2. Launch ICBM", "3. Exterminate Abomination"]
civilian_status = {"rescued": 0, "dead": 0}
generator_hp = 100
stats = {"reinforcements": 5, "current_hp": 100, "max_hp": 100, "current_ammo": 300}


player_score = 0


if __name__ == '__main__':
    # get player name from function
    player_name = basic_functions.get_player_name()
    time.sleep(1)
    print(f"Helldiver {player_name}, choose in what way you want to save the world today! ")
    for mission in mission_type:
        print(mission)
    mission_pick = int(input("Press 1, 2 or 3: "))
    # display mission options, stay in loop until player picks a valid mission option
    while mission_pick not in [1, 2, 3]:
        mission_pick = input("Press 1, 2 or 3: ")
    else:
        time.sleep(1)
        print("You dropped in on the battlefield!")
    # roll and run a random event
    run_event = basic_functions.event_roll()
    if run_event == "normal_bug_spawn":
        basic_functions.normal_bug_spawn(stats)

    elif run_event == "hive_spawn":
        basic_functions.hive_spawn(stats)

    elif run_event == "meteor_shower":
        basic_functions.meteor_shower(stats)

    elif run_event == "fire_tornadoes":
        basic_functions.fire_tornadoes(stats)
####################################################################################
    match mission_pick:
        case 1:
            rescue_civs = main_functions.rescue_operation(stats, civilian_status)
            # if too many civs die, mission fails, exit
            if rescue_civs == "mission failed":
                exit()
            else:
                # mission successful, update player score, run extraction, write player score
                player_score = basic_functions.update_player_score(player_score)
                player_score += 10
                main_functions.extraction(30, stats)
                player_stats = {"Name": player_name, "Score": player_score}
                with open("scores.jsonl", "a") as f:
                    f.write(json.dumps(player_stats, indent=4) + "\n")
                exit()

        case 2:
            # run the 3 stages of the mission then write the score
            main_functions.generator_boot(20, generator_hp, stats)
            main_functions.fuel_icbm(0, stats)
            main_functions.launch_icbm(20, stats)
            player_score = basic_functions.update_player_score(player_score)
            player_score += 20
            main_functions.extraction(30, stats)
            player_stats = {"Name": player_name, "Score": player_score}
            with open("scores.jsonl", "a") as f:
                f.write(json.dumps(player_stats, indent=4) + "\n")
            exit()

        case 3:
            boss_fight = main_functions.boss_fight(stats)
            if boss_fight == "mission successful":
                # if mission is successful, update the score, go to extraction, write the score
                player_score = basic_functions.update_player_score(player_score)
                player_score += 30
                main_functions.extraction(30, stats)
                player_stats = {"Name": player_name, "Score": player_score}
                with open("scores.jsonl", "a") as f:
                    f.write(json.dumps(player_stats, indent=4) + "\n")
                exit()
            else:
                # if mission failed, exit
                exit()



