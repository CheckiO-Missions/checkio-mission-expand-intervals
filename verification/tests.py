"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[[1, 3], [5, 7]]],
            "answer": [1,2,3,5,6,7]
        },
        {
            "input": [[[1, 3]]],
            "answer": [1,2,3]
        },
        {
            "input": [[]],
            "answer": []
        },
        {
            "input": [[[1,2], [4,4]]],
            "answer": [1,2,4]
        }
    ],
    "Extra": [
        {
            "input": [[[1,1], [2,2], [4,4]]],
            "answer": [1,2,4]
        },
        {
            "input": [[[1,4]]],
            "answer": [1,2,3,4]
        },
        {
            "input": [[[5,9], [10, 15]]],
            "answer": [5,6,7,8,9,10,11,12,13,14,15]
        }
    ]
}
