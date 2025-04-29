"""Homework 4 DS4300 Yasmeen Dao
Builds person/book network and obtains book recommendations
to demonstrate correctness of API
"""
from hw4_api import Api


def main():
    # connect to api
    api = Api()

    # build tree
    api.add_node('Spencer', 'Person')
    api.add_node('Emily', 'Person')
    api.add_node('Brendan', 'Person')
    api.add_node('Trevor', 'Person')
    api.add_node('Paxton', 'Person')
    api.add_node('Cosmos', 'Book', price=17.00)
    api.add_node('Database Design', 'Book', price=195.00)
    api.add_node('The Life of Cronkite', 'Book', price=29.95)
    api.add_node('DNA and you', 'Book', price=11.50)

    api.add_edge('Spencer', 'Emily', 'knows')
    api.add_edge('Emily', 'Spencer', 'knows')
    api.add_edge('Spencer', 'Brendan', 'knows')

    api.add_edge('Spencer', 'Database Design', 'bought')
    api.add_edge('Spencer', 'Cosmos', 'bought')
    api.add_edge('Emily', 'Database Design', 'bought')
    api.add_edge('Brendan', 'Database Design', 'bought')
    api.add_edge('Brendan', 'DNA and you', 'bought')
    api.add_edge('Trevor', 'Database Design', 'bought')
    api.add_edge('Trevor', 'Cosmos', 'bought')
    api.add_edge('Paxton', 'Database Design', 'bought')
    api.add_edge('Paxton', 'The Life of Cronkite', 'bought')

    # api call to test spencer's recommendations
    recs = api.get_recommendations('Spencer')
    # only need person, knows, bought, and book (not price but added to node anyways)
    print("Book Recommendations for Spencer:", recs)

    # test with emily also
    # recs = api.get_recommendations('Emily')
    # print("Book Recommendations for Emily:", recs)

if __name__ == '__main__':
    main()
