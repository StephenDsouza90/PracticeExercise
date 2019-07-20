#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

def split_and_convert(list_of_scores):
    """ Takes in a list of score of a University sports day (here written in a string format),
        which is then converted into a list of integers.
        This list will be used to find the second highest score.
        eg: ['2', '3', '6', '6', '5']
    """
    scores = list_of_scores.split(" ")
    conversion = [int(i) for i in scores]
    return conversion


def get_highest_scores(int_list_of_scores):
    """ Before getting the second highest score,
        we must set the max score to the first highest score.
        We loop through the scores to determine the first highest score.
        eg: 1st iteration is 2 .. max = 2
            2nd iteration is 3 .. since 3 > 2 .. max = 3
            3rd iteration is 6 .. since 6 > 3 .. max = 6
        By doing this, we can determine that the second highest score < the first highest score.
    """
    maxx = int_list_of_scores[0]

    for score in int_list_of_scores:
        if score > maxx:
            maxx = score
    return maxx

def get_second_highest_scores(highest_score, int_list_of_scores):
    """ As we have determined the first highest score, we know that the second highest score < the first highest score.
        In order to determind the second highest score, we can set second highest score to the min value in the list.
        Then as we loop through the list, if the score > min score BUT < highest score = second highest score.
        eg: 1st iteration is 2 .. min score = 2, while highest score = 2
            2nd iteration is 3 .. since 3 > 2 and < highest score = 3 .. min score = 2
            3rd iteration is 6 .. since 6 > 2 and < highest score = 6 .. min score = 2  
    """
    second_maxx = min(int_list_of_scores)
    
    for score in int_list_of_scores:
        if score > second_maxx: 
            if score < highest_score:
                second_maxx = score
    return second_maxx


numbers = input()

results_1 = split_and_convert(numbers)
results_2 = get_highest_scores(results_1)
results_3 = get_second_highest_scores(results_2, results_1)

print(results_3)