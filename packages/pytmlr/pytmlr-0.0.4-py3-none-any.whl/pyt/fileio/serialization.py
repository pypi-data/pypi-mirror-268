import pickle


def serialize(obj):
    return pickle.dumps(obj)


def deserialize(obj):
    return pickle.loads(obj)

