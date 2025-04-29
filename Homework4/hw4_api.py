"""File to implement graph API in Redis"""
import redis


class Api:
    def __init__(self):
        # Create a connection and clear the database
        self.r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        self.flush()

    def flush(self):
        self.r.flushall()

    def add_node(self, name, type, price=None):
        """
        add a node to the database of a given name and type
        """
        # self.r.hmset(name, {'type': type})

        node_data = {'type': type}
        if price is not None:
            node_data['price'] = price
        self.r.hmset(name, node_data)

    def add_edge(self, name1, name2, type):
        """
        add an edge between nodes named name1 and name2
        type is type of edge or relationship
        """
        # add members to set
        e_id = f"{name1}:{name2}:{type}"
        self.r.hset(e_id, 'source', name1)
        self.r.hset(e_id, 'destination', name2)
        self.r.hset(e_id, 'type', type)

    def get_adjacent(self, name, node_type=None, edge_type=None):
        """
        get names of adjacent nodes
        """
        adj_nodes = []
        # retrieve all edges associated with the node
        # scan keyes in redis database that match source:destination:edge_type
        for edge_id in self.r.scan_iter("*:*:*"):
            source, destination, edge_type = edge_id.split(":")
            # check if source of edge is same as name node
            if source == name:
                if not node_type or self.r.hget(destination, 'type') == node_type:
                    # add to list if destination matches node_type
                    adj_nodes.append(destination)
            elif destination == name:
                if not node_type or self.r.hget(source, 'type') == node_type:
                    # add to list if destination of edge is same as name node
                    adj_nodes.append(source)
        return adj_nodes

    def get_recommendations(self, name):
        # list of recommendations
        recs = []
        # get all people who know person
        links = self.get_adjacent(name, node_type='Person', edge_type='knows')
        # iterate through each person
        for l in links:
            # for all people get adjacent book node
            books = self.get_adjacent(l, node_type='Book', edge_type='bought')
            recs.extend(books)
        books_bought = self.get_adjacent(name, node_type='Book', edge_type='bought')
        # remove books that exist in both lists
        recs = list(set(recs) - set(books_bought))
        return recs


