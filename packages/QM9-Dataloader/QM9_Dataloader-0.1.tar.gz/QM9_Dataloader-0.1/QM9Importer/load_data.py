import pickle

def load(pkl_file=r'QM9.pkl'):
    with open(pkl_file, 'rb') as f:
        data = pickle.load(f)

    return data

if __name__ == "__main__":
    load = load()