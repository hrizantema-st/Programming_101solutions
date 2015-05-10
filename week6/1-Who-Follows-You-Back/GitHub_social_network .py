from directed_graph import DirectedGraph


class GitHubSocialNetwork:
    LEVEL = 4

    def __init__(self):
        self.network = {}

    def do_you_follow(self, user):
        if user in self.network:
            return True
        return False

    def do_you_follow_indirectly(self, user):
        pass

    def does_he_she_follows(self, user):
        pass

    def does_he_she_follows_indirectly(self, user):
        pass


    my_id = "a2186b354d5c6aa55c27"
    my_sec = "9f10a64ef6b2802730dc26cb78e0c918790cb147"
    r = requests.get('https://api.github.com/users/hrizantema-st?clien_id=my_id&client_secret=my_sec')
    json_r = json.load(r)
    followers_link = json_r["followers_url"]
    following_link = json_r["following_url"]



def build_network(start, level):
    v = set()
    q = []
    v.add(start)
    q.append(start)
    while len(q) != 0:
        cl, cn = q.pop(0)
        if cl > level:
            break
        network = get_network_for(start)
        for follower in network["followers"]:
            if follower not in v:
                g.add_
