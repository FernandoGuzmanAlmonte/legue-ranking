import sys
from collections import defaultdict

class Game:
    def __init__(self, team1, score1, team2, score2):
        self.team1 = team1
        self.score1 = score1
        self.team2 = team2
        self.score2 = score2

class LeagueRanking:
    def __init__(self):
        self.games = []
        self.points = defaultdict(int)
        self.teams = set()

    def parse_input(self, input_lines):
        for line in input_lines:
            if not line.strip():
                continue
            try:
                part1, part2 = line.strip().split(', ')
                team1, score1 = part1.rsplit(' ', 1)
                team2, score2 = part2.rsplit(' ', 1)

                self.games.append(Game(team1, int(score1), team2, int(score2)))
                self.teams.add(team1)
                self.teams.add(team2)
            except ValueError:
                raise ValueError(f"Invalid input format: {line}")

    def calculate_rankings(self):
        for game in self.games:
            if game.score1 > game.score2:
                self.points[game.team1] += 3
            elif game.score1 < game.score2:
                self.points[game.team2] += 3
            else:
                self.points[game.team1] += 1
                self.points[game.team2] += 1

        for team in self.teams:
            if team not in self.points:
                self.points[team] = 0

    def format_rankings(self):
        sorted_teams = sorted(self.points.keys(), key=lambda x: (-self.points[x], x))
        rankings = []
        prev_points = None

        for i, team in enumerate(sorted_teams, start=1):
            current_points = self.points[team]

            if current_points != prev_points:
                rank = i

            rankings.append((rank, team, current_points))
            prev_points = current_points

        return rankings

    def print_rankings(self, rankings):
        for rank, team, pts in rankings:
            pt_str = "pt" if pts == 1 else "pts"
            print(f"{rank}. {team}, {pts} {pt_str}")

def main():
    try:
        if len(sys.argv) != 2:
            print("Use: python league_ranking.py <input_file>", file=sys.stderr)
            sys.exit(1)

        input_file = sys.argv[1]
        with open(input_file, 'r') as file:
            input_lines = file.readlines()

        league = LeagueRanking()
        league.parse_input(input_lines)
        league.calculate_rankings()

        rankings = league.format_rankings()

        league.print_rankings(rankings)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()