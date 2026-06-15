import random

# Team stats
morale = 70
strength = 75
injuries = 0

print("⚽ FIFA World Cup 2026 Simulation ⚽")

# Pre-tournament preparation
for week in range(1, 4):
    print(f"\nPreparation Week {week}")

    print("1. Intensive Training")
    print("2. Friendly Match")
    print("3. Recovery Session")

    choice = input("Choose an activity (1-3): ")

    if choice == "1":
        strength += 5
        injuries += random.randint(0, 2)
        print("Training completed. Strength increased.")
    elif choice == "2":
        morale += 5
        print("Friendly match played. Morale increased.")
    elif choice == "3":
        injuries = max(0, injuries - 2)
        morale += 2
        print("Recovery session completed.")
    else:
        print("Invalid choice. Skipping week.")
        continue  # Skip to next week

# Future feature placeholder
pass

# Group Stage
print("\n=== GROUP STAGE ===")

for match in range(1, 4):
    print(f"\nGroup Match {match}")

    team_power = strength + morale - (injuries * 5)
    opponent = random.randint(60, 90)

    if team_power >= opponent:
        print("✅ Win!")
        morale += 5
    else:
        print("❌ Loss!")
        morale -= 10

    if morale <= 30:
        print("Team morale collapsed. Eliminated!")
        break

else:
    # Runs only if group stage completed without break
    print("\nQualified for Knockout Stage!")

    stages = ["Round of 16", "Quarter-final", "Semi-final", "Final"]

    for stage in stages:
        print(f"\n{stage}")

        team_power = strength + morale - (injuries * 5)
        opponent = random.randint(70, 95)

        if team_power >= opponent:
            print("✅ Victory!")
            morale += 5

            if stage == "Final":
                print("\n🏆 CONGRATULATIONS! YOU WON THE 2026 FIFA WORLD CUP! 🏆")
                break
        else:
            print("❌ Defeat!")
            print(f"Eliminated in the {stage}.")
            break

print("\nTournament Ended.")