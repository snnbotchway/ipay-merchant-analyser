import csv

total_success_count = 0
total_failure_count = 0

payment_for_vote_success_count = 0
sml_games_success_count = 0
voting_contest_success_count = 0

payment_for_vote_failure_count = 0
sml_games_failure_count = 0
voting_contest_failure_count = 0

payment_for_vote_failures = {}
sml_games_failures = {}
voting_contest_failures = {}
other_description_failures = {}


with open("./successful.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        description = row[16].lower()
        total_success_count += 1

        if "payment" in description and "for" in description and "vote" in description:
            payment_for_vote_success_count += 1
        elif "smlgames" in description:
            sml_games_success_count += 1
        elif "voting" in description and "contest" in description:
            voting_contest_success_count += 1


with open("./failed.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        description = row[16].lower()
        status_reason = row[3]
        total_failure_count += 1

        if "payment" in description and "for" in description and "vote" in description:
            payment_for_vote_failures.setdefault(status_reason, 0)
            payment_for_vote_failures[status_reason] += 1
            payment_for_vote_failure_count += 1
        elif "smlgames" in description:
            sml_games_failures.setdefault(status_reason, 0)
            sml_games_failures[status_reason] += 1
            sml_games_failure_count += 1
        elif "voting" in description and "contest" in description:
            voting_contest_failures.setdefault(status_reason, 0)
            voting_contest_failures[status_reason] += 1
            voting_contest_failure_count += 1
        else:
            other_description_failures.setdefault(status_reason, 0)
            other_description_failures[status_reason] += 1


class bcolors:
    green = '\033[92m'
    red = '\033[91m'
    end = '\033[0m'


print(f"\nTOTAL SUCCESS: {bcolors.green}{total_success_count}{bcolors.end}")
print(f"TOTAL FAILURES: {bcolors.green}{total_failure_count}{bcolors.end}")

print(f"{bcolors.green}\n\nOTHER DESCRIPTIONS{bcolors.end}")
for key, value in other_description_failures.items():
    print(f"{key}: {bcolors.green}{value}{bcolors.end}")

print(f"{bcolors.green}\n\nPAYMENT FOR VOTE(SmartKast_gen){bcolors.end}")
print(f"We recorded {bcolors.green}{payment_for_vote_success_count}{bcolors.end} successful out of {bcolors.green}{payment_for_vote_success_count+payment_for_vote_failure_count}{bcolors.end} transactions with {bcolors.red}{payment_for_vote_failure_count}{bcolors.end} failed.\n")
for key, value in payment_for_vote_failures.items():
    print(f"{key}: {bcolors.green}{value}{bcolors.end}")

print(f"{bcolors.green}\n\nSMLGAMES(suremanlottery){bcolors.end}")
print(f"We recorded {bcolors.green}{sml_games_success_count}{bcolors.end} successful out of {bcolors.green}{sml_games_success_count+sml_games_failure_count}{bcolors.end} transactions with {bcolors.red}{sml_games_failure_count}{bcolors.end} failed.\n")
for key, value in sml_games_failures.items():
    print(f"{key}: {bcolors.green}{value}{bcolors.end}")

print(f"{bcolors.green}\n\nVOTING CONTEST(votesapp){bcolors.end}")
print(f"We recorded {bcolors.green}{voting_contest_success_count}{bcolors.end} successful out of {bcolors.green}{voting_contest_success_count+voting_contest_failure_count}{bcolors.end} transactions with {bcolors.red}{voting_contest_failure_count}{bcolors.end} failed.\n")
for key, value in voting_contest_failures.items():
    print(f"{key}: {bcolors.green}{value}{bcolors.end}")
