if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    highest_score = max(arr)   

    filtered_scores = [score for score in arr if score != highest_score]


    runner_up_score = max(filtered_scores)

    print(runner_up_score)