class Friend:
    def __init__(self, name):
        self.__name = name
        self.send_list = {}
        self.total_send = 0
        self.total_recieve = 0
        self.__expected_gift = 0

    def init_friends(self, friends):
        for friend in friends:
            if self.__name != friend:
                self.send_list[friend] = 0

    def send_gift(self, reciever: str):
        self.total_send += 1
        self.send_list[reciever] += 1

    def recieve_gift(self):
        self.total_recieve += 1

    def calculate_present_index(self) -> int:
        return self.total_send - self.total_recieve

    def get_expect_gift(self, given_dict) -> int:
        for k, v in self.send_list.items():
            reciever: Friend = given_dict[k]
            if v > reciever.send_list[self.__name]:
                self.__expected_gift += 1
            if v == reciever.send_list[self.__name]:
                if self.calculate_present_index() > reciever.calculate_present_index():
                    self.__expected_gift += 1

        return self.__expected_gift


def solution(friends, gifts):
    answer = 0
    given_dict = {}

    for friend in friends:
        new_friend = Friend(friend)
        new_friend.init_friends(friends=friends)
        given_dict[friend] = new_friend

    for gift in gifts:
        sender, reciever = gift.split()
        given_dict[sender].send_gift(reciever)
        given_dict[reciever].recieve_gift()

    for _, friend in given_dict.items():
        answer = max(answer, friend.get_expect_gift(given_dict))

    return answer


if __name__ == "__main__":
    result = solution(
        ["muzi", "ryan", "frodo", "neo"],
        [
            "muzi frodo",
            "muzi frodo",
            "ryan muzi",
            "ryan muzi",
            "ryan muzi",
            "frodo muzi",
            "frodo ryan",
            "neo muzi",
        ],
    )

    print(result)
