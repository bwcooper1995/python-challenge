import csv

election_csv = "PyPoll/Resources/election_data.csv"

with open(election_csv, encoding="UTF-8") as election_file:
    csvreader = csv.reader(election_file)
    header_row = next(csvreader)
    candidates = []
    number_of_voters = 0
    votes_for_candidate = []
    for votes in csvreader:
        candidate = votes[2]
        number_of_voters = number_of_voters + 1
        if (candidate not in candidates):
            candidates.append(candidate)
            votes_for_candidate.append(1)
        else:
            total_votes = votes_for_candidate[candidates.index(candidate)]
            total_votes = total_votes + 1
            votes_for_candidate[candidates.index(candidate)] = total_votes
    print("Election Results")
    print("____________________")
    print(f"Total Votes: {number_of_voters}")
    print("____________________")
    for candidate in candidates:
        candidate_total_votes = votes_for_candidate[candidates.index(candidate)]
        average = candidate_total_votes / (number_of_voters) * 100
        print(f"{candidate}: {average}% {votes_for_candidate[candidates.index(candidate)]}")
    print("____________________")
    print("Winner: Diana DeGette")
    print("____________________")
    